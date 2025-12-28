---
layout: Post
title: Now
inline: false
date: 2025-12-27 10:00:00-0300
author: Marcos Ramon
---

<style>
  /* --- Layout Geral da Página Now --- */
  .now-intro {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    color: var(--color-text-main);
  }

  .now-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  /* --- Cartões de Seção --- */
  .now-section {
    background: var(--color-bg-sub); /* Fundo sutil */
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid var(--color-border-light);
  }

  .now-section h3 {
    margin-top: 0;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    border-bottom: 2px solid var(--color-border);
    padding-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .now-section h3 i {
    color: var(--color-text-link); /* Cor de destaque */
    font-size: 1rem;
  }

  /* --- Listas de Itens --- */
  .now-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .now-list li {
    margin-bottom: 0.8rem;
    line-height: 1.5;
    padding-left: 0; /* Remove recuo padrão */
  }

  /* --- Sistema de Classificação (Estrelas) --- */
  .media-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex-wrap: wrap;
    border-bottom: 1px dashed var(--color-border-light);
    padding-bottom: 8px;
    margin-bottom: 12px;
  }

  .media-title {
    font-weight: 600;
    margin-right: 10px;
  }

  .media-author {
    font-size: 0.85rem;
    color: var(--color-text-sub);
    margin-right: auto; /* Empurra as estrelas para a direita */
  }

  .rating {
    white-space: nowrap;
    font-size: 0.8rem;
    color: #f59e0b; /* Cor amarela/dourada para as estrelas */
  }
  
  .rating .fa-regular {
    color: var(--color-border); /* Estrela vazia cinza */
  }

  .rating-label {
    font-size: 0.7rem;
    color: var(--color-text-sub);
    margin-left: 5px;
    font-weight: normal;
  }

  /* --- Rodapé da Página --- */
  .now-footer {
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid var(--color-border-light);
    font-size: 0.85rem;
    color: var(--color-text-sub);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  @media (min-width: 768px) {
    .now-grid {
      grid-template-columns: 1fr 1fr; /* Duas colunas em telas maiores */
    }
    .full-width {
      grid-column: span 2;
    }
  }
</style>

<div class="now-intro">
  Neste momento estou entrando de férias e aproveitando para organizar as coisas e atualizar meus materiais de trabalho para o próximo semestre.
</div>

<div class="now-grid">

  <div class="now-section full-width">
    <h3><i class="fa-solid fa-briefcase"></i> Foco Profissional & Estudos</h3>
    <ul class="now-list">
      <li><strong>Estética e História da Arte:</strong> Planejando a implementação de novos conteúdos baseados nos cursos que fiz no MASP este semestre.</li>
      <li><strong>IA na Educação:</strong> Atualizando textos e gravando novos vídeos para a nova turma do curso de Aplicações da Inteligência Artificial.</li>
      <li><strong>Filosofia:</strong> Revisão geral dos materiais didáticos para o ensino médio.</li>
    </ul>
  </div>

  <div class="now-section">
    <h3><i class="fa-solid fa-book-open"></i> Lendo</h3>
    
    <div class="media-item">
      <span class="media-title">O Aleph</span>
      <span class="media-author">Jorge Luis Borges</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
        <span class="rating-label">(Relendo)</span>
      </span>
    </div>

  </div>

  <div class="now-section">
    <h3><i class="fa-solid fa-tv"></i> Assistindo</h3>
    
    <div class="media-item">
      <span class="media-title">Os bons companheiros</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
      </span>
    </div>

    <div class="media-item">
      <span class="media-title">Uma batalha após a outra</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i>
      </span>
    </div>

    <div class="media-item">
      <span class="media-title">Família Soprano</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
      </span>
    </div>

    <div class="media-item">
      <span class="media-title">Pluribus</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i>
        <span class="rating-label">(Ok)</span>
      </span>
    </div>

    <div class="media-item">
      <span class="media-title">Stranger Things</span>
      <span class="media-author">Temp. Final</span>
      <span class="rating">
        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i><i class="fa-regular fa-star"></i>
        <span class="rating-label">(Ruim)</span>
      </span>
    </div>
  </div>

  <div class="now-section">
    <h3><i class="fa-solid fa-gamepad"></i> Jogando / Fila</h3>
    
    <div class="media-item">
      <span class="media-title">Fez</span>
      <span class="rating">
        <span class="rating-label">Na fila</span>
      </span>
    </div>

    <div class="media-item">
      <span class="media-title"><a href="https://terrycavanagh.itch.io/egg" target="_blank">Egg</a></span>
      <span class="rating">
        <span class="rating-label">Na fila</span>
      </span>
    </div>
  </div>

  <div class="now-section full-width">
    <h3><i class="fa-solid fa-code"></i>Site</h3>
    <p>Atualizei o layout e os recursos do site. Estou animado para voltar a escrever com mais frequência.</p>
    <p><small><em>Fiz as alterações usando o Gemini pra modificar o código, e funcionou direitinho.</em></small></p>
  </div>

</div>

<div class="now-footer">
  <span><i class="fa-regular fa-clock"></i> <strong>Última atualização:</strong> 27 de dezembro de 2025</span>
  <span><a href="https://nownownow.com/about" target="_blank">O que é uma página Now?</a></span>
</div>
