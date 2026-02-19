---
layout: Post
title: Publicações
permalink: /publicacoes/
date: 2025-01-01
content-type: post
---

<style>
  /* --- Base --- */
  .publications-wrapper {
    font-family: inherit;
    max-width: 100%;
  }

  /* --- Intro & Profiles --- */
  .pub-intro {
    margin-bottom: 32px;
    font-size: 1rem;
    line-height: 1.7;
    color: var(--color-text-main);
  }

  .academic-profiles {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 16px;
    margin-bottom: 36px;
    padding-bottom: 36px;
    border-bottom: 1px solid var(--color-border-light);
  }

  .profile-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border: 1px solid var(--color-border);
    border-radius: 5px;
    text-decoration: none !important;
    color: var(--color-text-main) !important;
    font-size: 0.875rem;
    font-weight: 600;
    background: var(--color-bg-sub);
    transition: border-color 0.15s ease, color 0.15s ease;
  }

  .profile-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
  }

  .profile-btn i {
    font-size: 1rem;
    color: var(--color-text-link);
  }

  /* --- Stats Bar --- */
  .pub-stats {
    display: flex;
    gap: 24px;
    margin-bottom: 28px;
    flex-wrap: wrap;
  }

  .pub-stat {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .pub-stat-number {
    font-size: 1.6rem;
    font-weight: 700;
    line-height: 1;
    color: var(--color-text-main);
    font-variant-numeric: tabular-nums;
  }

  .pub-stat-label {
    font-size: 0.75rem;
    color: var(--color-text-sub);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 3px;
  }

  /* --- Filters --- */
  .pub-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 36px;
    padding-bottom: 28px;
    border-bottom: 1px solid var(--color-border-light);
  }

  .pub-filter-btn {
    padding: 5px 12px;
    border: 1px solid var(--color-border);
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    background: transparent;
    color: var(--color-text-sub);
    transition: all 0.15s ease;
    letter-spacing: 0.2px;
  }

  .pub-filter-btn:hover,
  .pub-filter-btn.active {
    border-color: var(--color-text-link);
    color: var(--color-text-link);
    background: transparent;
  }

  /* --- Year Heading --- */
  .pub-year-heading {
    margin-top: 36px;
    margin-bottom: 20px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--color-border-light);
    color: var(--color-text-main);
    font-size: 1.3rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }

  /* --- Publication Item --- */
  .pub-item {
    margin-bottom: 32px;
    padding-bottom: 32px;
    border-bottom: 1px solid var(--color-border-light);
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0 16px;
    align-items: start;
  }

  .pub-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }

  /* Left accent line colored by type */
  .pub-accent {
    width: 3px;
    height: 100%;
    min-height: 60px;
    border-radius: 2px;
    background: var(--color-border);
    flex-shrink: 0;
  }

  .pub-item[data-type="artigo"] .pub-accent   { background: #4a90d9; }
  .pub-item[data-type="capitulo"] .pub-accent { background: #7b68ee; }
  .pub-item[data-type="anais"] .pub-accent    { background: #50b89b; }

  .pub-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    min-width: 0;
  }

  /* --- Type Badge --- */
  .pub-type-badge {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    font-weight: 700;
    margin-bottom: 5px;
    display: inline-block;
  }

  .pub-item[data-type="artigo"]   .pub-type-badge { color: #4a90d9; }
  .pub-item[data-type="capitulo"] .pub-type-badge { color: #7b68ee; }
  .pub-item[data-type="anais"]    .pub-type-badge { color: #50b89b; }

  .pub-title {
    font-weight: 700;
    font-size: 1rem;
    color: var(--color-text-main);
    margin-bottom: 5px;
    line-height: 1.45;
  }

  .pub-authors {
    font-size: 0.875rem;
    color: var(--color-text-sub);
    font-style: italic;
    margin-bottom: 3px;
  }

  .pub-venue {
    font-size: 0.85rem;
    color: var(--color-text-sub);
    margin-bottom: 10px;
  }

  .pub-isbn {
    font-size: 0.8rem;
    color: var(--color-text-sub);
    margin-left: 8px;
    font-weight: normal;
  }

  /* --- Buttons --- */
  .pub-buttons {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 4px;
    align-items: center;
  }

  .pub-btn {
    display: inline-block;
    padding: 3px 10px;
    border: 1px solid var(--color-border);
    color: var(--color-text-sub) !important;
    border-radius: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    text-decoration: none !important;
    background-color: transparent;
    letter-spacing: 0.4px;
    transition: all 0.15s ease;
  }

  .pub-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
  }

  /* --- Citation --- */
  details.pub-citation {
    margin-top: 10px;
    width: 100%;
  }

  summary.citation-trigger {
    cursor: pointer;
    font-size: 0.75rem;
    color: var(--color-text-sub);
    font-weight: 600;
    list-style: none;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    user-select: none;
  }

  summary.citation-trigger:hover { color: var(--color-text-main); }
  summary.citation-trigger::-webkit-details-marker { display: none; }

  .citation-arrow {
    display: inline-block;
    transition: transform 0.15s ease;
    font-style: normal;
  }

  details[open] .citation-arrow {
    transform: rotate(90deg);
  }

  .citation-content {
    margin-top: 8px;
    padding: 10px 12px;
    background-color: var(--color-bg-sub);
    border-left: 2px solid var(--color-border);
    color: var(--color-text-sub);
    border-radius: 0 4px 4px 0;
    font-size: 0.82rem;
    font-family: monospace;
    white-space: pre-wrap;
    line-height: 1.5;
  }

  /* --- Hidden items (filtered out) --- */
  .pub-year-group.hidden { display: none; }
  .pub-item.hidden { display: none; }

  @media (max-width: 600px) {
    .academic-profiles { flex-direction: column; }
    .profile-btn { width: 100%; justify-content: center; }
    .pub-stats { gap: 16px; }
    .pub-item { grid-template-columns: 3px 1fr; gap: 0 12px; }
  }
</style>

<div class="publications-wrapper">

  <div class="pub-intro">
    <p>
      Esta página reúne parte da minha produção acadêmica, incluindo artigos em periódicos, capítulos de livros e trabalhos apresentados em eventos. Minhas áreas de interesse são Estética, Cibercultura e Educação Profissional.
    </p>
    <p>
      Para a lista completa e atualizada, incluindo orientações e projetos, acesse meu currículo na plataforma Lattes.
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

  <!-- Stats computed by Liquid -->
  {% assign total = site.data.publications | size %}
  {% assign artigos = site.data.publications | where: "type", "Artigo em Periódico" | size %}
  {% assign capitulos = site.data.publications | where: "type", "Capítulo de Livro" | size %}
  {% assign anais = site.data.publications | where: "type", "Anais de Evento" | size %}

  <div class="pub-stats">
    <div class="pub-stat">
      <span class="pub-stat-number">{{ total }}</span>
      <span class="pub-stat-label">Publicações</span>
    </div>
    <div class="pub-stat">
      <span class="pub-stat-number">{{ artigos }}</span>
      <span class="pub-stat-label">Artigos</span>
    </div>
    <div class="pub-stat">
      <span class="pub-stat-number">{{ capitulos }}</span>
      <span class="pub-stat-label">Capítulos</span>
    </div>
    <div class="pub-stat">
      <span class="pub-stat-number">{{ anais }}</span>
      <span class="pub-stat-label">Anais</span>
    </div>
  </div>

  <!-- Filters -->
  <div class="pub-filters">
    <button class="pub-filter-btn active" data-filter="all">Todos</button>
    <button class="pub-filter-btn" data-filter="artigo">Artigos em Periódico</button>
    <button class="pub-filter-btn" data-filter="capitulo">Capítulos de Livro</button>
    <button class="pub-filter-btn" data-filter="anais">Anais de Evento</button>
  </div>

  {% assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

  {% for year_group in publications_by_year %}
    <div class="pub-year-group" id="year-{{ year_group.name }}">
      <h3 class="pub-year-heading">{{ year_group.name }}</h3>
      <div class="pub-list">
        {% for pub in year_group.items %}
          {% assign type_key = "outro" %}
          {% if pub.type == "Artigo em Periódico" %}{% assign type_key = "artigo" %}
          {% elsif pub.type == "Capítulo de Livro" %}{% assign type_key = "capitulo" %}
          {% elsif pub.type == "Anais de Evento" %}{% assign type_key = "anais" %}
          {% endif %}

          <div class="pub-item" data-type="{{ type_key }}">
            <div class="pub-accent"></div>
            <div class="pub-content">

              {% if pub.type %}
                <span class="pub-type-badge">{{ pub.type }}</span>
              {% endif %}

              <div class="pub-title">{{ pub.title }}</div>
              <div class="pub-authors">{{ pub.authors }}</div>
              <div class="pub-venue">
                {{ pub.venue }}
                {% if pub.isbn %}<span class="pub-isbn">ISBN: {{ pub.isbn }}</span>{% endif %}
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
                <summary class="citation-trigger">
                  <i class="citation-arrow">›</i> Como citar
                </summary>
                <div class="citation-content">{{ pub.citation }}</div>
              </details>
              {% endif %}

            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}

</div>

<script>
(function() {
  const buttons = document.querySelectorAll('.pub-filter-btn');
  const items   = document.querySelectorAll('.pub-item');
  const groups  = document.querySelectorAll('.pub-year-group');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;

      items.forEach(item => {
        if (filter === 'all' || item.dataset.type === filter) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });

      // Hide year headings that have no visible items
      groups.forEach(group => {
        const visibleItems = group.querySelectorAll('.pub-item:not(.hidden)');
        group.classList.toggle('hidden', visibleItems.length === 0);
      });
    });
  });
})();
</script>
