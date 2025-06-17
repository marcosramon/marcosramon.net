const fs = require('fs');
const path = require('path');

// Função para normalizar o texto (remover acentos, caracteres especiais e converter para minúsculas)
function normalizeText(text) {
    // Remove a extensão .md se estiver presente
    text = text.replace(/\.md$/, '');
    
    // Normaliza os caracteres com acentos
    return text
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '') // Remove acentos
        .toLowerCase()
        .replace(/[^\w\s-]/g, '') // Remove caracteres especiais exceto espaços e hífens
        .replace(/\s+/g, '-') // Substitui espaços por hífens
        .replace(/-+/g, '-'); // Remove hífens duplicados
}

// Função para processar um arquivo
function processFile(filePath, isFromPodcast) {
    try {
        // Lê o conteúdo do arquivo
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Obtém o nome do arquivo sem a extensão
        const fileName = path.basename(filePath, '.md');
        
        // Gera o permalink normalizado
        const normalizedName = normalizeText(fileName);
        const permalink = isFromPodcast ? `ficcoes/${normalizedName}` : normalizedName;
        
        // Verifica se já existe um permalink nas propriedades
        if (content.includes('permalink:')) {
            // Substitui o permalink existente
            const updatedContent = content.replace(/permalink:.*(\r\n|\r|\n)/g, `permalink: ${permalink}\n`);
            fs.writeFileSync(filePath, updatedContent);
        } else {
            // Verifica se já existe uma seção de frontmatter (YAML) no início do arquivo
            if (content.startsWith('---')) {
                // Encontra o final do frontmatter para adicionar o permalink antes dele
                const endOfFrontmatter = content.indexOf('---', 3);
                if (endOfFrontmatter !== -1) {
                    const updatedContent = 
                        content.substring(0, endOfFrontmatter) + 
                        `permalink: ${permalink}\n` + 
                        content.substring(endOfFrontmatter);
                    fs.writeFileSync(filePath, updatedContent);
                } else {
                    // Se não encontrar o final do frontmatter, adiciona ao início
                    const updatedContent = `---\npermalink: ${permalink}\n---\n${content}`;
                    fs.writeFileSync(filePath, updatedContent);
                }
            } else {
                // Se não existir frontmatter, adiciona um novo
                const updatedContent = `---\npermalink: ${permalink}\n---\n\n${content}`;
                fs.writeFileSync(filePath, updatedContent);
            }
        }
        
        console.log(`Processado: ${filePath} -> permalink: ${permalink}`);
    } catch (error) {
        console.error(`Erro ao processar o arquivo ${filePath}:`, error);
    }
}

// Função para processar todos os arquivos em um diretório
function processDirectory(directoryPath, isFromPodcast) {
    try {
        // Lê todos os arquivos do diretório
        const files = fs.readdirSync(directoryPath);
        
        let count = 0;
        // Processa cada arquivo
        for (const file of files) {
            // Verifica se é um arquivo .md
            if (file.endsWith('.md')) {
                const filePath = path.join(directoryPath, file);
                processFile(filePath, isFromPodcast);
                count++;
            }
        }
        
        console.log(`Total de arquivos processados em ${directoryPath}: ${count}`);
    } catch (error) {
        console.error(`Erro ao processar o diretório ${directoryPath}:`, error);
    }
}

// Caminhos para os diretórios
const blogDirectory = 'C:\\Users\\marco\\Documents\\Site\\Blog';
const podcastDirectory = 'C:\\Users\\marco\\Documents\\Site\\Podcast';

// Executa o processamento
console.log('Iniciando processamento dos permalinks...');
console.log('Processando arquivos de blog...');
processDirectory(blogDirectory, false);
console.log('Processando arquivos de podcast...');
processDirectory(podcastDirectory, true);
console.log('Processamento concluído!');
