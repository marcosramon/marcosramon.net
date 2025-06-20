import os
import re

# --- CONFIGURAÇÃO ---
# Verifique se este é o caminho correto para sua pasta de posts.
PASTA_POSTS = r'C:\Users\marco\Documents\marcosramon.github.io\_posts'
# --- FIM DA CONFIGURAÇÃO ---


def processar_arquivo(caminho_arquivo):
    """
    Encontra a seção "Leia também" formatada com <h3> e a substitui
    pelo novo formato com <div class="leia-tambem">.
    """
    print(f"Verificando arquivo: {os.path.basename(caminho_arquivo)}")
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo_original = f.read()

        # Regex para encontrar o bloco inteiro, incluindo o "---" opcional.
        # Captura a lista de links para reutilização.
        pattern = re.compile(
            r'(?:\n---\n)?\s*<h3>Leia também:</h3>\s*((?:- <a href=.*(?:\n|$))*)',
            re.IGNORECASE
        )

        match = pattern.search(conteudo_original)

        # Se não encontrar o padrão, não faz nada no arquivo.
        if not match:
            print("  -> Seção 'Leia também' no formato antigo não encontrada. Pulando.")
            return

        # O grupo 1 contém a lista de links que queremos preservar.
        lista_de_links = match.group(1).strip()
        
        # *** A CORREÇÃO ESTÁ AQUI ***
        # Adicionado '\n\n' no início para garantir a separação da linha anterior.
        bloco_novo = (
            f'\n\n<div class="leia-tambem" markdown="1">\n'
            f'## Leia também:\n\n'
            f'{lista_de_links}\n'
            f'</div>'
        )

        # Substitui o bloco antigo encontrado pelo novo bloco.
        # count=1 garante que a substituição ocorra apenas uma vez por arquivo.
        conteudo_novo = pattern.sub(bloco_novo, conteudo_original, count=1)

        # Salva o arquivo apenas se houver alguma alteração.
        if conteudo_novo != conteudo_original:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_novo)
            print("  -> Seção 'Leia também' atualizada com sucesso!")
        else:
            print("  -> Nenhuma alteração foi necessária.")

    except Exception as e:
        print(f"  -> ERRO ao processar o arquivo: {e}")

def main():
    """
    Função principal que percorre e processa todos os arquivos.
    """
    if not os.path.isdir(PASTA_POSTS):
        print(f"ERRO: A pasta '{PASTA_POSTS}' não foi encontrada.")
        print("Por favor, verifique o caminho da variável PASTA_POSTS no início do script.")
        return

    print(f"Iniciando a atualização da seção 'Leia também' na pasta: {PASTA_POSTS}\n")
    
    arquivos_markdown = [f for f in os.listdir(PASTA_POSTS) if f.lower().endswith(('.md', '.markdown'))]
    
    if not arquivos_markdown:
        print("Nenhum arquivo Markdown encontrado na pasta.")
        return
        
    total_arquivos = len(arquivos_markdown)
    print(f"Encontrados {total_arquivos} arquivos para verificar.\n")

    for i, nome_arquivo in enumerate(arquivos_markdown):
        caminho_completo = os.path.join(PASTA_POSTS, nome_arquivo)
        processar_arquivo(caminho_completo)
        print("-" * 20)

    print("\nProcesso concluído!")

if __name__ == "__main__":
    main()