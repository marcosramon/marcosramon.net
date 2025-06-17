const fs = require('fs');
const path = require('path');

// Diretório onde os arquivos estão localizados
const diretorio = 'C:\\Users\\marco\\Documents\\Site\\Blog';

// Expressão regular para encontrar os diferentes tipos de callouts no início dos arquivos
const regexCallouts = /^> \[!(note|ensaio|data)\] (.*?)$/m;

// Expressão regular para extrair a data do texto
const regexData = /em (\d{2}\/\d{2}\/\d{4})/;

function processarArquivo(caminhoArquivo) {
    const nomeArquivo = path.basename(caminhoArquivo);
    console.log(`Processando arquivo: ${nomeArquivo}`);
    
    // Ler o conteúdo do arquivo
    let conteudo = fs.readFileSync(caminhoArquivo, 'utf8');
    
    // Verificar se o arquivo já está no formato padrão
    if (conteudo.match(/^> \[!data\] <small><i>Por Marcos Ramon, em \d{2}\/\d{2}\/\d{4}<\/i><\/small>$/m)) {
        console.log(`  ✓ Arquivo já está no formato padrão`);
        return false; // Nenhuma alteração necessária
    }
    
    // Encontrar o callout atual no arquivo
    const match = conteudo.match(regexCallouts);
    if (!match) {
        console.log(`  ⚠ Nenhum callout encontrado no arquivo`);
        return false;
    }
    
    const tipoCallout = match[1]; // note, ensaio ou data
    const conteudoCallout = match[2]; // conteúdo dentro do callout
    
    // Extrair a data do conteúdo do callout, se existir
    let data = '';
    const matchData = conteudo.match(regexData);
    if (matchData) {
        data = matchData[1];
    } else {
        // Se a data não for encontrada, usar a data atual formatada como DD/MM/AAAA
        const hoje = new Date();
        data = `${String(hoje.getDate()).padStart(2, '0')}/${String(hoje.getMonth() + 1).padStart(2, '0')}/${hoje.getFullYear()}`;
        console.log(`  ⚠ Data não encontrada, usando data atual: ${data}`);
    }
    
    // Criar o novo callout no formato padrão
    const novoCallout = `> [!data] <small><i>Por Marcos Ramon, em ${data}</i></small>`;
    
    // Substituir o callout antigo pelo novo
    const novoConteudo = conteudo.replace(match[0], novoCallout);
    
    // Salvar o arquivo com o conteúdo atualizado
    fs.writeFileSync(caminhoArquivo, novoConteudo, 'utf8');
    
    console.log(`  ✓ Callout atualizado: "${match[0]}" -> "${novoCallout}"`);
    return true; // Arquivo foi modificado
}

function processarDiretorio() {
    console.log(`Iniciando processamento no diretório: ${diretorio}`);
    
    let arquivosModificados = 0;
    let totalArquivos = 0;
    
    try {
        // Ler todos os arquivos do diretório
        const arquivos = fs.readdirSync(diretorio);
        
        // Filtrar apenas os arquivos markdown
        const arquivosMd = arquivos.filter(arquivo => arquivo.endsWith('.md'));
        
        totalArquivos = arquivosMd.length;
        console.log(`Encontrados ${totalArquivos} arquivos Markdown`);
        
        // Processar cada arquivo
        for (const arquivo of arquivosMd) {
            const caminhoCompleto = path.join(diretorio, arquivo);
            const modificado = processarArquivo(caminhoCompleto);
            if (modificado) {
                arquivosModificados++;
            }
        }
        
        console.log('\nResumo:');
        console.log(`Total de arquivos processados: ${totalArquivos}`);
        console.log(`Arquivos modificados: ${arquivosModificados}`);
        console.log(`Arquivos já no formato padrão: ${totalArquivos - arquivosModificados}`);
        
    } catch (erro) {
        console.error(`Erro ao processar diretório: ${erro.message}`);
    }
}

// Executar o script
processarDiretorio();
