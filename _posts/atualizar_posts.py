import os
import re
import yaml
from unidecode import unidecode

# --- CONFIGURAÇÃO ---
PASTA_POSTS = r'C:\Users\marco\Documents\marcosramon.github.io\_posts'
# --- FIM DA CONFIGURAÇÃO ---

def slugify(text):
    """Converte um texto em um formato "slug" amigável para URLs."""
    # Remove acentos e converte para minúsculas
    text = unidecode(text).lower()
    # Remove caracteres que não são letras, números, espaços ou hífens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # Substitui espaços e múltiplos hífens por um único hífen
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def processar_leia_tambem(texto_completo):
    """
    Encontra e reformata a seção "Leia também" inteira.
    Converte wikilinks para HTML e limpa a formatação.
    """
    # Regex para encontrar o bloco inteiro do "Leia também", começando com ">"
    bloco_regex = re.compile(r'((?:> .*\n)*> (\[!leia\] )?Leia também:?[\s\S]*)', re.IGNORECASE)
    match = bloco_regex.search(texto_completo)

    if not match:
        return texto_completo # Retorna o texto original se não encontrar a seção

    bloco_antigo = match.group(1)
    links_html = []

    # Processa cada linha dentro do bloco encontrado
    for linha in bloco_antigo.splitlines():
        # Procura por links no formato [[...]]
        link_match = re.search(r'\[\[(.*?)\]\]', linha)
        if link_match:
            conteudo_link = link_match.group(1)

            # Remove o prefixo "Blog/" se existir
            if conteudo_link.startswith('Blog/'):
                conteudo_link = conteudo_link[5:]

            # Separa o título real do texto de exibição (se usar "|")
            partes = conteudo_link.split('|')
            titulo_real = partes[0].strip()
            texto_exibicao = partes[-1].strip()

            # Cria o slug e o link HTML
            slug = slugify(titulo_real)
            link_html = f'<a href="/{slug}">{texto_exibicao}</a>'
            links_html.append(f"> - {link_html}")

    if not links_html:
        # Se não encontrou nenhum link válido, remove o bloco inteiro
        return texto_completo.replace(bloco_antigo, '')

    # Reconstrói a seção com a formatação correta
    bloco_novo = "> Leia também:\n" + "\n".join(links_html)

    # Substitui o bloco antigo pelo novo no texto completo
    return texto_completo.replace(bloco_antigo, bloco_novo)


def processar_arquivo(caminho_arquivo):
    """Aplica todas as transformações de conteúdo em um único arquivo."""
    print(f"Processando: {os.path.basename(caminho_arquivo)}")
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo_completo = f.read()

        # Separa o frontmatter do corpo do texto
        partes = conteudo_completo.split('---', 2)
        if len(partes) < 3:
            print("  -> AVISO: Não foi possível encontrar o frontmatter. Pulando.")
            return

        frontmatter_str = partes[1]
        corpo_markdown = partes[2]
        
        # 1. Ajuste dos caminhos das imagens
        corpo_markdown = corpo_markdown.replace('src="/assets/img/arquivos/', 'src="/assets/img/')

        # 2. Processamento da seção "Leia também"
        corpo_markdown = processar_leia_tambem(corpo_markdown)

        # 3. Limpeza final: remove linhas vazias de marcadores
        corpo_markdown = re.sub(r'>\s*-\s*\n', '', corpo_markdown)

        # Reconstrói o arquivo
        novo_conteudo_completo = f"---\n{frontmatter_str.strip()}\n---\n{corpo_markdown.strip()}\n"

        # Salva as alterações no mesmo arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo_completo)
        
        print("  -> Conteúdo atualizado com sucesso.")

    except Exception as e:
        print(f"  -> ERRO ao processar o arquivo: {e}")

def main():
    """Função principal que percorre e processa todos os arquivos."""
    if not os.path.isdir(PASTA_POSTS):
        print(f"ERRO: A pasta '{PASTA_POSTS}' não foi encontrada.")
        return

    print(f"Iniciando a atualização de conteúdo na pasta: {PASTA_POSTS}\n")
    
    arquivos_markdown = [f for f in os.listdir(PASTA_POSTS) if f.lower().endswith(('.md', '.markdown'))]
    
    total_arquivos = len(arquivos_markdown)
    print(f"Encontrados {total_arquivos} arquivos para verificar e atualizar.\n")

    for i, nome_arquivo in enumerate(arquivos_markdown):
        caminho_completo = os.path.join(PASTA_POSTS, nome_arquivo)
        processar_arquivo(caminho_completo)
        print("-" * 20)

    print("\nProcesso concluído!")

if __name__ == "__main__":
    main()