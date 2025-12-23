---
layout: Post
title: Publicações
permalink: /pesquisa/
---

<style>
  .pub-year-heading {
    margin-top: 40px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #eee;
    font-size: 1.5rem;
    color: #333;
  }
  
  .pub-item {
    margin-bottom: 25px;
    display: flex;
    flex-direction: column;
  }

  .pub-title {
    font-weight: bold;
    font-size: 1.1rem;
    color: #000;
  }

  .pub-authors {
    font-style: italic;
    color: #666;
    margin: 5px 0;
  }

  .pub-venue {
    color: #444;
    font-size: 0.95rem;
  }

  .pub-buttons {
    margin-top: 8px;
    display: flex;
    gap: 8px;
  }

  .pub-btn {
    display: inline-block;
    padding: 2px 10px;
    border: 1px solid #333;
    border-radius: 4px;
    font-size: 0.8rem;
    text-transform: uppercase;
    text-decoration: none !important;
    color: #333 !important;
    transition: all 0.2s;
  }

  .pub-btn:hover {
    background-color: #333;
    color: #fff !important;
    text-decoration: none;
  }

  /* Ajuste para modo escuro (se o tema suportar) */
  @media (prefers-color-scheme: dark) {
    .pub-year-heading { color: #ddd; border-color: #444; }
    .pub-title { color: #fff; }
    .pub-authors { color: #aaa; }
    .pub-venue { color: #ccc; }
    .pub-btn { border-color: #fff; color: #fff !important; }
    .pub-btn:hover { background-color: #fff; color: #000 !important; }
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
