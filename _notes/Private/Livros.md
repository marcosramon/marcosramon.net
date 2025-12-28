---
layout: Post
title: Livros
feed: hide
author: Marcos Ramon
date: 2025-06-25
description: Livros publicados por Marcos Ramon
image: descompasso-div.png
permalink: livros
---

<style>
  /* --- Layout Geral --- */
  .books-intro {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 3rem;
    color: var(--color-text-main);
  }

  .intro-links {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    flex-wrap: wrap;
  }

  /* --- Cartão do Livro --- */
  .book-item {
    display: flex;
    gap: 30px;
    margin-bottom: 60px;
    padding-bottom: 40px;
    border-bottom: 1px solid var(--color-border-light);
  }

  .book-item:last-child {
    border-bottom: none;
  }

  /* Capa do Livro */
  .book-cover {
    flex-shrink: 0;
    width: 200px;
  }

  .book-cover img {
    width: 100%;
    border-radius: 5px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    transition: transform 0.2s ease;
  }

  .book-cover img:hover {
    transform: scale(1.02);
  }

  /* Detalhes do Livro */
  .book-details {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .book-title {
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--color-text-main);
    line-height: 1.3;
  }

  .book-desc {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--color-text-main);
    margin-bottom: 20px;
  }

  /* Botões */
  .book-actions {
    margin-top: auto;
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }

  .action-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 8px 16px; /* Padding reduzido para botões mais compactos */
    border: 1px solid var(--color-border);
    border-radius: 6px;
    text-decoration: none !important;
    color: var(--color-text-main) !important;
    font-size: 0.9rem;
    font-weight: 600;
    background: var(--color-bg-sub);
    transition: all 0.2s ease;
  }

  .action-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  .action-btn.primary {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
    background: rgba(0,0,0,0.02);
  }

  /* Seção de Contato */
  .contact-section {
    margin-top: 20px;
    background: var(--color-bg-sub);
    padding: 20px;
    border-radius: 8px;
    border: 1px solid var(--color-border-light);
  }

  /* --- RESPONSIVIDADE (CELULAR) --- */
  @media (max-width: 768px) {
    .book-item {
      flex-direction: column;
      align-items: flex-start; /* Alinha tudo à esquerda */
      text-align: left;
      gap: 15px;
    }
    
    .book-cover {
      width: 120px; /* Capa menor e alinhada à esquerda */
      margin-bottom: 5px;
    }

    .book-title {
      font-size: 1.3rem;
      text-align: left; /* Título à esquerda */
    }

    .book-desc {
      text-align: left;
      font-size: 0.95rem;
    }

    .book-actions {
      width: 100%;
      flex-direction: row; /* Botões lado a lado se couberem */
      justify-content: flex-start; /* Alinhados à esquerda */
    }

    .action-btn {
      width: auto; /* Tamanho natural do botão */
      font-size: 0.85rem; /* Fonte um pouco menor no celular */
      padding: 8px 12px;
    }
    
    .intro-links .action-btn {
        width: auto;
        justify-content: flex-start;
    }
  }
</style>

<div class="books-intro">
  <p>
    Tenho dois livros autopublicados disponíveis em formato ebook na Amazon. Se você já leu algum deles, agradeço se fizer uma avaliação na Amazon, Goodreads, Skoob em algum outro lugar semelhante.
  </p>
  
  <div class="intro-links">
    <a href="https://www.goodreads.com/author/show/16012578.Marcos_Ramon" target="_blank" class="action-btn">
      <i class="fa-brands fa-goodreads"></i> Goodreads
    </a>
    <a href="https://www.skoob.com.br/autor/23478-marcos-ramon" target="_blank" class="action-btn">
      <i class="fa-solid fa-book"></i> Skoob
    </a>
  </div>
</div>

<hr style="margin-bottom: 50px;">

<div class="book-item">
  <div class="book-cover">
    <img src="assets/img/Pasted image 20250306152840.png" alt="Capa do livro A estética da angústia">
  </div>
  
  <div class="book-details">
    <h2 class="book-title">A estética da angústia: uma aproximação entre Schopenhauer e os Peanuts</h2>
    
    <div class="book-desc">
      Este livro propõe, a partir do tema da angústia, uma aproximação entre a filosofia de Arthur Schopenhauer e os quadrinhos de Charles Schulz. Os fundamentos da angústia são apresentados de acordo com a filosofia pessimista de Schopenhauer, propondo em seguida uma relação desta filosofia com o caráter dos Peanuts (Charlie Brown, Lucy, Linus, Snoopy e Schroeder).
    </div>
    
    <div class="book-actions">
      <a href="https://amzn.to/43pFb8t" target="_blank" class="action-btn primary">
        <i class="fa-brands fa-amazon"></i> Comprar eBook na Amazon
      </a>
    </div>
  </div>
</div>

<div class="book-item">
  <div class="book-cover">
    <img src="assets/img/Pasted image 20250306152907.png" alt="Capa do livro Descompasso">
  </div>
  
  <div class="book-details">
    <h2 class="book-title">Descompasso</h2>
    
    <div class="book-desc">
      Crônicas e ensaios sobre filosofia, arte, ensino e cotidiano. Neste livro, Marcos Ramon (professor de Filosofia, escritor, podcaster) relata experiências e propõe reflexões sobre a realidade a partir do que observa e vivencia. Um convite a uma forma mais atenta de se olhar o cotidiano.
    </div>
    
    <div class="book-actions">
      <a href="https://amzn.to/41rUU4n" target="_blank" class="action-btn primary">
        <i class="fa-brands fa-amazon"></i> Comprar eBook na Amazon
      </a>
    </div>
  </div>
</div>

<div class="contact-section">
  <h3>✉️ Contato</h3>
  <p style="margin-bottom: 0;">
    Para falar comigo sobre os livros, parcerias ou outros assuntos, mande um email para: 
    <a href="mailto:marcos.ferreira@ifb.edu.br" style="font-weight: bold; color: var(--color-text-link);">marcos.ferreira@ifb.edu.br</a>
  </p>
</div>
