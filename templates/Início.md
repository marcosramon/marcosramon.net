<%*
// Configuração
const blogFolder = "Blog";
const numeroDePostsRecentes = 15;

// Função para extrair informações do frontmatter
async function extrairInfoPost(arquivo) {
    try {
        const conteudo = await app.vault.read(arquivo);
        const frontmatterMatch = conteudo.match(/^---\n([\s\S]*?)\n---/);
        
        if (!frontmatterMatch) return null;
        
        const frontmatter = frontmatterMatch[1];
        
        // Extrair campos relevantes
        const info = {};
        
        // Data
        const dataMatch = frontmatter.match(/date:\s*(.+)$/m);
        info.data = dataMatch ? dataMatch[1].trim() : null;
        
        // Título
        const tituloMatch = frontmatter.match(/title:\s*(.+)$/m);
        info.titulo = tituloMatch ? tituloMatch[1].trim() : arquivo.basename;
        
        // Descrição
        const descMatch = frontmatter.match(/description:\s*(.+)$/m);
        info.descricao = descMatch ? descMatch[1].trim() : "";
        
        // Permalink
        const permalinkMatch = frontmatter.match(/permalink:\s*(.+)$/m);
        // Se o permalink já vier completo no frontmatter, usa ele; se não, extrai apenas o slug
        let permalink = permalinkMatch ? permalinkMatch[1].trim() : arquivo.basename;
        // Remove qualquer prefixo http se já existir (para padronização)
        if (permalink.startsWith('http')) {
            const url = new URL(permalink);
            permalink = url.pathname.replace(/^\//, ''); // Remove a barra inicial se existir
        }
        info.permalink = permalink;
        
        return info;
    } catch (error) {
        console.error("Erro ao processar arquivo:", arquivo.path, error);
        return null;
    }
}

// Função para formatar data de YYYY-MM-DD para DD.MM.YYYY
function formatarData(dataStr) {
    if (!dataStr) return "";
    
    const match = dataStr.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (match) {
        const [_, ano, mes, dia] = match;
        return `${dia}.${mes}.${ano}`;
    }
    return dataStr;
}

// Obter todos os arquivos do blog
const arquivosBlog = app.vault.getMarkdownFiles()
    .filter(file => file.path.startsWith(blogFolder + "/"));

// Processar arquivos um por um (mais seguro que processar todos de uma vez)
let posts = [];

// Função principal para gerar o template
async function gerarTemplate() {
    // Iniciar a saída sem frontmatter
    let saida = "";
    
    // Processar cada arquivo
    for (const arquivo of arquivosBlog) {
        const info = await extrairInfoPost(arquivo);
        if (info) {
            posts.push({
                arquivo: arquivo,
                data: info.data || "",
                titulo: info.titulo,
                descricao: info.descricao,
                permalink: info.permalink
            });
        }
    }
    
    // Ordenar posts pela data (assumindo formato YYYY-MM-DD)
    posts.sort((a, b) => {
        if (!a.data) return 1;
        if (!b.data) return -1;
        return b.data.localeCompare(a.data);
    });
    
    // Seção do post mais recente
    if (posts.length > 0) {
        const recente = posts[0];
        
        saida += `# Mais recente\n\n`;
        // Garantir que o permalink tenha o domínio completo
        const permalinkRecente = recente.permalink.startsWith('http') ? recente.permalink : `https://marcosramon.net/${recente.permalink}`;
        
        saida += `**${recente.titulo} - ${formatarData(recente.data)}**\n\n`;
        saida += `${recente.descricao} [[Blog/${recente.arquivo.basename}|Continue lendo →]]\n\n`;
        saida += `---\n\n`;
        
        // Lista de posts recentes
        saida += `# Últimos posts\n\n`;
        
        // Limitar a 15 posts
        const postsRecentes = posts.slice(0, numeroDePostsRecentes);
        
        for (const post of postsRecentes) {
            // Remover a data formatada e adicionar o "·" antes do título
            saida += `· [[Blog/${post.arquivo.basename}|${post.titulo}]]\n`;
        }
        
        // Links adicionais
        saida += `\n---\n\n`;
        saida += `[[Sobre]] · [Newsletter](https://marcosramon.substack.com/)`;
    } else {
        saida += "# Bem-vindo\n\nNão há posts disponíveis na pasta Blog.";
    }
    
    return saida;
}

// Gerar o template e retornar
tR = await gerarTemplate();
%>