import os
import re

# --- CONFIGURAÇÃO ---
# Verifique se este é o caminho correto para sua pasta de posts.
PASTA_POSTS = r'C:\Users\marco\Documents\marcosramon.github.io\_posts'
# --- FIM DA CONFIGURAÇÃO ---


def processar_arquivo(caminho_arquivo):
    """
    Encontra e remove linhas de hashtags que estão imediatamente antes
    da seção "Leia também".
    """
    print(f"Verificando arquivo: {os.path.basename(caminho_arquivo)}")
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo_original = f.read()

        # Regex para encontrar uma linha de hashtags seguida pelo div.
        # Ele captura o div (grupo 1) para mantê-lo na substituição.
        pattern = re.compile(
            r'(?:#\S+\s*)+\n*(<div class="leia-tambem" markdown="1">)',
            re.IGNORECASE
        )

        # A substituição por r'\1' apaga tudo, exceto o que foi capturado no grupo 1 (a tag div).
        conteudo_novo = pattern.sub(r'\1', conteudo_original)

        # Salva o arquivo apenas se houver alguma alteração.
        if conteudo_novo != conteudo_original:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_novo)
            print("  -> Linha de hashtags removida com sucesso!")
        else:
            print("  -> Padrão de hashtags problemático não encontrado. Nenhum ajuste feito.")

    except Exception as e:
        print(f"  -> ERRO ao processar o arquivo: {e}")

def main():
    """
    Função principal que percorre e processa todos os arquivos.
    """
    if not os.path.isdir(PASTA_POSTS):
        print(f"ERRO: A pasta '{PASTA_POSTS}' não foi encontrada.")
        return

    print(f"Iniciando a remoção de hashtags finais na pasta: {PASTA_POSTS}\n")
    
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


# Esta é a forma correta de chamar a função principal.
if __name__ == "__main__":
    main()