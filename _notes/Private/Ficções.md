---
layout: Post
title: Ficções
feed: hide
date: 2026-02-21
permalink: /ficcoes
image: ficcoes-sp.png
author: Marcos Ramon
---

<style>
  /* --- Layout da Página do Podcast --- */
  .podcast-container {
    font-family: inherit;
    max-width: 100%;
  }

  /* Imagem Banner */
  .podcast-banner {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }

  /* Descrição */
  .podcast-description {
    font-size: 1.1rem;
    line-height: 1.6;
    color: var(--color-text-main);
    margin-bottom: 2rem;
  }

  /* Grade de Botões de Plataformas */
  .listen-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 15px;
    margin-bottom: 40px;
  }

  .listen-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 12px 15px;
    border: 1px solid var(--color-border);
    border-radius: 8px;
    color: var(--color-text-main) !important;
    text-decoration: none !important;
    font-size: 0.9rem;
    font-weight: 600;
    transition: all 0.2s ease;
    background: var(--color-bg-sub);
  }

  .listen-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .listen-btn i {
    font-size: 1.2rem;
  }

  /* Player Wrapper */
  .player-wrapper {
    margin-top: 20px;
    margin-bottom: 40px;
    background: transparent;
  }

  .section-title {
    font-size: 0.9rem;
    text-transform: uppercase;
    color: var(--color-text-sub);
    letter-spacing: 1px;
    margin-bottom: 15px;
    font-weight: 700;
    border-bottom: 1px solid var(--color-border-light);
    padding-bottom: 5px;
  }

  /* Ajuste para o texto com links internos */
  .podcast-description a {
    color: var(--color-text-link);
    text-decoration: none;
    font-weight: 600;
  }
  .podcast-description a:hover {
    text-decoration: underline;
  }

  /* Lista de episódios em destaque */
  .ep-list {
    list-style: none;
    padding: 0;
    margin: 0 0 40px 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .ep-list li {
    padding: 14px 16px;
    border: 1px solid var(--color-border);
    border-radius: 8px;
    background: var(--color-bg-sub);
    line-height: 1.5;
    transition: border-color 0.2s ease;
  }

  .ep-list li:hover {
    border-color: var(--color-text-link);
  }

  .ep-list li a {
    font-weight: 600;
    color: var(--color-text-link);
    text-decoration: none;
  }

  .ep-list li a:hover {
    text-decoration: underline;
  }

  .ep-list li span {
    display: block;
    font-size: 0.88rem;
    color: var(--color-text-sub);
    margin-top: 3px;
  }
</style>

<div class="podcast-container">

  <img src="/assets/img/ficcoes wide.png" alt="Ficções Podcast Banner" class="podcast-banner">

  <div class="podcast-description">
    <p>
      <strong>Ficções</strong> é um podcast sobre filosofia, cotidiano, literatura, arte e tecnologia. Mais de 500 episódios falando de conceitos e ideias que nos ajudam a entender o mundo.
    </p>
    <p>
      Um projeto independente e sem fins comerciais, produzido por <a href="{{ '/sobre' | relative_url }}">Marcos Ramon</a>, professor de <a href="{{ '/notes' | relative_url }}">Filosofia</a> e escritor.
    </p>
  </div>

  <div class="listen-section">
    <div class="section-title">Onde ouvir</div>
    
    <div class="listen-grid">
      <a href="https://open.spotify.com/show/1smphr2Sl3kHncMYB984rc?si=545bce8419e14da7" target="_blank" class="listen-btn">
        <i class="fa-brands fa-spotify"></i> Spotify
      </a>

      <a href="https://podcasts.apple.com/br/podcast/fic%C3%A7%C3%B5es/id967600465" target="_blank" class="listen-btn">
        <i class="fa-brands fa-apple"></i> Apple
      </a>

      <a href="https://castbox.fm/channel/Fic%C3%A7%C3%B5es-id1399868?country=br" target="_blank" class="listen-btn">
        <i class="fa-solid fa-podcast"></i> CastBox
      </a>

      <a href="http://pca.st/4m8G" target="_blank" class="listen-btn">
        <i class="fa-solid fa-headphones"></i> Pocket Casts
      </a>

      <a href="https://tunein.com/podcasts/Culture/Fices-p610099/" target="_blank" class="listen-btn">
        <i class="fa-solid fa-radio"></i> TuneIn
      </a>

      <a href="https://anchor.fm/s/a9c85b0/podcast/rss" target="_blank" class="listen-btn">
        <i class="fa-solid fa-rss"></i> RSS Feed
      </a>
    </div>
  </div>

  <div class="player-wrapper">
    <div class="section-title">Últimos Episódios</div>
    <iframe style="border-radius:12px"
      src="https://open.spotify.com/embed/show/1smphr2Sl3kHncMYB984rc?utm_source=generator"
      width="100%" height="352" frameBorder="0" allowfullscreen=""
      allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      loading="lazy">
    </iframe>
  </div>

  <div class="highlights-section">
    <div class="section-title">Por onde começar</div>
    <ul class="ep-list">
      <li>
        <a href="https://open.spotify.com/episode/6VchJVQjl5FX8EMwNynCQ7?si=e730604dfbba4cbb" target="_blank">Fazer 60 pinturas por dia</a>
        <span>Sobre não se martirizar buscando a perfeição.</span>
      </li>
      <li>
        <a href="https://open.spotify.com/episode/0mL6Ne71hj2pa6qKMJoWt5?si=c9abb6590015411e" target="_blank">Sobre escolher o que falar</a>
        <span>Encontrei uma citação em um livro de cartas do Deleuze.</span>
      </li>
      <li>
        <a href="https://open.spotify.com/episode/4aVprnSJ0uy3UhztFUPkcb?si=e767e9cdcbe34082" target="_blank">Amor</a>
        <span>Neste episódio aponto as reflexões que foram desenvolvidas por Platão, Espinosa, Nietzsche, Schopenhauer e Roland Barthes sobre o amor e seus desdobramentos.</span>
      </li>
      <li>
        <a href="https://open.spotify.com/episode/6P3sqd96C5tlz1X0cCkyzs?si=58544e92628e4539" target="_blank">Crítica interna e viés de confirmação</a>
        <span>Sobre "A revolução dos bichos", extremistas de direita assistindo a um vídeo sobre Platão e alguém dizendo que Roger Waters não entende a letra de "The Wall". </span>
      </li>
      <li>
        <a href="https://open.spotify.com/episode/2LyUujDku43EpSnxwkAbWv?si=ba04f12a07224605" target="_blank">Podcasts à moda antiga</a>
        <span>Na semana passada gravei um episódio falando que o podcast, do jeito como se produzia antes, mas reflexivo e menos comercial, continua existindo. </span>
      </li>
    </ul>
  </div>

</div>
