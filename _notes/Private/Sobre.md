---
layout: Post
title: Sobre
date: 2025-06-25
permalink: /sobre
author: Marcos Ramon
excerpt: Marcos Ramon, professor de filosofia no IFB, pesquisando estética, cibercultura e ensino.
og_image: /arquivos/tolis2023 1.jpg
feed: hide
---

<style>
  /* --- Layout Geral --- */
  .about-container {
    font-family: inherit;
    max-width: 100%;
  }

  /* --- Seção de Perfil (Topo) --- */
  .profile-header {
    display: flex;
    gap: 30px;
    align-items: center;
    margin-bottom: 40px;
    padding-bottom: 30px;
    border-bottom: 1px solid var(--color-border-light);
  }

  .profile-img-wrapper {
    flex-shrink: 0;
    width: 220px;
  }

  .profile-img-wrapper img {
    width: 100%;
    border-radius: 50%; /* Foto redonda */
    border: 4px solid var(--color-bg-sub);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  }

  .profile-bio {
    flex-grow: 1;
    font-size: 1.1rem;
    line-height: 1.6;
    color: var(--color-text-main);
  }

  /* --- Blocos de Conteúdo --- */
  .about-section {
    margin-bottom: 40px;
  }

  .about-section h2 {
    font-size: 1.4rem;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--color-border-light);
    color: var(--color-text-main);
  }

  .about-section h3 {
    font-size: 1.1rem;
    margin-top: 25px;
    margin-bottom: 15px;
    color: var(--color-text-main);
  }

  /* --- Grid de Links (Acadêmico + Outros) --- */
  .links-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 15px;
    margin-bottom: 30px;
  }

  .link-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 15px;
    background: var(--color-bg-sub);
    border: 1px solid var(--color-border-light);
    border-radius: 8px;
    text-decoration: none !important;
    color: var(--color-text-main) !important;
    transition: all 0.2s ease;
  }

  .link-card:hover {
    border-color: var(--color-text-link);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }

  .link-icon {
    font-size: 1.5rem;
    color: var(--color-text-link);
    width: 30px;
    text-align: center;
  }

  .link-info strong {
    display: block;
    font-size: 0.95rem;
  }

  .link-info span {
    font-size: 0.85rem;
    color: var(--color-text-sub);
  }

  /* --- Caixas de Destaque (Tech, Citação, Licença) --- */
  .info-box {
    background: var(--color-bg-sub);
    padding: 20px;
    border-radius: 8px;
    border: 1px solid var(--color-border-light);
    margin-bottom: 30px;
    font-size: 0.95rem;
  }

  .citation-box {
    background: rgba(0,0,0,0.02);
    border-left: 4px solid var(--color-text-link);
    padding: 15px;
    font-family: monospace;
    color: var(--color-text-main);
    margin-top: 15px;
  }

  /* --- Responsividade --- */
  @media (max-width: 768px) {
    .profile-header {
      flex-direction: column;
      text-align: center;
    }
    .profile-img-wrapper {
      width: 180px;
      margin-bottom: 10px;
    }
    .links-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="about-container">

  <div class="profile-header">
    <div class="profile-img-wrapper">
      <img src="assets/img/tolis2023 1.jpg" alt="Marcos Ramon">
    </div>
    <div class="profile-bio">
      <p>Meu nome é [[Marcos Ramon]]. Sou professor de Filosofia no Instituto Federal de Brasília, onde pesquiso cibercultura, estética e cultura digital.</p>
      <p>Aqui você vai encontrar uma série de textos e publicações que tenho feito ao longo dos anos, assim como indicações dos meus podcasts e vídeos. É tudo feito por puro diletantismo. Então, encare esses materiais como trabalhos em processo. 😉</p>
      <p>Para ver todos os textos do blog, utilize o <a href="https://marcosramon.net/posts">índice</a> ou explore o site de outras formas. 👇🏻</p>
    </div>
  </div>

  <div class="about-section">
    <h2>Como funciona este site?</h2>
    <p>Este site é um espaço de ideias interconectadas, organizado de maneira não linear, semelhante a um [jardim digital](https://maggieappleton.com/garden-history)[^1]. Aqui, não há uma hierarquia rígida a ser seguida; as conexões surgem organicamente por meio de links internos, permitindo que os temas se cruzem e evoluam com o tempo, no estilo de um [wiki](https://pt.wikipedia.org/wiki/Wiki).</p>
    
    <div class="info-box">
      <p>Na página <a href="https://marcosramon.net/notes"><strong>Wiki</strong></a> você encontra uma combinação de wiki pessoal, textos ou anotações relacionadas à minha pesquisa e interesses acadêmicos.</p>
      <p>Já em <a href="https://marcosramon.net/posts"><strong>Blog</strong></a> você pode ler os textos em formato de crônica e reflexões sobre o cotidiano que escrevo regularmente.</p>
      <p style="margin-bottom: 0;">Abaixo dos textos você vai ver indicações para outras publicações dentro site, sendo essa uma outra forma de navegar aqui. Não há seção de comentário no site, mas se quiser conversar sobre qualquer texto ou publicação, mande um <a href="mailto:marcosramon@gmail.com">email</a>.</p>
    </div>

    <h3>Sobre o site</h3>
    <p class="tech-stack" style="font-size: 0.9rem; color: var(--color-text-sub);">
      Este site é publicado com <a href="https://obsidian.md/">Obsidian</a>, <a href="https://jekyllrb.com/">Jekyll</a> e <a href="https://pages.github.com/">GitHub Pages</a>. O template que utilizo é uma versão customizada de <a href="https://jekyll-garden.github.io/">Jekyll Garden</a>.
    </p>
  </div>

  <div class="about-section">
    <h2>Conexões e Vida Acadêmica</h2>
    
    <p>Aqui segue o link do meu currículo lattes e do Orcid. Se quiser saber mais, acesse outros dados sobre minha [[Vida acadêmica]]. Quem tiver interesse em trocar ideias sobre a pesquisa é só mandar um [email](mailto:marcosramon@gmail.com).</p>

    <div class="links-grid">
      <a href="http://lattes.cnpq.br/9538072103558772" target="_blank" class="link-card">
        <div class="link-icon"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="link-info"><strong>Currículo Lattes</strong><span>Plataforma Lattes</span></div>
      </a>
      
      <a href="https://orcid.org/0000-0002-8720-8706" target="_blank" class="link-card">
        <div class="link-icon"><i class="fa-brands fa-orcid"></i></div>
        <div class="link-info"><strong>ORCID</strong><span>0000-0002-8720-8706</span></div>
      </a>

      <a href="https://www.youtube.com/conexaofilosofica" target="_blank" class="link-card">
        <div class="link-icon"><i class="fa-brands fa-youtube"></i></div>
        <div class="link-info"><strong>Conexão Filosófica</strong><span>Vídeos de aula e filosofia</span></div>
      </a>

      <a href="/ficcoes" class="link-card">
        <div class="link-icon"><i class="fa-solid fa-microphone-lines"></i></div>
        <div class="link-info"><strong>Podcast Ficções</strong><span>Narrativas filosóficas</span></div>
      </a>

      <a href="/livros" class="link-card">
        <div class="link-icon"><i class="fa-solid fa-book"></i></div>
        <div class="link-info"><strong>Meus Livros</strong><span>Publicações autorais</span></div>
      </a>
    </div>
  </div>

  <div class="about-section">
    <h2>Como citar</h2>
    <p>Para citar qualquer texto deste site em formato acadêmico, utilize o [modelo de referência para sites da ABNT](https://normaliza.ifb.edu.br/doku.php?id=referencias:modelos_de_referencias:documentos_em_meio_eletronico:documentos_de_acesso_exclusivo_em_meio_eletronico):</p>
    
    <div class="citation-box">
      <strong>Exemplo:</strong><br>
      RAMON, Marcos. <strong>A releitura como forma de reencontro.</strong> Disponível em: &lt;https://marcosramon.net/a-releitura-como-forma-de-reencontro&gt;. Acesso em: 2 mar. 2025.
    </div>
  </div>

  <div class="about-section">
    <h2>Uso e compartilhamento</h2>
    <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 250px;">
        <p>Este é um site pessoal e eu autorizo o compartilhamento, a distribuição e a remixagem de tudo que tem aqui (exceto aquilo que não for de minha autoria, porque aí não depende de mim), desde que o propósito disso não envolva fins comerciais e desde que seja mencionada a fonte original. Mais informações sobre essa licença de uso nesse [link](http://creativecommons.org/licenses/by-nc-sa/3.0/br/).</p>
      </div>
      <div>
        <img src="assets/img/Pasted image 20250302190730.png" width="120" style="opacity: 0.8;">
      </div>
    </div>
  </div>

</div>

[^1]: Um jardim digital é um espaço online para ideias em constante evolução, e, portanto, diferente de um blog tradicional. Em vez de textos apenas organizados por data, ele funciona como um ambiente exploratório, onde notas e reflexões se conectam organicamente. É um conceito que quer resgatar a liberdade criativa dos primeiros dias da web.
