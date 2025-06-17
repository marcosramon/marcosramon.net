import os
import re
import random
import yaml
from typing import List, Tuple, Optional

# Lista de tags preferenciais
TAGS_PREFERENCIAIS = [
    "informação", "cotidiano", "escrita", "ensino", "educação", "podcast", 
    "tecnologia", "internet", "cultura", "arte", "filosofia", "pensamento", 
    "reflexão", "ética", "estética", "política", "pesquisa", "grafos", 
    "consumo", "comportamento", "ciência", "leitura", "livros", 
    "quadrinhos", "felicidade", "comunicação", "música", "conhecimento"
]

def extrair_yaml_frontmatter(conteudo: str) -> Tuple[Optional[dict], str]:
    """Extrai o frontmatter YAML do início do arquivo."""
    yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = yaml_pattern.match(conteudo)
    
    if match:
        yaml_content = match.group(1)
        try:
            yaml_data = yaml.safe_load(yaml_content)
            conteudo_sem_yaml = conteudo[match.end():]
            return yaml_data, conteudo_sem_yaml
        except yaml.YAMLError:
            return None, conteudo
    
    return None, conteudo

def verificar_tags_existentes(conteudo: str) -> bool:
    """Verifica se já existem tags antes do último callout."""
    # Padrão para encontrar o último callout
    ultimo_callout_pattern = re.compile(r'---\s*\n>\s*\[\!leia\]')
    
    # Padrão para verificar se há tags (#tag) antes do último callout
    tags_pattern = re.compile(r'#[\w-]+\s+#[\w-]+\s*\n+---\s*\n>\s*\[\!leia\]')
    
    # Verificar se o texto tem o formato esperado (com último callout)
    if not ultimo_callout_pattern.search(conteudo):
        return False
    
    # Verificar se já existem tags antes do último callout
    return bool(tags_pattern.search(conteudo))

def extrair_tags_do_yaml(yaml_data: dict) -> List[str]:
    """Extrai as tags do frontmatter YAML."""
    if not yaml_data or 'tags' not in yaml_data:
        return []
    
    tags = yaml_data['tags']
    if isinstance(tags, list):
        return tags
    elif isinstance(tags, str):
        return [tag.strip() for tag in tags.split(',')]
    
    return []

def gerar_tags_do_conteudo(titulo: str, conteudo: str) -> List[str]:
    """Gera tags relevantes com base no título e conteúdo do texto."""
    texto_completo = (titulo + " " + conteudo).lower()
    tags_relevantes = []
    
    for tag in TAGS_PREFERENCIAIS:
        if tag.lower() in texto_completo:
            tags_relevantes.append(tag)
    
    # Se não encontrou tags suficientes, adiciona algumas aleatórias da lista
    if len(tags_relevantes) < 2:
        tags_disponiveis = [tag for tag in TAGS_PREFERENCIAIS if tag not in tags_relevantes]
        num_tags_faltando = 2 - len(tags_relevantes)
        tags_aleatorias = random.sample(tags_disponiveis, min(num_tags_faltando, len(tags_disponiveis)))
        tags_relevantes.extend(tags_aleatorias)
    
    return tags_relevantes

def adicionar_tags(conteudo: str, tags: List[str]) -> str:
    """Adiciona as tags antes do último callout."""
    # Garantir que temos exatamente duas tags
    if len(tags) > 2:
        tags_selecionadas = random.sample(tags, 2)
    elif len(tags) < 2:
        # Complementar com tags aleatórias se necessário
        tags_disponiveis = [tag for tag in TAGS_PREFERENCIAIS if tag not in tags]
        tags_complementares = random.sample(tags_disponiveis, 2 - len(tags))
        tags_selecionadas = tags + tags_complementares
    else:
        tags_selecionadas = tags
    
    # Formatar as tags (hashtag + nome)
    tags_formatadas = " ".join([f"#{tag}" for tag in tags_selecionadas])
    
    # Inserir as tags antes do último callout
    padrao_callout = re.compile(r'((?:\n|^)---\s*\n>\s*\[\!leia\])')
    conteudo_modificado = padrao_callout.sub(f"\n\n{tags_formatadas}\n\n---\n> [!leia]", conteudo)
    
    return conteudo_modificado

def processar_arquivo(caminho_arquivo: str) -> None:
    """Processa um único arquivo Markdown do Obsidian."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        # Verifica se já existem tags antes do último callout
        if verificar_tags_existentes(conteudo):
            print(f"[IGNORADO] {os.path.basename(caminho_arquivo)} - Já possui tags antes do callout")
            return
        
        # Extrai o frontmatter YAML
        yaml_data, conteudo_sem_yaml = extrair_yaml_frontmatter(conteudo)
        
        # Determina as tags a serem adicionadas
        tags = []
        if yaml_data and 'tags' in yaml_data:
            # Extrai tags do YAML frontmatter
            tags = extrair_tags_do_yaml(yaml_data)
            print(f"[INFO] {os.path.basename(caminho_arquivo)} - Extraindo tags do YAML: {tags}")
        
        if not tags:
            # Gera tags com base no conteúdo
            titulo = yaml_data.get('title', '') if yaml_data else ''
            tags = gerar_tags_do_conteudo(titulo, conteudo_sem_yaml)
            print(f"[INFO] {os.path.basename(caminho_arquivo)} - Gerando tags do conteúdo: {tags}")
        
        # Adiciona as tags ao conteúdo
        conteudo_modificado = adicionar_tags(conteudo, tags)
        
        # Salva o arquivo modificado
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_modificado)
        
        print(f"[SUCESSO] {os.path.basename(caminho_arquivo)} - Tags adicionadas: {' '.join(['#' + tag for tag in tags[:2]])}")
    
    except Exception as e:
        print(f"[ERRO] {os.path.basename(caminho_arquivo)} - {str(e)}")

def processar_pasta(caminho_pasta: str) -> None:
    """Processa todos os arquivos Markdown em uma pasta."""
    contador = {'total': 0, 'modificados': 0, 'ignorados': 0, 'erros': 0}
    
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.md'):
            contador['total'] += 1
            caminho_completo = os.path.join(caminho_pasta, arquivo)
            
            try:
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                if verificar_tags_existentes(conteudo):
                    contador['ignorados'] += 1
                    continue
                
                processar_arquivo(caminho_completo)
                contador['modificados'] += 1
            
            except Exception as e:
                print(f"[ERRO] {arquivo} - {str(e)}")
                contador['erros'] += 1
    
    print(f"\nResumo:")
    print(f"Total de arquivos: {contador['total']}")
    print(f"Arquivos modificados: {contador['modificados']}")
    print(f"Arquivos ignorados (já têm tags): {contador['ignorados']}")
    print(f"Erros: {contador['erros']}")

if __name__ == "__main__":
    caminho_pasta = r"C:\Users\marco\Documents\Site\Blog"
    
    # Confirma com o usuário antes de prosseguir
    print(f"Este script irá processar todos os arquivos .md na pasta: {caminho_pasta}")
    confirmacao = input("Deseja continuar? (s/n): ")
    
    if confirmacao.lower() == 's':
        processar_pasta(caminho_pasta)
    else:
        print("Operação cancelada pelo usuário.")
