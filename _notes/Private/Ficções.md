---
layout: Post
title: Ficções
feed: hide
date: 2025-12-27
permalink: /ficcoes
image: /assets/img/ficcoes-sp.png
---

<style>
  /* --- Layout da Página do Podcast --- */
  .podcast-container {
    font-family: inherit;
    max-width: 100%;
  }

  /* Imagem Banner (Opcional, se quiser manter a wide no topo) */
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
</style>

<div class="podcast-container">

  <img src="/assets/img/ficcoes wide.png" alt="Ficções Podcast Banner" class="podcast-banner">

  <div class="podcast-description">
    <p>
      <strong>Ficções</strong> é um podcast que reúne narrativas filosóficas, ou seja, reflexões que abordam temas variados como filosofia, cotidiano, literatura, arte e tecnologia. Cada episódio explora algum conceito, ideia ou teoria filosófica.
    </p>
    <p>
      O podcast é um projeto independente e sem fins comerciais, produzido por <a href="{{ '/sobre' | relative_url }}">Marcos Ramon</a>, professor de <a href="{{ '/notes' | relative_url }}">Filosofia</a> e escritor.
    </p>
  </div>

  <div class="listen-section">
    <div class="section-title">Onde ouvir (+500 episódios)</div>
    
    <div class="listen-grid">
      <a href="https://open.spotify.com/show/..." target="_blank" class="listen-btn">
        <i class="fa-brands fa-spotify"></i> Spotify
      </a>
      
      <a href="https://podcasts.apple.com/br/podcast/fic%C3%A7%C3%B5es/id967600465" target="_blank" class="listen-btn">
        <i class="fa-brands fa-apple"></i> Apple
      </a>

      <a href="https://castbox.fm/channel/Fic%C3%A7%C3%B5es-id1399868?country=br" target="_blank" class="listen-btn">
        <i class="fa-solid fa-podcast"></i> CastBox
      </a>

      <a href="http://pca.st/4m8G" target="_blank" class="listen-btn">
        <i class="fa-solid fa-rss"></i> Pocket Casts
      </a>

      <a href="https://overcast.fm/itunes967600465/fic-es" target="_blank" class="listen-btn">
        <i class="fa-solid fa-headphones"></i> Overcast
      </a>

      <a href="https://tunein.com/podcasts/Culture/Fices-p610099/" target="_blank" class="listen-btn">
        <i class="fa-solid fa-radio"></i> TuneIn
      </a>
    </div>
  </div>

  <div class="player-wrapper">
    <div class="section-title">Últimos Episódios</div>
    <iframe src="https://embed.podcasts.apple.com/us/podcast/fic%C3%A7%C3%B5es/id967600465?itsct=podcast_box&itscg=30200" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation-by-user-activation" allow="autoplay *; encrypted-media *;" style="width: 100%; max-width: 100%; overflow: hidden; border-radius: 10px; background: transparent none repeat scroll 0% 0%;" height="450px" frameborder="0"></iframe>
  </div>

</div>
