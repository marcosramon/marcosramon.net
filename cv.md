---
layout: Post
title: Currículo
permalink: /cv/
date: 2025-01-01
description: Currículo Acadêmico e Profissional de Marcos Ramon.
content-type: static
---

<style>
  /* --- Layout do Currículo --- */
  .cv-container {
    font-family: inherit;
    max-width: 100%;
  }

  /* --- Botões de Perfil (Topo) --- */
  .cv-profiles {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 50px;
    padding-bottom: 30px;
    border-bottom: 1px solid var(--color-border-light);
  }

  .cv-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 16px;
    border: 1px solid var(--color-border);
    border-radius: 30px; /* Botões arredondados */
    text-decoration: none !important;
    color: var(--color-text-main) !important;
    font-size: 0.9rem;
    font-weight: 500;
    background: var(--color-bg-sub);
    transition: all 0.2s ease;
  }

  .cv-btn:hover {
    border-color: var(--color-text-link);
    color: var(--color-text-link) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }

  .cv-btn i {
    font-size: 1.1rem;
    color: var(--color-text-link);
  }

  /* --- Seções do CV --- */
  .cv-section {
    margin-bottom: 50px;
  }

  .cv-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--color-text-main);
    margin-bottom: 25px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .cv-title i {
    color: var(--color-text-link);
    font-size: 1.2rem;
    opacity: 0.8;
  }

  /* --- Itens da Linha do Tempo --- */
  .cv-item {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
  }

  .cv-date {
    flex-shrink: 0;
    width: 120px;
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--color-text-sub);
    text-align: right;
    padding-top: 2px;
  }

  .cv-content {
    flex-grow: 1;
    border-left: 2px solid var(--color-border-light);
    padding-left: 20px;
    padding-bottom: 10px;
  }

  .cv-item:last-child .cv-content {
    border-left: 2px solid transparent;
  }

  .cv-main-text {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--color-text-main);
    margin-bottom: 5px;
    line-height: 1.3;
  }

  .cv-sub-text {
    font-size: 1rem;
    color: var(--color-text-main);
    margin-bottom: 5px;
  }

  .cv-desc {
    font-size: 0.9rem;
    color: var(--color-text-sub);
    line-height: 1.5;
    margin-bottom: 5px;
  }

  /* --- Tags de Competências/Idiomas (Corrigido) --- */
  .skills-list {
    display: flex;
    flex-wrap: wrap; /* Garante a quebra de linha no celular */
    gap: 10px;       /* Espaçamento consistente */
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .skill-tag {
    background: var(--color-bg-sub);
    border: 1px solid var(--color-border-light);
    padding: 6px 14px;
    border-radius: 20px; /* Estilo Pílula (arredondado) */
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--color-text-main);
    transition: all 0.2s ease;
    line-height: 1.2;
    cursor: default;
  }

  .skill-tag:hover {
    border-color: var(--color-text-link);
    transform: translateY(-1px);
  }

  /* --- Responsividade --- */
  @media (max-width: 768px) {
    .cv-item {
      flex-direction: column;
      gap: 5px;
    }
    .cv-date {
      width: 100%;
      text-align: left;
      margin-bottom: 5px;
      color: var(--color-text-link); /* Destaque na data no mobile */
    }
    .cv-content {
      border-left: none;
      padding-left: 0;
      border-top: 1px solid var(--color-border-light);
      padding-top: 10px;
    }
  }
</style>

<div class="cv-container">

  <div class="cv-profiles">
    <a href="http://lattes.cnpq.br/9538072103558772" target="_blank" class="cv-btn">
      <i class="fa-solid fa-graduation-cap"></i> Currículo Lattes
    </a>
    <a href="https://orcid.org/0000-0002-8720-8706" target="_blank" class="cv-btn">
      <i class="fa-brands fa-orcid"></i> ORCID
    </a>
    <a href="mailto:marcos.ferreira@ifb.edu.br" class="cv-btn">
      <i class="fa-solid fa-envelope"></i> E-mail
    </a>
    <a href="{{ '/publicacoes' | relative_url }}" class="cv-btn">
      <i class="fa-solid fa-book-open"></i> Ver Publicações
    </a>
  </div>

  <div class="cv-section">
    <div class="cv-title"><i class="fa-solid fa-user-graduate"></i> Formação Acadêmica</div>
    
    <div class="cv-item">
      <div class="cv-date">2012 - 2014</div>
      <div class="cv-content">
        <div class="cv-main-text">Doutorado em Comunicação</div>
        <div class="cv-sub-text">Universidade de Brasília (UnB)</div>
        <div class="cv-desc">Tese: Cultura, Complexidade e Colaboração Online: uma visão da Comunicação.</div>
      </div>
    </div>

    <div class="cv-item">
      <div class="cv-date">2009 - 2011</div>
      <div class="cv-content">
        <div class="cv-main-text">Mestrado em Cultura e Sociedade</div>
        <div class="cv-sub-text">Universidade Federal do Maranhão (UFMA)</div>
        <div class="cv-desc">Dissertação sobre o produtor-artista e a cibercultura.</div>
      </div>
    </div>

    <div class="cv-item">
      <div class="cv-date">1999 - 2004</div>
      <div class="cv-content">
        <div class="cv-main-text">Licenciatura em Filosofia</div>
        <div class="cv-sub-text">Universidade Federal do Maranhão (UFMA)</div>
      </div>
    </div>
  </div>

  <div class="cv-section">
    <div class="cv-title"><i class="fa-solid fa-briefcase"></i> Atuação Profissional</div>
    
    <div class="cv-item">
      <div class="cv-date">2010 - Atual</div>
      <div class="cv-content">
        <div class="cv-main-text">Professor EBTT</div>
        <div class="cv-sub-text">Instituto Federal de Brasília (IFB)</div>
        <div class="cv-desc">
          Atuação no ensino de Filosofia e em cursos de Licenciatura em Dança e Mestrado Profissional (ProfEPT).
          Coordenador do Grupo Interdisciplinar de Pesquisa em Filosofia e Cultura.
          Coordenador de Comunicação (2023-2024).
          Coordenador de Pesquisa (2018-2019).
        </div>
      </div>
    </div>

    <div class="cv-item">
      <div class="cv-date">2006 - 2010</div>
      <div class="cv-content">
        <div class="cv-main-text">Professor</div>
        <div class="cv-sub-text">Universidade Federal do Maranhão (UFMA)</div>
        <div class="cv-desc">Atuação no Colégio Universitário (COLUN) e no Departamento de Filosofia.</div>
      </div>
    </div>

    <div class="cv-item">
      <div class="cv-date">2005 - 2006</div>
      <div class="cv-content">
        <div class="cv-main-text">Professor Substituto</div>
        <div class="cv-sub-text">Instituto Federal do Maranhão (IFMA)</div>
      </div>
    </div>
  </div>

  <div class="cv-section">
    <div class="cv-title"><i class="fa-solid fa-layer-group"></i> Áreas de Interesse</div>
    <div class="skills-list">
      <span class="skill-tag">Filosofia</span>
      <span class="skill-tag">Estética</span>
      <span class="skill-tag">Cibercultura</span>
      <span class="skill-tag">Educação Profissional</span>
      <span class="skill-tag">Tecnologias Educacionais</span>
      <span class="skill-tag">Podcast</span>
    </div>
  </div>

  <div class="cv-section">
    <div class="cv-title"><i class="fa-solid fa-language"></i> Idiomas</div>
    
    <div class="cv-item">
      <div class="cv-date">Inglês</div>
      <div class="cv-content" style="border-left: none; padding-left: 0;">
        <div class="skills-list"> <span class="skill-tag">Compreende Bem</span>
          <span class="skill-tag">Lê Bem</span>
          <span class="skill-tag">Fala Razoavelmente</span>
        </div>
      </div>
    </div>
    
    <div class="cv-item">
      <div class="cv-date">Espanhol</div>
      <div class="cv-content" style="border-left: none; padding-left: 0;">
        <div class="skills-list">
          <span class="skill-tag">Lê Razoavelmente</span>
        </div>
      </div>
    </div>
    
    <div class="cv-item">
      <div class="cv-date">Francês</div>
      <div class="cv-content" style="border-left: none; padding-left: 0;">
        <div class="skills-list">
          <span class="skill-tag">Lê Razoavelmente</span>
        </div>
      </div>
    </div>
  </div>

</div>
