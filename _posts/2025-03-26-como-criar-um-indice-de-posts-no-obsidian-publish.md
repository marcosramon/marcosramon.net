---
title: Como criar um índice de posts no Obsidian Publish
date: 2025-03-26
tags:
  - obsidian
  - tecnologia
  - Escrever
  - Publicar
  - internet
description: Um guia simples para criar índices de posts no Obsidian Publish
permalink: como-criar-um-indice-de-posts-no-obsidian-publish
author: Marcos Ramon
---
O [Obsidian Publish](https://obsidian.md/publish) é um serviço que permite que você transforme suas notas do Obsidian em um site. Pensei em usar o serviço como o meu blog permanente, mas encontrei algumas dificuldades, como, por exemplo, criar um índice com todos os textos do blog.

Apesar de ter conseguido uma alternativa, que mostro no vídeo logo abaixo, desisti da ideia de usar o Obsidian Publish.

De qualquer forma, deixo aqui o vídeo explicativo com a solução que encontrei, algumas telas dos índices que eu criei (um como todos os textos listados por ano e outro com os textos mais recentes) e os códigos que criei para fazer os índices. Esses códigos funcionam junto com o plugin [Templater](https://silentvoid13.github.io/Templater/introduction.html). Espero que seja útil. 😉

<iframe width="560" height="315" src="https://www.youtube.com/embed/LlePHlwxVu8?si=iI2V4h29o-nwXiYb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### **Código para textos mais recentes**

<img src="/assets/img/obsidian-mais-recentes.png">
<small>Print da tela inicial com textos mais recentes</small>

Para criar essa página logo acima, eu criei o código abaixo:

```
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
```

### **Código para índice completo, por ano**

<img src="/assets/img/obsidian-indice.png">
<small>Página com índice completo, com posts divididos por ano</small>

Para gerar o índice da imagem acima, utilizei este código:

```
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
```
Espero que seja útil. 😊

<div class="leia-tambem" markdown="1">
## Leia também:

- <a href="/sobre-escrever-e-fazer-podcasts">Sobre escrever e fazer podcasts</a> 
- <a href="/o-tempo-da-escrita">O tempo da escrita</a>
- <a href="/a-internet-e-o-olhar-dos-outros">A internet e o olhar dos outros</a>
</div>

