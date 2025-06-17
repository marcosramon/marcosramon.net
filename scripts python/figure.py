import os
import re

def convert_markdown_link_to_html(markdown_link):
    # Converte links no formato [texto](url) para <a href="url">texto</a>
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(link_pattern, r'<a href="\2">\1</a>', markdown_link)

def convert_figure_to_obsidian(content):
    # Padrão para encontrar blocos figure com seus conteúdos
    figure_pattern = r'<figure[^>]*>\s*<img src="[^"]*?/assets/images/([^"]*?)"[^>]*>\s*<figcaption>(.*?)</figcaption>\s*</figure>'
    
    def replacement(match):
        image_name = match.group(1)
        caption = match.group(2).strip()
        
        # Verifica se há links markdown na legenda e converte para HTML
        if '[' in caption and '](' in caption:
            caption = convert_markdown_link_to_html(caption)
            
        return f"\n![[arquivos/{image_name}]]\n<small>{caption}</small>\n"
    
    return re.sub(figure_pattern, replacement, content)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Aplica a conversão de figure para o formato Obsidian
        updated_content = convert_figure_to_obsidian(content)
        
        # Se o conteúdo foi modificado, escreve de volta no arquivo
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Imagens convertidas em: {file_path}")
        else:
            print(f"Nenhuma imagem para converter em: {file_path}")
    
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")

def process_directory(directory_path):
    count = 0
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, filename)
                process_file(file_path)
                count += 1
    
    print(f"\nProcessamento concluído! {count} arquivos verificados.")

if __name__ == "__main__":
    directory_path = r"C:\Users\marco\Documents\Site\Textos revisados\Textos para blog"
    print(f"Iniciando processamento na pasta: {directory_path}")
    process_directory(directory_path)
