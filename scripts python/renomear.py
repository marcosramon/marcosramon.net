import os

def rename_files_in_folder(folder_path):
    try:
        # Lista todos os arquivos na pasta
        for file_name in os.listdir(folder_path):
            # Verifica se o arquivo é um arquivo markdown
            if file_name.endswith('.md'):
                # Separa o nome do arquivo e a extensão
                name, ext = os.path.splitext(file_name)
                
                # Transforma o nome para ter apenas a primeira letra maiúscula
                if len(name) > 1:
                    new_name = name[0] + name[1:].lower()
                else:
                    new_name = name.upper()
                
                # Renomeia o arquivo
                os.rename(
                    os.path.join(folder_path, file_name),
                    os.path.join(folder_path, new_name + ext)
                )
                print(f"Renomeado: {file_name} -> {new_name + ext}")
        
        return "Renomeação de arquivos concluída com sucesso."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Define o caminho da nova pasta
folder_path = r"C:\Users\marco\Documents\Site\Textos revisados\Posts para podcast"

# Chama a função
resultado = rename_files_in_folder(folder_path)
print(resultado)
print("\nPressione Enter para sair...")
input()  # Espera o usuário pressionar Enter antes de fechar
