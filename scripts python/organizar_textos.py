import os
import re
import shutil
import yaml

# Configuração de caminhos
TEXTS_FOLDER = r"C:\Users\marco\Documents\Site\Textos revisados"
BLOG_FOLDER = os.path.join(TEXTS_FOLDER, "Textos para blog")
PODCAST_FOLDER = os.path.join(TEXTS_FOLDER, "Posts para podcast")

# Garantir que as pastas de destino existam
os.makedirs(BLOG_FOLDER, exist_ok=True)
os.makedirs(PODCAST_FOLDER, exist_ok=True)

# Padrão para encontrar a seção de front matter (metadados)
FRONT_MATTER_PATTERN = r"^---\n(.*?)\n---"

def is_podcast_post(content, front_matter):
    """
    Determina se um arquivo é um post de podcast com base em:
    1. Presença de iframe com anchor.fm ou outro serviço de podcast
    2. Tags que incluem 'podcast'
    3. Menção a 'podcast', 'episódio', 'Ficções' no conteúdo
    """
    # Verificar se há iframe de podcast
    if re.search(r'<iframe[^>]*anchor\.fm|<iframe[^>]*spotify\.com|<iframe[^>]*apple\.com/podcast', content, re.IGNORECASE):
        return True
    
    # Verificar tags
    if 'tags' in front_matter and front_matter['tags']:
        if isinstance(front_matter['tags'], list) and 'podcast' in [tag.lower() if isinstance(tag, str) else '' for tag in front_matter['tags']]:
            return True
        elif isinstance(front_matter['tags'], str) and 'podcast' in front_matter['tags'].lower():
            return True
    
    # Verificar menções específicas no conteúdo
    podcast_keywords = ['ficções', 'ficçoes', 'podcast ficções', 'episódio do podcast', 'novo episódio']
    for keyword in podcast_keywords:
        if keyword.lower() in content.lower():
            return True
    
    # Verificar título
    if 'title' in front_matter and front_matter['title']:
        title = front_matter['title'].lower()
        if 'podcast' in title or 'ficções' in title or 'ficçoes' in title or 'episódio' in title:
            return True
    
    return False

def organize_files():
    """
    Lê todos os arquivos na pasta de textos revisados,
    identifica se são posts de blog ou podcast e os move para a pasta apropriada.
    """
    total_files = 0
    podcast_count = 0
    blog_count = 0
    error_count = 0
    
    print("Iniciando organização de arquivos...")
    
    for filename in os.listdir(TEXTS_FOLDER):
        # Ignorar subdiretórios e arquivos não markdown
        if not filename.endswith('.md') or os.path.isdir(os.path.join(TEXTS_FOLDER, filename)):
            continue
        
        filepath = os.path.join(TEXTS_FOLDER, filename)
        total_files += 1
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Encontrar e analisar o front matter
            match = re.search(FRONT_MATTER_PATTERN, content, re.DOTALL)
            front_matter = {}
            
            if match:
                front_matter_text = match.group(1)
                try:
                    front_matter = yaml.safe_load(front_matter_text)
                except Exception as e:
                    print(f"Erro ao parsear o front matter de {filename}: {e}")
            
            # Determinar se é um post de podcast ou blog
            if is_podcast_post(content, front_matter):
                dest_folder = PODCAST_FOLDER
                podcast_count += 1
                file_type = "podcast"
            else:
                dest_folder = BLOG_FOLDER
                blog_count += 1
                file_type = "blog"
            
            # Mover o arquivo para a pasta correspondente
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(filepath, dest_path)
            print(f"Arquivo '{filename}' classificado como {file_type} e movido para a pasta correspondente.")
            
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")
            error_count += 1
    
    print("\nOrganização concluída!")
    print(f"Total de arquivos processados: {total_files}")
    print(f"Arquivos de podcast: {podcast_count}")
    print(f"Arquivos de blog: {blog_count}")
    print(f"Erros encontrados: {error_count}")

if __name__ == "__main__":
    organize_files()
