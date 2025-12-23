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
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 100%;
  }

  /* --- Estilos Padrão (Modo Claro) --- */
  /* Força cores base para garantir contraste */
  :root {
    --pub-heading-color: #333;
    --pub-title-color: #111;
    --pub-text-color: #444;
    --pub-meta-color: #666;
    --pub-border-color: #e0e0e0;
    --pub-btn-hover-bg: rgba(0,0,0,0.05);
    --pub-citation-bg: #f9f9f9;
    --pub-citation-border: #eee;
  }

  /* --- Cabeçalho do Ano --- */
  .pub-year-heading {
    margin-top: 40px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--pub-border-color);
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--pub-heading-color);
    opacity: 1; /* Removi opacidade para melhorar leitura */
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
    color: var(--pub-title-color);
    margin-bottom: 4px;
    line-height: 1.4;
  }

  .pub-authors {
    font-size: 0.95rem;
    color: var(--pub-text-color);
    font-style: italic;
    margin-bottom: 4px;
  }

  .pub-venue {
    font-size: 0.9rem;
    color: var(--pub-meta-color);
    margin-bottom: 8px;
  }

  .pub-isbn {
    font-size: 0.85rem;
    color: var(--pub-meta-color);
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
    border: 1px solid currentColor;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    text-decoration: none !important;
    background-color: transparent;
    /* A cor é herdada do link do tema, não definimos fixo aqui */
    opacity: 0.9;
    transition: all 0.2s ease;
  }

  .pub-btn:hover {
    background-color: var(--pub-btn-hover-bg);
    opacity: 1;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  /* --- Citação --- */
  details.pub-citation {
    margin-top: 10px;
    width: 100%;
  }

  summary.citation-trigger {
    cursor: pointer;
    font-size: 0.8rem;
    color: var(--pub-meta-color);
    font-weight: 500;
    list-style: none;
  }
  
  summary.citation-trigger:hover {
    color: var(--pub-text-color);
    text-decoration: underline;
  }

  .citation-content {
    margin-top: 8px;
    padding: 10px;
    background-color: var(--pub-citation-bg);
    border: 1px solid var(--pub-citation-border);
    border-radius: 4px;
    font-size: 0.85rem;
    font-family: monospace;
    color: var(--pub-text-color);
    white-space: pre-wrap;
  }

  /* --- MODO ESCURO (Dark Mode) --- */
  /* Detecta preferência do sistema ou classe do tema */
  @media (prefers-color-scheme: dark) {
    :root {
      --pub-heading-color: #f0f0f0;
      --pub-title-color: #ffffff;
      --pub-text-color: #cccccc;
      --pub-meta-color: #aaaaaa;
      --pub-border-color: #444444;
      --pub-btn-hover-bg: rgba(255,255,255,0.1);
      --pub-citation-bg: #2a2a2a;
      --pub-citation-border: #444;
    }
  }

  /* Suporte extra caso seu site use uma classe .dark-mode no body via JS */
  body.dark-mode, body[data-theme="dark"] {
      --pub-heading-color: #f0f0f0;
      --pub-title-color: #ffffff;
      --pub-text-color: #cccccc;
      --pub-meta-color: #aaaaaa;
      --pub-border-color: #444444;
      --pub-btn-hover-bg: rgba(255,255,255,0.1);
      --pub-citation-bg: #2a2a2a;
      --pub-citation-border: #444;
  }
  
  /* Força a aplicação das variáveis nos elementos */
  .pub-year-heading { color: var(--pub-heading-color); border-color: var(--pub-border-color); }
  .pub-title { color: var(--pub-title-color); }
  .pub-authors { color: var(--pub-text-color); }
  .pub-venue { color: var(--pub-meta-color); }
  .pub-isbn { color: var(--pub-meta-color); }
  .citation-content { background-color: var(--pub-citation-bg); border-color: var(--pub-citation-border); color: var(--pub-text-color); }
  summary.citation-trigger { color: var(--pub-meta-color); }
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
