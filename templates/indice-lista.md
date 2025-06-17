<%*
// Busca todos os arquivos na pasta blog
const blogFolder = "Blog";
const files = app.vault.getMarkdownFiles()
  .filter(file => file.path.startsWith(blogFolder));

// Função para obter a data personalizada de um arquivo
async function getCustomDate(file) {
  const content = await app.vault.read(file);
  // Busca a propriedade 'date:' no frontmatter
  const dateMatch = content.match(/date:\s*(\d{4}-\d{2}-\d{2})/);
  if (dateMatch && dateMatch[1]) {
    return dateMatch[1];
  }
  // Retorna a data de criação do arquivo se não encontrar a data personalizada
  return new Date(file.stat.ctime).toISOString().slice(0, 10);
}

// Formata a data para formato brasileiro
function formatDate(dateStr) {
  const parts = dateStr.split('-');
  return `${parts[2]}/${parts[1]}/${parts[0]}`;
}

// Organiza os arquivos por data
let postsWithDates = [];
for (const file of files) {
  const date = await getCustomDate(file);
  postsWithDates.push({
    file: file,
    date: date
  });
}

// Ordena do mais recente para o mais antigo
postsWithDates.sort((a, b) => b.date.localeCompare(a.date));

// Gera a tabela
let table = "| Data | Título |\n| ---- | ------ |\n";
for (const post of postsWithDates) {
  const formattedDate = formatDate(post.date);
  const fileName = post.file.basename;
  table += `| ${formattedDate} | [[${fileName}]] |\n`;
}

tR += table;
%>