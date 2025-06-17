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
    date: date,
    year: date.split('-')[0] // Extrai o ano da data
  });
}

// Ordena do mais recente para o mais antigo
postsWithDates.sort((a, b) => b.date.localeCompare(a.date));

// Agrupa os posts por ano
const postsByYear = {};
for (const post of postsWithDates) {
  if (!postsByYear[post.year]) {
    postsByYear[post.year] = [];
  }
  postsByYear[post.year].push(post);
}

// Obtém os anos em ordem decrescente
const years = Object.keys(postsByYear).sort((a, b) => b.localeCompare(a));

// Gera o conteúdo agrupado por ano
let content = "";
for (const year of years) {
  content += `## ${year}\n\n`;
  content += "| Data | Título |\n| ---- | ------ |\n";
  
  for (const post of postsByYear[year]) {
    const formattedDate = formatDate(post.date);
    const fileName = post.file.basename;
    content += `| ${formattedDate} | [[${fileName}]] |\n`;
  }
  
  content += "\n"; // Adiciona uma linha em branco entre os anos
}

tR += content;
%>