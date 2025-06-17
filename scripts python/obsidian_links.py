import os
import re
import glob
from collections import defaultdict
import random

# Caminhos para as pastas
BLOG_PATH = r"C:\Users\marco\Documents\Site\Blog"
PODCAST_PATH = r"C:\Users\marco\Documents\Site\Podcast"

def extract_title(content):
    """Extrai o título do arquivo markdown."""
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1)
    
    # Tenta extrair do frontmatter
    frontmatter_match = re.search(r'---\s+title:\s*"?([^"\n]+)"?\s+', content)
    if frontmatter_match:
        return frontmatter_match.group(1)
    
    # Retorna o nome do arquivo como último recurso
    return None

def extract_tags(content):
    """Extrai as tags do conteúdo."""
    # Procura tags no frontmatter
    frontmatter_match = re.search(r'---\s+.*?tags:\s*\[(.*?)\]', content, re.DOTALL)
    if frontmatter_match:
        tags_str = frontmatter_match.group(1)
        return [tag.strip().strip('"\'') for tag in tags_str.split(',')]
    
    # Procura tags no formato #tag
    hashtag_matches = re.findall(r'#(\w+)', content)
    if hashtag_matches:
        return hashtag_matches
    
    return []

def extract_first_paragraph(content):
    """Extrai o primeiro parágrafo do texto."""
    # Remove o frontmatter
    content_without_frontmatter = re.sub(r'---\s+.*?---\s+', '', content, flags=re.DOTALL)
    
    # Remove os títulos
    content_without_titles = re.sub(r'^#.*$', '', content_without_frontmatter, flags=re.MULTILINE)
    
    # Encontra o primeiro parágrafo real
    paragraph_match = re.search(r'\n\n(.*?)\n\n', content_without_titles, re.DOTALL)
    if paragraph_match:
        return paragraph_match.group(1).strip()
    
    return ""

def check_and_fix_callout(content):
    """Verifica e corrige o formato do callout 'Leia também'."""
    # Procura pelo callout no formato [!abstract]
    abstract_pattern = r'> \[!abstract\] Leia também:'
    if re.search(abstract_pattern, content):
        content = re.sub(abstract_pattern, '> [!leia] Leia também:', content)
    
    # Verifica se o callout já existe
    leia_pattern = r'> \[!leia\] Leia também:'
    if not re.search(leia_pattern, content):
        # Adiciona o callout no final do arquivo
        content += "\n\n---\n> [!leia] Leia também:\n> -\n> -\n> -"
    
    return content

def extract_existing_links(content):
    """Extrai links existentes no callout 'Leia também'."""
    callout_match = re.search(r'> \[!(?:leia|abstract)\] Leia também:(?:\n> - (?:\[\[(.*?)\]\])?)*', content, re.DOTALL)
    if not callout_match:
        return []
    
    callout_content = callout_match.group(0)
    link_matches = re.findall(r'> - \[\[(.*?)\]\]', callout_content)
    return link_matches

def has_complete_links(content):
    """Verifica se o callout já possui 3 links preenchidos."""
    existing_links = extract_existing_links(content)
    return len(existing_links) >= 3

def similarity_score(file1_info, file2_info):
    """Calcula o score de similaridade entre dois arquivos."""
    score = 0
    
    # Pontuação baseada em tags comuns
    common_tags = set(file1_info["tags"]) & set(file2_info["tags"])
    score += len(common_tags) * 5
    
    # Pontuação baseada em palavras comuns no título
    title1_words = set(file1_info["title"].lower().split()) if file1_info["title"] else set()
    title2_words = set(file2_info["title"].lower().split()) if file2_info["title"] else set()
    common_title_words = title1_words & title2_words
    score += len(common_title_words) * 3
    
    # Pontuação baseada no primeiro parágrafo
    para1_words = set(file1_info["first_paragraph"].lower().split())
    para2_words = set(file2_info["first_paragraph"].lower().split())
    common_para_words = para1_words & para2_words
    score += len(common_para_words) * 0.5
    
    # Bônus para correspondência de "podcast" nos títulos
    if "podcast" in file1_info["title"].lower() and "podcast" in file2_info["title"].lower():
        score += 10
    
    return score

def find_related_files(target_file, all_files_info, num_links=3):
    """Encontra arquivos relacionados com base em similaridade."""
    target_info = all_files_info[target_file]
    
    similarity_scores = []
    for file, info in all_files_info.items():
        if file != target_file:  # Não inclui o próprio arquivo
            score = similarity_score(target_info, info)
            similarity_scores.append((file, score))
    
    # Ordena por score de similaridade (mais alto primeiro)
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Retorna os N arquivos mais similares
    return [file for file, score in similarity_scores[:num_links]]

def update_callout_links(content, related_files):
    """Atualiza o callout com os links relacionados."""
    # Extrai os links existentes
    existing_links = extract_existing_links(content)
    
    # Mantém os links existentes e adiciona novos até completar 3
    final_links = existing_links.copy()
    
    # Adiciona novos links sem duplicar
    for file in related_files:
        link_text = os.path.splitext(os.path.basename(file))[0]
        if link_text not in existing_links and len(final_links) < 3:
            final_links.append(link_text)
    
    # Se ainda não tivermos 3 links, adicione mais relacionados
    while len(final_links) < 3 and len(related_files) > len(final_links) - len(existing_links):
        for file in related_files:
            link_text = os.path.splitext(os.path.basename(file))[0]
            if link_text not in final_links and len(final_links) < 3:
                final_links.append(link_text)
    
    # Atualiza o callout
    callout_text = f"> [!leia] Leia também:\n"
    for link in final_links:
        callout_text += f"> - [[{link}]]\n"
    
    # Adiciona linhas vazias se necessário
    while len(final_links) < 3:
        callout_text += "> -\n"
        final_links.append(None)
    
    # Substitui o callout antigo pelo novo
    old_callout_pattern = r'> \[!(?:leia|abstract)\] Leia também:(?:\n> - (?:\[\[.*?\]\])?)*'
    content = re.sub(old_callout_pattern, callout_text.rstrip(), content, flags=re.DOTALL)
    
    return content, final_links

def ensure_all_files_referenced(all_files_info, files_referenced):
    """Garante que todos os arquivos sejam referenciados pelo menos uma vez."""
    unreferenced_files = set(all_files_info.keys()) - set(files_referenced)
    files_to_update = {}
    
    for unreferenced_file in unreferenced_files:
        # Encontra um arquivo aleatório que ainda não tem 3 links
        potential_files = [file for file in all_files_info.keys() 
                          if file != unreferenced_file and 
                          len(extract_existing_links(all_files_info[file]["content"])) < 3]
        
        if potential_files:
            # Escolhe um arquivo aleatório
            target_file = random.choice(potential_files)
            
            # Se esse arquivo ainda não está na lista para atualização, adiciona-o
            if target_file not in files_to_update:
                files_to_update[target_file] = []
            
            # Adiciona o arquivo não referenciado à lista de links
            files_to_update[target_file].append(unreferenced_file)
            
            # Atualiza a lista de arquivos referenciados
            files_referenced.add(unreferenced_file)
    
    return files_to_update

def main():
    # Coleta todos os arquivos markdown
    blog_files = glob.glob(os.path.join(BLOG_PATH, "*.md"))
    podcast_files = glob.glob(os.path.join(PODCAST_PATH, "*.md"))
    all_files = blog_files + podcast_files
    
    # Dicionário para armazenar informações de cada arquivo
    all_files_info = {}
    
    # Coleta informações de cada arquivo
    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                title = extract_title(content) or os.path.splitext(os.path.basename(file_path))[0]
                tags = extract_tags(content)
                first_paragraph = extract_first_paragraph(content)
                
                all_files_info[file_path] = {
                    "content": content,
                    "title": title,
                    "tags": tags,
                    "first_paragraph": first_paragraph
                }
        except Exception as e:
            print(f"Erro ao processar {file_path}: {e}")
    
    # Rastreia os arquivos que foram referenciados
    files_referenced = set()
    files_updated = []
    
    # Processa cada arquivo
    for file_path, file_info in all_files_info.items():
        content = file_info["content"]
        
        # Verifica e corrige o formato do callout
        content = check_and_fix_callout(content)
        
        # Verifica se o callout já está completo
        if not has_complete_links(content):
            # Encontra arquivos relacionados
            related_files = find_related_files(file_path, all_files_info)
            
            # Atualiza o callout
            content, final_links = update_callout_links(content, related_files)
            
            # Atualiza as informações do arquivo
            all_files_info[file_path]["content"] = content
            
            # Marca os arquivos como atualizados
            files_updated.append(file_path)
            
            # Adiciona os arquivos referenciados à lista
            for link in final_links:
                if link:
                    # Adiciona o arquivo correspondente ao link
                    for f in all_files:
                        if os.path.splitext(os.path.basename(f))[0] == link:
                            files_referenced.add(f)
                            break
    
    # Garante que todos os arquivos do blog sejam referenciados
    additional_updates = ensure_all_files_referenced(
        {f: info for f, info in all_files_info.items() if f in blog_files},
        files_referenced
    )
    
    # Aplica as atualizações adicionais
    for file_path, related_files in additional_updates.items():
        content = all_files_info[file_path]["content"]
        
        # Atualiza o callout
        content, _ = update_callout_links(content, related_files)
        
        # Atualiza as informações do arquivo
        all_files_info[file_path]["content"] = content
        
        # Marca o arquivo como atualizado se ainda não estiver
        if file_path not in files_updated:
            files_updated.append(file_path)
    
    # Escreve as alterações nos arquivos
    for file_path in files_updated:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(all_files_info[file_path]["content"])
            print(f"Atualizado: {file_path}")
        except Exception as e:
            print(f"Erro ao atualizar {file_path}: {e}")
    
    print(f"\nTotal de arquivos atualizados: {len(files_updated)}")

if __name__ == "__main__":
    main()
