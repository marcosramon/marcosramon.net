const fs = require('fs');
const path = require('path');

// Caminhos das pastas a serem verificadas
const folders = [
    'C:\\Users\\marco\\Documents\\Site\\Blog',
    'C:\\Users\\marco\\Documents\\Site\\Podcast'
];

// Função para processar um arquivo
function processFile(filePath) {
    try {
        // Ler o conteúdo do arquivo
        let content = fs.readFileSync(filePath, 'utf8');
        let originalContent = content;
        let modified = false;

        // Padrão para encontrar callouts "leia" e "abstract"
        const calloutPattern = /> \[\!(leia|abstract)\](.*?)(?=\n[^>]|\n*$)/gs;
        
        // Coletar todos os callouts do arquivo
        const callouts = [];
        let match;
        while ((match = calloutPattern.exec(content)) !== null) {
            callouts.push({
                type: match[1], // leia ou abstract
                fullText: match[0],
                start: match.index,
                end: match.index + match[0].length
            });
        }

        // Processar os callouts se houver mais de um
        if (callouts.length > 1) {
            // Ordenar em ordem reversa para que a remoção não afete os índices
            callouts.sort((a, b) => b.start - a.start);
            
            // Encontrar o callout "leia" que deve ser mantido (geralmente o último)
            const keepCalloutIndex = callouts.findIndex(c => c.type === 'leia');
            
            if (keepCalloutIndex !== -1) {
                // Extrair o callout a ser mantido
                const keepCallout = callouts[keepCalloutIndex];
                
                // Processar o callout que será mantido para remover linhas vazias
                let keepCalloutText = keepCallout.fullText;
                keepCalloutText = keepCalloutText.replace(/> - \n/g, ''); // Remover itens vazios
                keepCalloutText = keepCalloutText.replace(/> -\n/g, ''); // Versão alternativa
                
                // Corrigir links com "1" no final
                keepCalloutText = keepCalloutText.replace(/\[\[(.*?) 1\]\]/g, '[[$1]]');
                
                // Atualizar o conteúdo substituindo o callout original pelo corrigido
                content = content.substring(0, keepCallout.start) + 
                          keepCalloutText + 
                          content.substring(keepCallout.end);
                
                // Remover outros callouts
                callouts.forEach((callout, index) => {
                    if (index !== keepCalloutIndex) {
                        // Ajustar índices após modificação anterior
                        const offset = keepCallout.start < callout.start ? 
                                      (keepCalloutText.length - keepCallout.fullText.length) : 0;
                        
                        const adjustedStart = callout.start + offset;
                        const adjustedEnd = callout.end + offset;
                        
                        // Remover este callout
                        content = content.substring(0, adjustedStart) + 
                                 content.substring(adjustedEnd);
                    }
                });
                
                modified = true;
            }
        } else if (callouts.length === 1) {
            // Se houver apenas um callout, ainda precisamos verificar se é do tipo correto e remover linhas vazias
            const callout = callouts[0];
            
            if (callout.type === 'abstract') {
                // Remover callout abstract
                content = content.substring(0, callout.start) + content.substring(callout.end);
                modified = true;
            } else if (callout.type === 'leia') {
                // Corrigir o callout "leia" para remover linhas vazias
                let keepCalloutText = callout.fullText;
                keepCalloutText = keepCalloutText.replace(/> - \n/g, ''); // Remover itens vazios
                keepCalloutText = keepCalloutText.replace(/> -\n/g, ''); // Versão alternativa
                
                // Corrigir links com "1" no final
                keepCalloutText = keepCalloutText.replace(/\[\[(.*?) 1\]\]/g, '[[$1]]');
                
                // Atualizar apenas se houver alterações
                if (keepCalloutText !== callout.fullText) {
                    content = content.substring(0, callout.start) + 
                              keepCalloutText + 
                              content.substring(callout.end);
                    modified = true;
                }
            }
        }

        // Salvar o arquivo apenas se foi modificado
        if (modified && content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`Arquivo corrigido: ${filePath}`);
            return true;
        }
        
        return false;
    } catch (error) {
        console.error(`Erro ao processar o arquivo ${filePath}:`, error);
        return false;
    }
}

// Função para percorrer recursivamente os diretórios
function processDirectory(dirPath) {
    const files = fs.readdirSync(dirPath);
    let totalProcessed = 0;
    let totalFixed = 0;
    
    for (const file of files) {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);
        
        if (stats.isDirectory()) {
            // Processar subdiretório recursivamente
            const subResults = processDirectory(filePath);
            totalProcessed += subResults.processed;
            totalFixed += subResults.fixed;
        } else if (stats.isFile() && filePath.endsWith('.md')) {
            // Processar arquivo Markdown
            totalProcessed++;
            if (processFile(filePath)) {
                totalFixed++;
            }
        }
    }
    
    return { processed: totalProcessed, fixed: totalFixed };
}

// Iniciar o processamento
let grandTotalProcessed = 0;
let grandTotalFixed = 0;

console.log('Iniciando correção dos callouts...');
for (const folder of folders) {
    console.log(`\nProcessando pasta: ${folder}`);
    
    try {
        const results = processDirectory(folder);
        grandTotalProcessed += results.processed;
        grandTotalFixed += results.fixed;
        
        console.log(`Arquivos processados: ${results.processed}`);
        console.log(`Arquivos corrigidos: ${results.fixed}`);
    } catch (error) {
        console.error(`Erro ao processar a pasta ${folder}:`, error);
    }
}

console.log('\n=== Resumo ===');
console.log(`Total de arquivos processados: ${grandTotalProcessed}`);
console.log(`Total de arquivos corrigidos: ${grandTotalFixed}`);
console.log('Correção concluída!');
