## Textos mais recentes
<%*
// Pasta onde estão os posts do blog
const blogFolder = "Blog";
const files = app.vault.getMarkdownFiles()
  .filter(file => file.path.startsWith(blogFolder));

// Função para obter a data do frontmatter ou da criação do arquivo
async function getCustomDate(file) {
  const content = await app.vault.read(file);
  const dateMatch = content.match(/date:\s*(\d{4}-\d{2}-\d{2})/);
  return dateMatch ? dateMatch[1] : new Date(file.stat.ctime).toISOString().slice(0, 10);
}

// Formata a data para o padrão brasileiro (DD/MM/AAAA)
function formatDate(dateStr) {
  const [year, month, day] = dateStr.split('-');
  return `${day}/${month}/${year}`;
}

// Obtém os arquivos com suas datas
let postsWithDates = [];
for (const file of files) {
  const date = await getCustomDate(file);
  postsWithDates.push({ file, date });
}

// Ordena do mais recente para o mais antigo e limita a 7 posts
postsWithDates.sort((a, b) => b.date.localeCompare(a.date));
const recentPosts = postsWithDates.slice(0, 7);

// Gera a tabela
let table = "| Data | Título |\n| ---- | ------ |\n";
for (const post of recentPosts) {
  table += `| ${formatDate(post.date)} | [[${post.file.basename}]] |\n`;
}

tR += table;
%>