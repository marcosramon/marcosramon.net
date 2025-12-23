---
layout: Post
title: "Publicações"
permalink: /publicacoes/
date: 2025-12-23
author: Marcos Ramon
content-type: post
---

<style>
  /* --- Configurações Base --- */
  .publications-wrapper {
    /* Herda a fonte do corpo do site para consistência total */
    font-family: inherit;
    max-width: 100%;
  }

  /* --- Cabeçalho do Ano --- */
  .pub-year-heading {
    margin-top: 40px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    /* Usa a cor de borda e texto padrão do tema */
    border-bottom: 1px solid var(--color-border-light);
    color: var(--color-text-main);
    font-size: 1.5rem;
    font-weight: 600;
  }
  
  /* --- Item da Publicação --- */
  .pub-item {
    margin-bottom: 35px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .pub-title {
    font-weight: 700;
    font-size: 1.1rem;
    /* Cor principal do texto */
    color: var(--color-text-main);
    margin-bottom: 4px;
    line-height: 1.4;
  }

  .pub-authors {
    font-size: 0.95rem;
    /* Cor secundária do texto (cinza mais suave) */
    color: var(--color-text-sub);
    font-style: italic;
    margin-bottom: 4px;
  }

  .pub-venue {
    font-size: 0.9rem;
    color: var(--color-text-sub);
    margin-bottom: 8px;
  }

  .pub-isbn {
    font-size: 0.85rem;
    color: var(--color-text-sub);
    margin-left: 10px;
    font-weight: normal;
  }

  /* --- Botões --- */
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
    /* Usa a cor de link configurada no tema (azul) */
    border: 1px solid var(--color-text-link);
    color: var(--color-text-link) !important;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    text-decoration: none !important;
    background-color: transparent;
    transition: all 0.2s ease;
  }

  .pub-btn:hover {
    /* Usa a cor de fundo secundária no hover */
    background-color: var(--color-bg-sub);
    color: var(--color-text-link) !important;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  /* --- Citação (Caixa "Como Citar") --- */
  details.pub-citation {
    margin-top: 10px;
    width: 100%;
  }

  summary.citation-trigger {
    cursor: pointer;
    font-size: 0.8rem;
    color: var(--color-text-sub);
    font-weight: 500;
    list-style: none;
  }
  
  summary.citation-trigger:hover {
    color: var(--color-text-main);
    text-decoration: underline;
  }

  .citation-content {
    margin-top: 8px;
    padding: 10px;
    /* Fundo e bordas usando as variáveis do tema */
    background-color: var(--color-bg-sub);
    border: 1px solid var(--color-border-light);
    color: var(--color-text-main);
    border-radius: 4px;
    font-size: 0.85rem;
    font-family: monospace;
    white-space: pre-wrap;
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
