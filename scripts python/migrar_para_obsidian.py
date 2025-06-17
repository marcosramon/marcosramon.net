import os
import re
import shutil
from datetime import datetime
import yaml

# Configuração de caminhos
ORIGIN_FOLDER = r"C:\Users\marco\Documents\Site\Revisar"
IMAGES_ORIGIN_FOLDER = r"C:\Users\marco\Documents\Site\images"
IMAGES_DEST_FOLDER = r"C:\Users\marco\Documents\Site\arquivos"
TEXTS_DEST_FOLDER = r"C:\Users\marco\Documents\Site\Textos revisados"

# Garantir que as pastas de destino existam
os.makedirs(IMAGES_DEST_FOLDER, exist_ok=True)
os.makedirs(TEXTS_DEST_FOLDER, exist_ok=True)

# Padrão para encontrar a seção de front matter (metadados)
FRONT_MATTER_PATTERN = r"^---\n(.*?)\n---"

# Função para converter a data para o formato brasileiro
def convert_date(date_str):
    try:
        # Formatos possíveis: YYYY-MM-DD HH:MM:SS Z ou YYYY-MM-DD
        if ' ' in date_str:
            date_part = date_str.split(' ')[0]
        else:
            date_part = date_str
        
        year, month, day = date_part.split('-')
        return f"{day}/{month}/{year}"
    except Exception as e:
        print(f"Erro ao converter data '{date_str}': {e}")
        return date_str

# Função para extrair informações do nome do arquivo
def extract_info_from_filename(filename):
    # Padrão esperado: YYYY-MM-DD-titulo-do-post.md
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.*?)\.md", filename)
    if match:
        year, month, day, slug = match.groups()
        return {
            'date': f"{day}/{month}/{year}",
            'original_date': f"{year}-{month}-{day}"
        }
    return None

# Função para processar as imagens no conteúdo
def process_images(content, filename_without_ext):
    # Encontrar todas as referências a imagens no formato: <img src="/assets/images/nome-da-imagem.jpg">
    img_pattern = r'<img src="(/assets/images/([^"]+))">'
    
    def replace_image(match):
        original_path = match.group(1)
        image_filename = match.group(2)
        
        # Caminho completo para a imagem original e de destino
        original_image_path = os.path.join(IMAGES_ORIGIN_FOLDER, image_filename)
        dest_image_path = os.path.join(IMAGES_DEST_FOLDER, image_filename)
        
        # Copiar a imagem se existir
        if os.path.exists(original_image_path):
            shutil.copy2(original_image_path, dest_image_path)
            print(f"Imagem copiada: {image_filename}")
        else:
            print(f"AVISO: Imagem não encontrada: {image_filename}")
        
        # Retornar o novo formato de imagem para o Obsidian
        return f'![[{image_filename}]]'
    
    # Substituir todas as ocorrências de imagens
    new_content = re.sub(img_pattern, replace_image, content)
    return new_content

# Função principal para processar cada arquivo
def process_file(filename):
    filepath = os.path.join(ORIGIN_FOLDER, filename)
    
    # Extrair informações do nome do arquivo
    filename_info = extract_info_from_filename(filename)
    if not filename_info:
        print(f"AVISO: O arquivo {filename} não segue o padrão esperado de nomenclatura.")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Encontrar a seção de front matter
        match = re.search(FRONT_MATTER_PATTERN, content, re.DOTALL)
        if not match:
            print(f"AVISO: Não foi possível encontrar o front matter em {filename}")
            return False
        
        # Extrair o front matter e o conteúdo real
        front_matter_text = match.group(1)
        real_content = content[match.end():].strip()
        
        # Parsear o front matter
        front_matter = yaml.safe_load(front_matter_text)
        
        # Modificar o front matter
        new_front_matter = {
            'title': front_matter.get('title', ''),
            'date': convert_date(front_matter.get('date', filename_info['original_date'])),
            'author': "Marcos Ramon",
            'description': front_matter.get('excerpt', ''),
            'tags': front_matter.get('tags', []),
            'published': front_matter.get('published', True)
        }
        
        # Adicionar o callout com a data no início
        original_date_parts = filename_info['original_date'].split('-')
        callout_date = f"{original_date_parts[2]}/{original_date_parts[1]}/{original_date_parts[0]}"
        date_callout = f"> [!data] <small><i>Por Marcos Ramon, em {callout_date}</i></small>\n\n"
        
        # Adicionar o callout de "Leia também" no final
        related_callout = "\n\n> [!leia] Leia também\n> - \n> - \n> - "
        
        # Processar as imagens no conteúdo
        filename_without_ext = os.path.splitext(filename)[0]
        processed_content = process_images(real_content, filename_without_ext)
        
        # Montar o novo conteúdo
        new_front_matter_text = yaml.dump(new_front_matter, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_front_matter_text}---\n\n{date_callout}{processed_content}{related_callout}"
        
        # Criar o novo nome de arquivo (sem a data no início)
        title_slug = '-'.join(new_front_matter['title'].lower().split())
        new_filename = f"{title_slug}.md"
        new_filepath = os.path.join(TEXTS_DEST_FOLDER, new_filename)
        
        # Salvar o novo arquivo
        with open(new_filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"Arquivo processado com sucesso: {filename} -> {new_filename}")
        return True
    
    except Exception as e:
        print(f"Erro ao processar o arquivo {filename}: {e}")
        return False

# Função para processar todos os arquivos
def process_all_files():
    success_count = 0
    fail_count = 0
    
    for filename in os.listdir(ORIGIN_FOLDER):
        if filename.endswith('.md'):
            if process_file(filename):
                success_count += 1
            else:
                fail_count += 1
    
    print(f"\nProcessamento concluído!")
    print(f"Arquivos processados com sucesso: {success_count}")
    print(f"Arquivos com erro: {fail_count}")

# Executar o script
if __name__ == "__main__":
    print("Iniciando migração de arquivos para o Obsidian Publish...")
    process_all_files()
