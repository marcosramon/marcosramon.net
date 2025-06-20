import os
import re
import yaml # Certifique-se de que PyYAML está instalado: pip install pyyaml

# --- CONFIGURAÇÃO ---
PASTA_POSTS = r'C:\Users\marco\Documents\marcosramon.github.io\_posts'
# --- FIM DA CONFIGURAÇÃO ---

def substituir_wikilink(match):
    """
    Função auxiliar para o re.sub.
    Recebe um match de wikilink e retorna o texto de exibição.
    Ex: [[Elena Ferrante]] -> "Elena Ferrante"
    Ex: [[Virginia Woolf|Woolf]] -> "Woolf"
    """
    conteudo_interno = match.group(1)
    # Pega a parte depois do "|" se existir, senão, o conteúdo inteiro.
    return conteudo_interno.split('|')[-1]

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

        # --- TAREFA 1: Adicionar 'author' ao Frontmatter ---
        dados_frontmatter = yaml.safe_load(frontmatter_str) or {}
        if 'author' not in dados_frontmatter:
            dados_frontmatter['author'] = 'Marcos Ramon'
            print("  -> Adicionando 'author: Marcos Ramon'.")
        
        # Converte o dicionário de volta para uma string YAML formatada
        # O allow_unicode garante que acentos sejam mantidos corretamente.
        novo_frontmatter_str = yaml.dump(dados_frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False)

        # --- TAREFA 2: Atualizar o formato do "Leia também" ---
        # Regex para encontrar o bloco de citação do "Leia também"
        leia_tambem_regex = re.compile(r'> Leia também:\n((?:> .*(?:\n|$))*)', re.IGNORECASE)
        
        match_leia = leia_tambem_regex.search(corpo_markdown)
        if match_leia:
            print("  -> Formatando a seção 'Leia também'.")
            # Pega apenas a lista de links (grupo 1 da regex)
            lista_links = match_leia.group(1)
            # Remove o "> " do início de cada linha da lista
            lista_links_limpa = re.sub(r'^> ', '', lista_links, flags=re.MULTILINE)
            
            # Monta o novo bloco com <h3> e a lista limpa
            bloco_novo = f"<h3>Leia também:</h3>\n{lista_links_limpa.strip()}"
            
            # Substitui o bloco antigo pelo novo no corpo do texto
            corpo_markdown = leia_tambem_regex.sub(bloco_novo, corpo_markdown, count=1)

        # --- TAREFA 3: Converter wikilinks para texto simples ---
        wikilink_regex = re.compile(r'\[\[(.*?)\]\]')
        # Verifica se há wikilinks antes de tentar substituir
        if wikilink_regex.search(corpo_markdown):
            print("  -> Convertendo wikilinks para texto simples.")
            corpo_markdown = wikilink_regex.sub(substituir_wikilink, corpo_markdown)

        # Reconstrói o arquivo com as alterações
        novo_conteudo_completo = f"---\n{novo_frontmatter_str.strip()}\n---\n{corpo_markdown.strip()}\n"

        # Salva as alterações no mesmo arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo_completo)
        
        print("  -> Arquivo atualizado com sucesso.")

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