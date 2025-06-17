import os
import re
import yaml
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from datetime import datetime
import string

# Configuração inicial
TEXTS_FOLDER = r"C:\Users\marco\Documents\Site\Textos revisados"

# Baixar recursos do NLTK necessários (execute apenas uma vez)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Palavras de parada em português
stop_words = set(stopwords.words('portuguese'))
# Adicionar palavras de parada adicionais específicas para os textos
custom_stop_words = {'é', 'ser', 'estar', 'ter', 'haver', 'fazer', 'ir', 'vir', 'mesmo', 'apenas', 'também'}
stop_words = stop_words.union(custom_stop_words)

# Padrão para encontrar a seção de front matter (metadados)
FRONT_MATTER_PATTERN = r"^---\n(.*?)\n---"

def extract_content(text):
    """Extrai o conteúdo principal, removendo front matter e callouts"""
    # Remover front matter
    text = re.sub(r'^---.*?---\s*', '', text, flags=re.DOTALL)
    
    # Remover callouts
    text = re.sub(r'> \[!.*?\].*?(?=\n\n|\Z)', '', text, flags=re.DOTALL)
    
    return text.strip()

def correct_date_format(date_str):
    """Converte a data para o formato DD-MM-YYYY"""
    try:
        # Tenta identificar o formato da data
        if isinstance(date_str, str):
            # Se for no formato YYYY-MM-DD
            if re.match(r'^\d{4}-\d{2}-\d{2}', date_str):
                year, month, day = date_str.split('-', 2)
                # Se houver hora ou timezone, descartar
                day = day.split(' ')[0].split('T')[0]
                return f"{day}-{month}-{year}"
            
            # Se for no formato DD/MM/YYYY
            elif re.match(r'^\d{2}/\d{2}/\d{4}', date_str):
                day, month, year = date_str.split('/', 2)
                return f"{day}-{month}-{year}"
            
            # Outros formatos possíveis...
            else:
                return date_str  # Retorna sem alteração se formato não reconhecido
        return date_str
    except Exception as e:
        print(f"Erro ao corrigir formato de data '{date_str}': {e}")
        return date_str

def generate_description(content, max_length=160):
    """Gera uma descrição a partir do conteúdo do texto"""
    if not content.strip():
        return ""
    
    # Extrair a primeira sentença ou as primeiras X caracteres
    sentences = sent_tokenize(content)
    if sentences:
        description = sentences[0]
        # Limitar tamanho
        if len(description) > max_length:
            description = description[:max_length].rstrip() + "..."
        return description
    return ""

def generate_tags(content, max_tags=5):
    """Gera tags a partir do conteúdo do texto"""
    if not content.strip():
        return []
    
    # Tokenizar e limpar o texto
    tokens = word_tokenize(content.lower())
    
    # Remover pontuação e números
    tokens = [word for word in tokens if word not in string.punctuation and not word.isdigit()]
    
    # Remover stop words
    filtered_tokens = [word for word in tokens if word not in stop_words and len(word) > 3]
    
    # Contar frequência de palavras
    word_freq = {}
    for word in filtered_tokens:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Selecionar as palavras mais frequentes como tags
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Capitalizar a primeira letra de cada tag
    tags = [word.capitalize() for word, _ in sorted_words[:max_tags]]
    
    # Adicionar algumas tags comuns baseadas em padrões no texto
    if re.search(r'\blivro|\bleitura|\bescrever|\btexto|\bescrita\b', content, re.IGNORECASE):
        if 'Literatura' not in tags:
            tags.append('Literatura')
    
    if re.search(r'\bpensar|\bpensamento|\bideia|\bconceito|\bfilosofia\b', content, re.IGNORECASE):
        if 'Filosofia' not in tags:
            tags.append('Filosofia')
    
    if re.search(r'\bvida|\bcotidiano|\bdia a dia|\brotina\b', content, re.IGNORECASE):
        if 'Cotidiano' not in tags:
            tags.append('Cotidiano')
            
    if re.search(r'\bpodcast|\bepisódio|\bficções|\báudio\b', content, re.IGNORECASE):
        if 'Podcast' not in tags:
            tags.append('Podcast')
    
    return tags[:max_tags]  # Limitar ao número máximo de tags

def process_file(filepath):
    """Processa um arquivo, corrigindo a data e adicionando tags e description se necessário"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Encontrar o front matter
        match = re.search(FRONT_MATTER_PATTERN, content, re.DOTALL)
        if not match:
            print(f"AVISO: Não foi possível encontrar o front matter em {filepath}")
            return False
        
        front_matter_text = match.group(1)
        
        try:
            front_matter = yaml.safe_load(front_matter_text)
        except Exception as e:
            print(f"Erro ao parsear o front matter de {filepath}: {e}")
            return False
        
        # Extrair o conteúdo para análise
        main_content = extract_content(content)
        
        # Correções e adições ao front matter
        if 'date' in front_matter:
            front_matter['date'] = correct_date_format(front_matter['date'])
        
        # Adicionar description se estiver vazia
        if 'description' not in front_matter or not front_matter['description']:
            front_matter['description'] = generate_description(main_content)
        
        # Adicionar tags se estiver vazia
        if 'tags' not in front_matter or not front_matter['tags']:
            front_matter['tags'] = generate_tags(main_content)
        
        # Criar novo front matter
        new_front_matter = yaml.dump(front_matter, allow_unicode=True, sort_keys=False)
        
        # Substituir o front matter antigo pelo novo
        new_content = content.replace(match.group(0), f"---\n{new_front_matter}---")
        
        # Salvar o arquivo atualizado
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        return True
    
    except Exception as e:
        print(f"Erro ao processar o arquivo {filepath}: {e}")
        return False

def enhance_all_files():
    """Processa todos os arquivos na pasta e subpastas"""
    total_files = 0
    success_count = 0
    error_count = 0
    
    print("Iniciando aprimoramento de metadados...")
    
    # Função recursiva para processar arquivos em uma pasta e suas subpastas
    def process_folder(folder_path):
        nonlocal total_files, success_count, error_count
        
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            
            # Se for uma pasta, processa recursivamente
            if os.path.isdir(item_path):
                process_folder(item_path)
            # Se for um arquivo markdown, processa
            elif item.endswith('.md'):
                total_files += 1
                print(f"Processando: {item}")
                
                if process_file(item_path):
                    success_count += 1
                else:
                    error_count += 1
    
    # Iniciar o processamento a partir da pasta raiz
    process_folder(TEXTS_FOLDER)
    
    print("\nAprimoramento concluído!")
    print(f"Total de arquivos processados: {total_files}")
    print(f"Arquivos atualizados com sucesso: {success_count}")
    print(f"Arquivos com erro: {error_count}")

if __name__ == "__main__":
    enhance_all_files()
