const fs = require('fs');
const path = require('path');
const readline = require('readline');

// Caminho da pasta a ser processada
const folderPath = "C:\\Users\\marco\\Documents\\Site\\HTML import";

// Tags disponíveis para escolha
const availableTags = [
  "informação", "cotidiano", "escrita", "ensino", "educação", 
  "podcast", "tecnologia", "internet", "cultura", "arte", 
  "filosofia", "pensamento", "reflexão", "ética", "estética", 
  "política", "pesquisa", "grafos"
];

// Função para extrair texto do markdown (removendo formatação)
function extractPlainText(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, '$1') // Remove bold
    .replace(/\*(.*?)\*/g, '$1')     // Remove italic
    .replace(/\[(.*?)\]\(.*?\)/g, '$1') // Remove links
    .replace(/#{1,6}\s+/g, '')       // Remove headers
    .replace(/`{1,3}.*?`{1,3}/g, '') // Remove code blocks
    .replace(/^\s*>\s*(.*)$/gm, '$1') // Remove blockquotes
    .replace(/!\[\[.*?\]\]/g, '')    // Remove image links
    .replace(/\[\[.*?\]\]/g, '')     // Remove wiki links
}

// Função para sugerir tags com base no conteúdo
function suggestTags(title, content) {
  // Palavras-chave a verificar no título e conteúdo
  const keywordMap = {
    "felicidade": ["filosofia", "reflexão", "ética"],
    "vida": ["filosofia", "reflexão", "cotidiano"],
    "Aristóteles": ["filosofia", "pensamento", "ética"],
    "arte": ["arte", "estética", "cultura"],
    "filosofia": ["filosofia", "pensamento", "reflexão"],
    "educação": ["educação", "ensino", "reflexão"],
    "política": ["política", "ética", "reflexão"],
    "tecnologia": ["tecnologia", "internet", "informação"],
    "cultura": ["cultura", "arte", "reflexão"],
    "ética": ["ética", "filosofia", "reflexão"],
    "caminho": ["reflexão", "filosofia", "cotidiano"],
    "ação humana": ["filosofia", "ética", "reflexão"],
    "maldade": ["ética", "filosofia", "reflexão"],
    "egoísmo": ["ética", "filosofia", "reflexão"]
  };

  const combinedText = (title + " " + content).toLowerCase();
  let suggestedTags = new Set();

  // Buscar palavras-chave no texto
  Object.keys(keywordMap).forEach(keyword => {
    if (combinedText.includes(keyword.toLowerCase())) {
      keywordMap[keyword].forEach(tag => suggestedTags.add(tag));
    }
  });

  // Se não encontrou palavras-chave suficientes, adicione algumas tags padrão
  if (suggestedTags.size < 3) {
    if (combinedText.includes("felicidade") || combinedText.includes("aristóteles")) {
      suggestedTags.add("filosofia");
      suggestedTags.add("reflexão");
      suggestedTags.add("ética");
    } else {
      suggestedTags.add("reflexão");
      suggestedTags.add("cotidiano");
      suggestedTags.add("pensamento");
    }
  }

  // Limitar a 3-5 tags
  return Array.from(suggestedTags).slice(0, 5);
}

// Função para corrigir o formato da data
function fixDateFormat(frontmatter) {
  const dateMatch = frontmatter.match(/date:\s*(\d{2})[-\/](\d{2})[-\/](\d{4})/);
  if (dateMatch) {
    const day = dateMatch[1];
    const month = dateMatch[2];
    const year = dateMatch[3];
    // Formato correto: dia-mês-ano
    return frontmatter.replace(/date:.*/, `date: ${day}-${month}-${year}`);
  }
  
  // Tenta outro formato comum (ano/mês/dia)
  const altDateMatch = frontmatter.match(/date:\s*(\d{2})[-\/](\d{2})[-\/](\d{4})/);
  if (altDateMatch) {
    return frontmatter.replace(/date:.*/, `date: ${altDateMatch[3]}-${altDateMatch[2]}-${altDateMatch[1]}`);
  }
  
  return frontmatter;
}

// Função principal para processar um arquivo
async function processFile(filePath) {
  try {
    // Ler o conteúdo do arquivo
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Dividir o conteúdo em partes
    const parts = content.split('---');
    if (parts.length < 3) {
      console.log(`Formato inválido no arquivo: ${filePath}`);
      return;
    }
    
    let frontmatter = parts[1];
    let mainContent = parts.slice(2).join('---');
    
    // Extrair o título
    const titleMatch = frontmatter.match(/title:\s*(.*)/);
    const title = titleMatch ? titleMatch[1].trim() : '';
    
    // 1. Corrigir o formato da data
    frontmatter = fixDateFormat(frontmatter);
    
    // Extrair o primeiro parágrafo para usar como descrição
    const paragraphs = mainContent.trim().split('\n\n');
    let firstParagraph = '';
    
    // Procurar pelo título repetido e o início do texto
    const titleRepeatRegex = new RegExp(`# ${title}\\s*[^\\n]*\\n---`, 'i');
    const titleRepeatMatch = mainContent.match(titleRepeatRegex);
    
    if (titleRepeatMatch) {
      // 2. Remover o trecho repetido (título + início do texto + linha separadora)
      mainContent = mainContent.replace(titleRepeatMatch[0], '');
      
      // Extrair o trecho inicial para a descrição
      const introText = titleRepeatMatch[0].replace(new RegExp(`# ${title}\\s*`, 'i'), '').replace('---', '').trim();
      firstParagraph = introText;
    } else {
      // Se não encontrou o padrão específico, use o primeiro parágrafo como descrição
      for (const para of paragraphs) {
        if (para.trim() && !para.startsWith('# ') && !para.startsWith('> [!')) {
          firstParagraph = extractPlainText(para);
          break;
        }
      }
    }
    
    // 3. Atualizar o campo "description"
    if (firstParagraph) {
      // Limitar a descrição a cerca de 150-200 caracteres
      const shortDescription = firstParagraph.substring(0, 180) + (firstParagraph.length > 180 ? '...' : '');
      frontmatter = frontmatter.replace(/description:.*/, `description: ${shortDescription}`);
    }
    
    // 4. Adicionar tags com base no conteúdo
    const plainContent = extractPlainText(mainContent);
    const suggestedTags = suggestTags(title, plainContent);
    
    // Atualizar as tags no frontmatter
    if (frontmatter.includes('tags:')) {
      // Encontrar onde termina o bloco de tags
      const tagsBlockRegex = /tags:(?:\n\s*-\s*.*)*(?=\n[^\s-]|$)/;
      const tagsMatch = frontmatter.match(tagsBlockRegex);
      
      if (tagsMatch) {
        const tagsBlock = tagsMatch[0];
        const newTagsBlock = `tags:\n  - ${suggestedTags.join('\n  - ')}`;
        frontmatter = frontmatter.replace(tagsBlock, newTagsBlock);
      }
    } else {
      // Adicionar bloco de tags se não existir
      const newTagsBlock = `tags:\n  - ${suggestedTags.join('\n  - ')}`;
      frontmatter += `\n${newTagsBlock}`;
    }
    
    // Reconstruir o conteúdo do arquivo
    const newContent = `---\n${frontmatter.trim()}\n---\n${mainContent.trim()}\n`;
    
    // Escrever de volta ao arquivo
    fs.writeFileSync(filePath, newContent);
    console.log(`Arquivo processado: ${path.basename(filePath)}`);
    
  } catch (error) {
    console.error(`Erro ao processar o arquivo ${filePath}:`, error);
  }
}

// Função para processar todos os arquivos na pasta
async function processAllFiles() {
  try {
    const files = fs.readdirSync(folderPath);
    
    let processedCount = 0;
    for (const file of files) {
      if (file.endsWith('.md')) {
        const filePath = path.join(folderPath, file);
        await processFile(filePath);
        processedCount++;
      }
    }
    
    console.log(`\nProcessamento concluído. ${processedCount} arquivos foram atualizados.`);
  } catch (error) {
    console.error('Erro ao processar os arquivos:', error);
  }
}

// Iniciar o processamento
console.log('Iniciando processamento dos arquivos markdown...');
processAllFiles();
