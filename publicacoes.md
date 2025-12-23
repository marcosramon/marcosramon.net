---
layout: Post
title: "Publicações"
permalink: /publicacoes/
date: 2025-12-23
author: Marcos Ramon
content-type: post
---

<style>
  /* Fonte do sistema */
  .publications-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 100%;
  }

  /* Cabeçalho do Ano */
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
  
  /* Item da publicação */
  .pub-item {
    margin-bottom: 35px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .pub-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: #000;
    margin-bottom: 4px;
    line-height: 1.4;
  }

  .pub-authors {
    font-size: 0.95rem;
    color: #555;
    font-style: italic;
    margin-bottom: 4px;
  }

  .pub-venue {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 8px;
  }

  /* ISBN e Informações Extras */
  .pub-isbn {
    font-size: 0.85rem;
    color: #777;
    margin-left: 10px;
    font-weight: normal;
  }

  /* Botões (Agora usando a cor do link do tema) */
  .pub-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 5px;
    align-items: center;
  }

  .pub-btn {
    display: inline-block;
    padding: 3px 10px;
    border: 1px solid currentColor; /* Pega a cor do texto (azul do tema) */
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    text-decoration: none !important;
    background-color: transparent;
    opacity: 0.9;
    transition: all 0.2s ease;
  }

  .pub-btn:hover {
    background-color: rgba(0,0,0,0.05); /* Fundo sutil ao passar o mouse */
    opacity: 1;
    transform: translateY(-1px);
  }

  /* Área "Como Citar" (Collapsible) */
  details.pub-citation {
    margin-top: 10px;
    width: 100%;
  }

  summary.citation-trigger {
    cursor: pointer;
    font-size: 0.8rem;
    color: #888;
    list-style: none; /* Remove a seta padrão em alguns browsers */
    font-weight: 500;
  }
  
  summary.citation-trigger:hover {
    color: #555;
    text-decoration: underline;
  }

  .citation-content {
    margin-top: 8px;
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #eee;
    border-radius: 4px;
    font-size: 0.85rem;
    font-family: monospace; /* Fonte de código para copiar fácil */
    color: #555;
    white-space: pre-wrap; /* Mantém quebras de linha se houver */
  }

  /* Modo Escuro */
  @media (prefers-color-scheme: dark) {
    .pub-year-heading { color: #eee; border-color: #444; }
    .pub-title { color: #f0f0f0; }
    .pub-authors { color: #bbb; }
    .pub-venue, .pub-isbn { color: #999; }
    .citation-content { background-color: #222; border-color: #444; color: #ccc; }
    .pub-btn:hover { background-color: rgba(255,255,255,0.1); }
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
          
          <div class="pub-venue">
            {{ pub.venue }}
            {% if pub.isbn %}
              <span class="pub-isbn">ISBN: {{ pub.isbn }}</span>
            {% endif %}
          </div>
          
          {% if pub.links %}
          <div class="pub-buttons">
            {% for link in pub.links %}
              <a href="{{ link.url }}" class="pub-btn" target="_blank">{{ link.label }}</a>
            {% endfor %}
          </div>
          {% endif %}

          {% if pub.citation %}
          <details class="pub-citation">
            <summary class="citation-trigger">▼ Como citar</summary>
            <div class="citation-content">{{ pub.citation }}</div>
          </details>
          {% endif %}

        </div>
      {% endfor %}
    </div>
  {% endfor %}

</div>
