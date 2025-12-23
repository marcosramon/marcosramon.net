---
layout: Post
title: Publicações
permalink: /publicacoes/
---

<style>
  /* Garante que a fonte seja a do sistema (sem serifa) */
  .publications-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 100%;
  }

  /* Estilo do Ano */
  .pub-year-heading {
    margin-top: 40px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
    font-size: 1.5rem;
    font-weight: 600;
    color: #333;
    opacity: 0.9;
  }
  
  /* Container de cada publicação */
  .pub-item {
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  /* Título do artigo */
  .pub-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: #000;
    margin-bottom: 4px;
    line-height: 1.4;
  }

  /* Autores */
  .pub-authors {
    font-size: 0.95rem;
    color: #555;
    font-style: italic;
    margin-bottom: 4px;
  }

  /* Revista/Conferência */
  .pub-venue {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 10px;
  }

  /* Botões (Links) */
  .pub-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }

  .pub-btn {
    display: inline-block;
    padding: 4px 12px;
    border: 1px solid #333;
    border-radius: 4px; /* Cantos arredondados */
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    text-decoration: none !important; /* Remove sublinhado padrão */
    color: #333 !important;
    background-color: transparent;
    transition: all 0.2s ease;
  }

  /* Efeito Hover (passar o mouse) */
  .pub-btn:hover {
    background-color: #333;
    color: #fff !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    transform: translateY(-1px);
  }

  /* Ajustes para Modo Escuro (Dark Mode) */
  @media (prefers-color-scheme: dark) {
    .pub-year-heading { color: #eee; border-color: #444; }
    .pub-title { color: #f0f0f0; }
    .pub-authors { color: #bbb; }
    .pub-venue { color: #999; }
    .pub-btn { border-color: #eee; color: #eee !important; }
    .pub-btn:hover { background-color: #eee; color: #111 !important; }
  }
</style>

<div class="publications-wrapper">

  {% assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

  {% for year_group in publications_by_year %}
    <h3 class="pub-year-heading">{{ year_group.name }}</h3>
    
    <div class="pub-list">
      {% for pub in year_group.items %}
        <div class="pub-item">
          <div class="pub-title">{{ pub.title }}</div>
          
          <div class="pub-authors">{{ pub.authors }}</div>
          
          <div class="pub-venue">{{ pub.venue }}</div>
          
          {% if pub.links %}
          <div class="pub-buttons">
            {% for link in pub.links %}
              <a href="{{ link.url }}" class="pub-btn" target="_blank">{{ link.label }}</a>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  {% endfor %}

</div>
