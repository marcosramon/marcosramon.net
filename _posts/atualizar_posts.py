import os
import re
import yaml
import shutil
from unidecode import unidecode

# --- CONFIGURAÇÃO ---
# Altere para o caminho exato da sua pasta de posts.
# Usei 'r' antes da string para o Python lidar corretamente com as barras invertidas do Windows.
PASTA_POSTS = r'C:\Users\marco\Documents\marcosramon.github.io\_posts'
# --- FIM DA CONFIGURAÇÃO ---


def slugify(text):
    """
    Converte um texto em um formato "slug" amigável para URLs.
    Ex: "A beleza do absurdo" -> "a-beleza-do-absurdo"
    """
    # Converte para minúsculas e remove acentos
    text = unidecode(text).lower()
    # Mantém apenas letras, números e hífens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # Substitui espaços por hífens
    text = re.sub(r'\s+', '-', text).strip('-')
    return text


def processar_arquivo(caminho_arquivo):
    """
    Aplica todas as transformações necessárias em um único arquivo.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo_completo = f.read()

        # 1. Separar o YAML frontmatter do resto do conteúdo
        partes = conteudo_completo.split('---', 2)
        if len(partes) < 3:
            print(f"  -> AVISO: Arquivo não parece ter um frontmatter YAML. Pulando: {os.path.basename(caminho_arquivo)}")
            return

        frontmatter_str = partes[1]
        corpo_markdown = partes[2]
        
        # Carregar o frontmatter para obter os metadados
        metadados = yaml.safe_load(frontmatter_str)
        
        titulo = metadados.get('title')
        data = metadados.get('date')

        if not titulo or not data:
            print(f"  -> ERRO: Título ou data não encontrados no frontmatter. Pulando: {os.path.basename(caminho_arquivo)}")
            return

        # 2. Remover o callout [!data]
        # Esta regex procura por "> [!data]" seguido por qualquer coisa até o final da linha,
        # e opcionalmente por uma linha em branco logo após.
        corpo_markdown_novo = re.sub(r'>\s*\[!data\].*?\n\n?', '', corpo_markdown, flags=re.IGNORECASE)

        # 3. Alterar formato da imagem
        # Captura o nome do arquivo dentro de ![[...]] e o substitui pelo formato <img>
        corpo_markdown_novo = re.sub(
            r'!\[\[(.*?)\]\]',
            r'<img src="/assets/img/\1">',
            corpo_markdown_novo
        )
        
        # 4. Retirar o callout do final ([!leia])
        # Procura pela linha horizontal, a linha do callout e as substitui.
        corpo_markdown_novo = re.sub(
            r'\n---\n>\s*\[!leia\]\s*(Leia também:)',
            r'\n> \1',
            corpo_markdown_novo,
            flags=re.IGNORECASE
        )

        # Monta o novo conteúdo do arquivo
        novo_conteudo_completo = f"---\n{frontmatter_str.strip()}\n---\n{corpo_markdown_novo.lstrip()}"

        # Define o novo nome do arquivo
        slug_titulo = slugify(titulo)
        nome_arquivo_antigo = os.path.basename(caminho_arquivo)
        novo_nome_arquivo = f"{data}-{slug_titulo}.md"
        novo_caminho_arquivo = os.path.join(os.path.dirname(caminho_arquivo), novo_nome_arquivo)

        # Salva o conteúdo no novo arquivo
        with open(novo_caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo_completo)
        
        print(f"  -> Processado e salvo como: {novo_nome_arquivo}")

        # Se o nome do arquivo antigo for diferente do novo, apaga o antigo.
        if caminho_arquivo.lower() != novo_caminho_arquivo.lower():
            os.remove(caminho_arquivo)
            print(f"  -> Arquivo original '{nome_arquivo_antigo}' removido.")
            
    except Exception as e:
        print(f"  -> ERRO ao processar o arquivo {os.path.basename(caminho_arquivo)}: {e}")


def main():
    """
    Função principal que percorre a pasta e processa os arquivos.
    """
    if not os.path.isdir(PASTA_POSTS):
        print(f"ERRO: A pasta '{PASTA_POSTS}' não foi encontrada.")
        print("Por favor, verifique o caminho no início do script.")
        return

    print(f"Iniciando a atualização de arquivos na pasta: {PASTA_POSTS}\n")
    
    # Lista todos os arquivos que terminam com .md ou .markdown
    arquivos_markdown = [f for f in os.listdir(PASTA_POSTS) if f.lower().endswith(('.md', '.markdown'))]
    
    total_arquivos = len(arquivos_markdown)
    print(f"Encontrados {total_arquivos} arquivos Markdown para processar.\n")

    for i, nome_arquivo in enumerate(arquivos_markdown):
        caminho_completo = os.path.join(PASTA_POSTS, nome_arquivo)
        if os.path.isfile(caminho_completo):
            print(f"Processando arquivo {i+1}/{total_arquivos}: {nome_arquivo}...")
            processar_arquivo(caminho_completo)
            print("-" * 20)

    print("\nProcesso concluído!")

# Executa a função principal
if __name__ == "__main__":
    # Para rodar o script sem a dependência `unidecode`, comente a linha `from unidecode import unidecode`
    # e descomente a próxima linha `import unicodedata`. Você também precisará ajustar a função `slugify`.
    # Se você instalou o `unidecode`, não precisa fazer nada.
    main()