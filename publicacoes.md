---
layout: Post
title: Publicações
permalink: /publicacoes/
date: 2025-01-01
content-type: post
---

<style>
  /* --- Configurações Base --- */
  .publications-wrapper {
    font-family: inherit;
    max-width: 100%;
  }

  /* --- Área de Introdução e Perfis --- */
  .pub-intro {
    margin-bottom: 40px;
    font-size: 1.1rem;
    line-height: 1.6;
    color: var(--color-text-main);
  }

  .academic-profiles {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid var(--color-border-light);
    padding-bottom: 40px;
  }

  .profile-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 18px;
    border: 1px solid var(--color-border);
    border-radius: 6px;
    text-decoration: none !important;
    color: var(--color-text-main) !important;
    font-size: 0.95rem;
    font-weight: 600;
    background: var(--color-bg-sub);
    transition: all 0.2s ease;
  }

  .profile-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .profile-btn i {
    font-size: 1.1rem;
    color: var(--color-text-link);
  }

  /* --- Cabeçalho do Ano --- */
  .pub-year-heading {
    margin-top: 40px;
    margin-bottom: 25px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--color-border-light);
    color: var(--color-text-main);
    font-size: 1.5rem;
    font-weight: 600;
  }
  
  /* --- Item da Publicação --- */
  .pub-item {
    margin-bottom: 40px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  /* --- ETIQUETA DE TIPO --- */
  .pub-type-badge {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 700;
    color: var(--color-text-link);
    margin-bottom: 5px;
    display: inline-block;
  }

  .pub-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--color-text-main);
    margin-bottom: 6px;
    line-height: 1.4;
  }

  .pub-authors {
    font-size: 0.95rem;
    color: var(--color-text-sub);
    font-style: italic;
    margin-bottom: 4px;
  }

  .pub-venue {
    font-size: 0.9rem;
    color: var(--color-text-sub);
    margin-bottom: 10px;
  }

  .pub-isbn {
    font-size: 0.85rem;
    color: var(--color-text-sub);
    margin-left: 10px;
    font-weight: normal;
  }

  /* --- Botões da Publicação (PDF/DOI) --- */
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
    background-color: var(--color-bg-sub);
    color: var(--color-text-link) !important;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  /* --- Citação (Caixa "Como Citar") --- */
  details.pub-citation {
    margin-top: 12px;
    width: 100%;
  }

  summary.citation-trigger {
    cursor: pointer;
    font-size: 0.8rem;
    color: var(--color-text-sub);
    font-weight: 600;
    list-style: none;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  
  summary.citation-trigger:hover { color: var(--color-text-main); }
  summary.citation-trigger::-webkit-details-marker { display: none; }

  .citation-content {
    margin-top: 10px;
    padding: 12px;
    background-color: var(--color-bg-sub);
    border: 1px solid var(--color-border-light);
    color: var(--color-text-main);
    border-radius: 6px;
    font-size: 0.85rem;
    font-family: monospace;
    white-space: pre-wrap;
    line-height: 1.4;
  }

  @media (max-width: 600px) {
    .academic-profiles {
      flex-direction: column;
    }
    .profile-btn {
      width: 100%;
      justify-content: center;
    }
  }
</style>

<div class="publications-wrapper">

  <div class="pub-intro">
    <p>
      Esta página reúne parte da minha produção acadêmica, incluindo artigos em periódicos, capítulos de livros e trabalhos apresentados em eventos. Minhas áreas de interesse são Estética, Cibercultura e Educação Profissional.
    </p>
    <p>
      Abaixo você encontra uma seleção dos trabalhos mais recentes. Para a lista completa e atualizada de produções, orientações e projetos, acesse meu currículo na plataforma Lattes.
    </p>
  </div>

  <div class="academic-profiles">
    <a href="http://lattes.cnpq.br/9538072103558772" target="_blank" class="profile-btn">
      <i class="fa-solid fa-graduation-cap"></i> Currículo Lattes
    </a>
    <a href="https://orcid.org/0000-0002-8720-8706" target="_blank" class="profile-btn">
      <i class="fa-brands fa-orcid"></i> ORCID
    </a>
    <a href="mailto:marcos.ferreira@ifb.edu.br" class="profile-btn">
      <i class="fa-solid fa-envelope"></i> E-mail Institucional
    </a>
  </div>

  {% assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

  {% for year_group in publications_by_year %}
    <h3 class="pub-year-heading">{{ year_group.name }}</h3>
    
    <div class="pub-list">
      {% for pub in year_group.items %}
        <div class="pub-item">
          
          {% if pub.type %}
            <span class="pub-type-badge">{{ pub.type }}</span>
          {% endif %}

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
