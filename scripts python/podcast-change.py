import os
import re
from datetime import datetime
import yaml

def convert_date_format(date_str):
    try:
        # Parse the date string
        date_obj = datetime.strptime(date_str.split('+')[0].strip(), '%Y-%m-%d %H:%M:%S')
        # Format to Brazilian format
        return date_obj.strftime('%d-%m-%Y')
    except Exception as e:
        print(f"Error converting date: {e}")
        return date_str

def extract_description(content):
    # Try to find a meaningful description after the iframe
    iframe_pattern = r'<iframe.*?</iframe>\s*(.*?)(?:\n|$)'
    match = re.search(iframe_pattern, content, re.DOTALL)
    if match and match.group(1).strip():
        return match.group(1).strip()
    return "Episódio do podcast Ficções"

def convert_figure_to_obsidian(content):
    # Pattern to match figure blocks
    figure_pattern = r'<figure[^>]*>[\s\S]*?<img src="[^"]*?/assets/images/([^"]*?)"[^>]*>[\s\S]*?<figcaption>(.*?)</figcaption>[\s\S]*?</figure>'
    
    def replacement(match):
        image_name = match.group(1)
        caption = match.group(2).strip()
        return f"\n![[arquivos/{image_name}]]\n<small>{caption}</small>\n"
    
    return re.sub(figure_pattern, replacement, content)

def add_podcast_callout(content):
    # Find the "Leia também" section and add the podcast callout after it
    leia_pattern = r'(> \[!leia\] Leia também\s*>\s*-\s*>\s*-\s*>\s*-)'
    if re.search(leia_pattern, content):
        return re.sub(leia_pattern, r'\1\n\n> [!podcast] Sobre o podcast [[Podcast/Ficções|Ficções]].\n', content)
    else:
        # If "Leia também" section is not found, add at the end
        return content + "\n\n> [!podcast] Sobre o podcast [[Podcast/Ficções|Ficções]].\n"

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find the YAML front matter
    front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not front_matter_match:
        print(f"No front matter found in {file_path}")
        return
    
    front_matter = front_matter_match.group(1)
    rest_of_content = content[front_matter_match.end():]
    
    # Parse the front matter
    try:
        # Handle the front matter as a string to preserve the original format
        front_matter_dict = yaml.safe_load(front_matter)
        
        # Update the date format
        if 'date' in front_matter_dict:
            front_matter_dict['date'] = convert_date_format(str(front_matter_dict['date']))
        
        # Update the description
        if 'description' in front_matter_dict:
            desc = front_matter_dict['description']
            if '<iframe' in desc:
                front_matter_dict['description'] = extract_description(desc)
        
        # Convert the front matter back to YAML
        new_front_matter = yaml.dump(front_matter_dict, allow_unicode=True, sort_keys=False)
        
        # Process the rest of the content
        new_content = convert_figure_to_obsidian(rest_of_content)
        new_content = add_podcast_callout(new_content)
        
        # Combine the new front matter and content
        updated_content = f"---\n{new_front_matter}---\n{new_content}"
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Successfully processed {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(('.md', '.markdown')):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path)

if __name__ == "__main__":
    directory_path = r"C:\Users\marco\Documents\Site\Textos revisados\Posts para podcast"
    process_directory(directory_path)
    print("Processing complete!")
