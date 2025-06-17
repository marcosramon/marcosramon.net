import os
import re
import requests
import shutil
from datetime import datetime
import urllib.parse

def download_image(image_url, save_path, new_filename):
    """Download an image from a URL and save it with a new filename."""
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        
        # Extract file extension from URL or default to .jpeg
        ext = os.path.splitext(urllib.parse.urlparse(image_url).path)[1]
        if not ext:
            ext = '.jpeg'
            
        full_path = os.path.join(save_path, new_filename + ext)
        
        with open(full_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        
        return new_filename + ext
    except Exception as e:
        print(f"Erro ao baixar imagem {image_url}: {e}")
        return None

def parse_month(month_str):
    """Convert English month name to month number."""
    months = {
        'january': '01', 'february': '02', 'march': '03', 'april': '04',
        'may': '05', 'june': '06', 'july': '07', 'august': '08',
        'september': '09', 'october': '10', 'november': '11', 'december': '12'
    }
    return months.get(month_str.lower(), '01')

def format_date(date_str):
    """Convert date string from 'Month Day, Year' to 'DD-MM-YYYY'."""
    try:
        # Extract components from "January 2, 2017"
        match = re.search(r'(\w+)\s+(\d+),\s+(\d{4})', date_str)
        if match:
            month, day, year = match.groups()
            month_num = parse_month(month)
            day_num = day.zfill(2)
            return f"{day_num}-{month_num}-{year}", f"{day_num}/{month_num}/{year}"
        return "01-01-2023", "01/01/2023"  # Default date if parsing fails
    except Exception as e:
        print(f"Erro ao processar data {date_str}: {e}")
        return "01-01-2023", "01/01/2023"  # Default date if any error occurs

def extract_tags_from_content(content):
    """Extract potential tags from content based on common words and themes."""
    # This is a simple implementation - could be improved with NLP
    potential_tags = ['arte', 'filosofia', 'comportamento', 'tecnologia', 
                     'educação', 'cultura', 'política', 'sociedade']
    
    content_lower = content.lower()
    found_tags = []
    
    for tag in potential_tags:
        if tag in content_lower:
            found_tags.append(tag)
    
    # Add at least one tag if none found
    if not found_tags:
        found_tags = ['pensamentos']
        
    return found_tags

def extract_authors(content):
    """Extract mentioned authors as aliases."""
    # Look for potential author names in the format [Name](link)
    author_matches = re.findall(r'\[([^]]+)\]\(http', content)
    
    # Filter out the author's own name
    aliases = [f"[[{author}]]" for author in author_matches if "Marcos Ramon" not in author]
    
    return aliases

def process_markdown_file(file_path, images_dir):
    """Process a single markdown file imported from Medium."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract title
        title_match = re.search(r'^### (.+?)$', content, re.MULTILINE)
        if not title_match:
            title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
        
        if not title_match:
            print(f"Não foi possível extrair o título do arquivo: {file_path}")
            return
            
        title = title_match.group(1).strip()
        
        # Extract date
        date_match = re.search(r'on \[([^]]+)\]', content)
        if date_match:
            date_str = date_match.group(1)
            formatted_date, display_date = format_date(date_str)
        else:
            formatted_date, display_date = "01-01-2023", "01/01/2023"
        
        # Extract content (main text)
        # Remove everything from "By [Marcos Ramon]..." onwards
        main_content = re.sub(r'By \[Marcos Ramon\].*', '', content, flags=re.DOTALL)
        
        # Remove duplicate headers
        if title_match:
            main_content = re.sub(r'^# .*?\n---\n', '', main_content, flags=re.MULTILINE)
            main_content = re.sub(r'^### .*?\n', '', main_content, flags=re.MULTILINE)
        
        # Extract and process images
        img_matches = re.findall(r'!\[\]\((https?://[^)]+)\)', main_content)
        for i, img_url in enumerate(img_matches):
            image_name = f"{title.lower().replace(' ', '-')}-medium"
            if len(img_matches) > 1:
                image_name += f"-{i+1}"
                
            new_image_filename = download_image(img_url, images_dir, image_name)
            
            if new_image_filename:
                # Replace image URL with local path
                main_content = main_content.replace(
                    f'![]({img_url})', 
                    f'![[{new_image_filename}]]'
                )
        
        # Extract tags and aliases
        tags = extract_tags_from_content(main_content)
        aliases = extract_authors(main_content)
        
        # Create new frontmatter
        frontmatter = f"""---
title: {title}
date: {formatted_date}
tags:
{chr(10).join('  - ' + tag for tag in tags)}
description: {title}
image: 
aliases:
{chr(10).join('  - ' + alias for alias in aliases)}
---"""

        # Add initial callout
        callout_start = f"> [!data] <small><i>Por Marcos Ramon, em {display_date}</i></small>"
        
        # Add final callout
        callout_end = """---
> [!leia] Leia também:
> - 
> - 
> - """
        
        # Combine all parts
        new_content = f"{frontmatter}\n\n{callout_start}\n\n{main_content.strip()}\n\n{callout_end}"
        
        # Create new filename
        new_filename = f"{title}.md"
        new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
        
        # Write the new file
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(new_content)
        
        # If the new filename is different from the original, remove the original
        if os.path.abspath(file_path) != os.path.abspath(new_file_path):
            os.remove(file_path)
            
        print(f"Processado: {new_filename}")
        
    except Exception as e:
        print(f"Erro ao processar arquivo {file_path}: {e}")

def main():
    # Directory paths
    markdown_dir = r"C:\Users\marco\Documents\Site\HTML import"
    images_dir = r"C:\Users\marco\Documents\Site\arquivos"
    
    # Make sure the directories exist
    os.makedirs(images_dir, exist_ok=True)
    
    # Process all markdown files in the directory
    for filename in os.listdir(markdown_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(markdown_dir, filename)
            process_markdown_file(file_path, images_dir)
            
    print("Processamento concluído!")

if __name__ == "__main__":
    main()
