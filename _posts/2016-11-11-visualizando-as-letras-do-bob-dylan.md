---
title: Visualizando as letras do Bob Dylan
date: 2016-11-11
tags:
  - pensamentos
  - música
  - Grafos
  - pesquisa
description: O Eduardo Friedman fez uma seleção com algumas das melhores letras do Bob Dylan. No post ele explica o motivo da escolha das canções e do…
image:
permalink: visualizando-as-letras-do-bob-dylan
---
O [Eduardo Friedman](https://medium.com/u/4c7cd2bb169b) fez uma seleção com algumas das melhores letras do Bob Dylan. [No post](https://cabineliteraria.com.br/melhores-letras-do-dylan-1964-1976-4f7715f25940#.1tgafgnht) ele explica o motivo da escolha das canções e do período da obra do Dylan (1964–1976). Como forma de contribuir/retribuir, eu fiz um [grafo](https://pt.wikipedia.org/wiki/Teoria_dos_grafos) com os termos mais utilizados pelo Dylan nesse conjunto de letras.

Para montar o grafo eu utilizei o algoritmo do [Nodus Labs](http://noduslabs.com/) criado pelo [Dmitry Paranyushkin](https://www.facebook.com/deemeetree?fref=ts). Depois processei o arquivo com o [Gephi](https://gephi.org/) e cheguei no resultado abaixo:

<img src="/assets/img/visualizando-as-letras-do-bob dylan-medium-1.png">

Quando montei o grafo coloquei todas as letras das músicas juntas em um arquivo só. O grafo mostra, portanto, a correlação entre os principais termos utilizados no conjunto do que Dylan escreveu [nessas sete canções](https://drive.google.com/open?id=1kbZfpERvNFRUEAWwX7inKH-bJJn8MerFx0noOCqljmM). Da mesma forma, a separação por cores nas [arestas](https://pt.wikipedia.org/wiki/Aresta) mostra a proximidade do uso das palavras no todo e não, necessariamente, em cada música. Importante pontuar que o algoritmo já tem um conjunto de _stopwords_, mas seria possível também fazer um grafo manual com um número maior de termos/palavras analisando cada uma em separado de acordo com a sua importância no contexto da canção. Além do grafo, fiz também uma nuvem de palavras com o [Voyant Tools](https://voyant-tools.org/):

<img src="/assets/img/visualizando-as-letras-do-bob dylan-medium-2.png">

Achei interessante fazer isso como uma extensão de um experimento que eu já tinha feito com visualização de letras de música como [[[Blog/Visualizando letras de música como networks|networks]].

Não sei bem o que fazer com essas coisas, mas vou continuar testando possibilidades. Ah, montei também uma playlist no Spotify com a seleção do [Eduardo Friedman](https://medium.com/u/4c7cd2bb169b):

#música #Grafos

> Leia também:
> - [[Blog/Visualizando a hashtag diadopodcast|Visualizando a hashtag diadopodcast]]
> - [[A importância do contexto]]
> - [[4'33'']]

