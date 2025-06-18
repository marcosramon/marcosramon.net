---
title: PodcastFriday
date: 2016-09-16
tags:
  - filosofia
  - reflexão
  - cotidiano
  - arte
  - estética
  - Grafos
  - pesquisa
description: "Análise do uso da hashtag #podcastfriday"
image: 
permalink: podcastfriday
---
# #PodcastFriday

Análise do uso da hashtag #podcastfriday no dia 16/09/2016

---


Ontem, dia 16/09/2016, o [Jurandir Filho](https://medium.com/u/9922ba124ee3), dos podcasts [Cinema com Rapadura](http://cinemacomrapadura.com.br/) e [99 Vidas](http://99vidas.com.br/), apresentou uma proposta de utilização da sexta-feira como um dia para se divulgar/indicar podcasts:

![](https://twitter.com/jurandirfilho/status/776787756378763265)

Como quem gosta de podcast geralmente segue outras pessoas que também costumam falar sobre o assunto, acabei vendo no Twitter, logo cedo, as pessoas utilizando a hashtag #podcastfriday com as recomendações de outros programas e promoção dos próprios (no caso de quem não só ouve, mas também faz podcasts).

Um podcast é algo relativamente simples de se acessar; e, sendo gratuito, era de se esperar que mais pessoas aderissem à mídia. No entanto, apesar da simplicidade que mencionei, é ainda difícil pra muita gente explicar como esses produtos são distribuídos e como podem ser acessados. Isso se deve ao fato de que não temos [um Youtube para os podcasts](https://medium.com/@_lindsayp/where-is-the-youtube-for-podcasts-144d71cfcdc#.5hopvblis), mas também ocorre, eu acredito, por conta da impressão de que existe pouca diversidade temática nos podcasts, o que afasta as pessoas que não estejam interessadas em saber sobre cultura pop por meio dos podcasts.

Nos Estados Unidos o podcast já é uma mídia com muito espaço. E isso é assim, em grande parte, porque alguns dos grandes fenômenos de público de lá tratam de temas bem diversos (tome os podcasts [Serial](https://serialpodcast.org/), [Radiolab](http://www.radiolab.org/) e [WTF With Marc Maron](http://www.wtfpod.com/), todos com grande audiência, como exemplos). No Brasil, no entanto, a maior parte dos criadores se dedicam a um mesmo tipo de produção: uma roda de conversa sobre entretenimento (cinema, quadrinhos, séries, games etc). Existem, obviamente, iniciativas diferentes: [Projeto Humanos](http://projetohumanos.com.br/), [Mamilos](http://www.b9.com.br/podcasts/mamilos/), [Café Brasil](http://www.portalcafebrasil.com.br/todos/podcasts/) e muitos outros. O que estou dizendo, portanto, não é que falta diversidade nos temas e propostas de podcast no Brasil, mas sim que a _maioria_ dos podcasts são monotemáticos. Alie a isso o fato de que alguns dos podcasts com mais público do Brasil ([Nerdcast](https://jovemnerd.com.br/nerdcast/), [MRG](https://jovemnerd.com.br/mrg/), [Melhores do Mundo](http://melhoresdomundo.net/category/podcast/) etc) tratam quase que exclusivamente de entretenimento; e são justamente esses que acabam sendo lembrados quando alguém vem com aquela pergunta bacana: _Me indica um podcast?_

Não é errado, obviamente, fazer ou ouvir podcasts sobre entretenimento. Cada um faz e consome o que quer. E pra quem gosta muito de um assunto, quanto mais melhor. No entanto, pra mídia como um todo é extremamente negativo que no espaço de um mês, por exemplo, saiam 100 episódios sobre _Stranger Things_ ou _Esquadrão Suicida_. A não ser que as abordagens sejam realmente diferentes, a saturação do _tema do momento_ afasta pessoas interessadas em outros assuntos e olhares. E é por isso que eu penso que uma iniciativa como a #podcastfriday pode ser uma grande virada.

O Ivan Mizanzuk (do [Anticast](http://anticast.com.br/) e Projeto Humanos) sugeriu, em um post, que um mapeamento desse #podcastfriday poderia auxiliar as pessoas a encontrarem correlações entre os ouvintes e temas:

![](https://twitter.com/mizanzuk/status/776891760798826496)

O Murilo Ferraz do [Filosofia Pop](http://filosofiapop.com.br/) me marcou na postagem e eu comprei o desafio. Então, o que fiz foi o seguinte: extraí os dados de ontem do Twitter para chegar em algo próximo dessa correlação de quem gosta do quê. Consegui, com o [Netlytic](https://netlytic.org/), extrair 1317 tweets com a hashtag #podcastfriday, todos postados até a meia noite do dia 16/09. Os gráficos que eu mostro mais abaixo foram gerados com o [Beam](https://beam.venngage.com/) e os [grafos](https://pt.wikipedia.org/wiki/Teoria_dos_grafos) foram feitos com o [Gephi](https://gephi.org/). Seguem os dados:

<img src="/assets/img/Pasted image 20250311153736.png">
Grafo com a rede de tweets sobre a #podcastfriday.

A imagem acima representa um grafo da conversação no Twitter sem os termos (_hashtags_ e usuários). Um grafo é composto por _nós_ (os pontos de conexão) e arestas (as conexões entre os nós). Nessa representação eu escolhi separar as áreas de interesse por cores. Assim, podemos ver um grupo azul, verde, laranja etc. Esses são os grupos que conversaram entre si e/ou indicaram os mesmos podcasts. A imagem final que conseguir gerar é gigantesca (10000 por 10000 pixels). Se você quiser, pode baixar a imagem original em .[pgn](https://drive.google.com/open?id=0B_NS1VYqt3XBaHBueUlUcjFtLUU) ou .[pdf](https://drive.google.com/open?id=0B_NS1VYqt3XBMHZPdVFwNHpfTFk) para ampliar e verificar os dados com mais detalhes. A vantagem caso do pdf é poder fazer busca por termos, mas pra isso você precisa dar um zoom monstruoso (pelo menos 800%).

Mais pra frente eu vou voltar pra essa imagem dando um zoom em algumas áreas, mas antes veja alguns outros dados interessantes:
<img src="/assets/img/Pasted image 20250311153753.png">
<img src="/assets/img/Pasted image 20250311153806.png">

Você pode [baixar aqui o arquivo do Excel (.csv)](https://drive.google.com/open?id=0B_NS1VYqt3XBTktaYUNYODdhWUk) com todos os tweets extraídos, caso tenha interesse.

#### Grafo com as redes conectadas com menções aos podcasts e usuários:
<img src="/assets/img/Pasted image 20250311153822.png">
Grafo com a rede de tweets com termos utilizados.

Na imagem acima as cores representam os grupos, ou seja, pessoas que demonstraram interesse mútuo nos mesmos podcasts e/ou perfis. Dando zoom em alguns focos da imagem é possível ver essas conexões de maneira mais clara:
<img src="/assets/img/Pasted image 20250311153834.png">
O #anticast foi o podcast mais mencionado e sua rede principal é essa de cor azul.

<img src="/assets/img/Pasted image 20250311153846.png">
Rede do podcast #99vidas , com a cor laranja.

<img src="/assets/img/Pasted image 20250311153901.png">
Um grupo bem concentrado (de verde) em torno do #algumacoisacast.

<img src="/assets/img/Pasted image 20250311153911.png">
Rede lilás com maior presença do #jogabilidade.

<img src="/assets/img/Pasted image 20250311153921.png">
O termo #jurandirfilho (vermelho) se conectando com #rapadura, #jovemnerd e #99vidas (laranja).

Como disse antes, o que acho bacana na iniciativa do Jurandir é que essa ação, se se tornar contínua, conseguirá atrair mais pessoas para a mídia por meio da ampliação das redes de indicações que serão criadas. Vi muita gente descobrindo e indicando coisas novas, o que certamente ampliará a diversidade e longevidade do podcast.

![](https://twitter.com/Laianne27/status/776898982765264896)

Os fenômenos de massa sempre vão existir, em qualquer mídia que seja; mas o reconhecimento da variedade de temas dos podcasts (e, acredite, tem podcast sobre muita coisa que você nem imagina) vai aproximar mais pessoas da mídia e estimular quem tem ideias diferentes pra colocar em prática. O difícil é imaginar que a empolgação nas próximas sextas continuará a mesma. Será?

---

**Update (24/09/2016, 23h)**: ontem foi o segundo dia da #PodcastFriday. Fiz uma análise comparativa aqui: [[HTML import/#PodcastFriday, dia 2|#PodcastFriday, dia 2]]


#filosofia #arte

> Leia também:
> - <a href="/podcastfriday-dia-2">PodcastFriday, dia 2</a>
> - <a href="/podcastfriday-tres-meses-depois">Podcastfriday, três meses depois</a>
> - <a href="/visualizando-a-pesquisa">Visualizando a pesquisa</a>
