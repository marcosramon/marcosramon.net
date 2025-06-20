---
title: Visualizando a hashtag diadopodcast
date: 2015-10-25
tags:
- podcast
- tecnologia
- internet
- pesquisa
- Grafos
description: O dia 21 de Outubro é o dia do podcast no Brasil. Esse dia é utilizado
  como pretexto para se divulgar de forma mais intensa o podcast no…
image: null
aliases: null
permalink: visualizando-a-hashtag-diadopodcast
author: Marcos Ramon
---
O dia 21 de Outubro é o dia do podcast no Brasil. Esse dia é utilizado como pretexto para se divulgar de forma mais intensa o podcast no Brasil. A ação, que foi idealizada por um [grupo de podcasters brasileiros](http://diadopodcast.com.br/), acaba mobilizando naturalmente um grande número de produtores e consumidores da mídia.

Coletei alguns dados sobre a interação entre essas pessoas no Twitter e coloco aqui algumas impressões. Mas antes de tudo, acho que é importante dizer como cheguei ao material que estou apresentando aqui: utilizei o [NodeXl](http://nodexl.codeplex.com/) e o [Socioviz](http://socioviz.net) para coletar os dados do Twitter e o [Gephi](http://gephi.github.io/) para gerar os [grafos](https://pt.wikipedia.org/wiki/Teoria_dos_grafos).

No primeiro grafo que vou mostrar, por exemplo, estão todos os tweets com a hashtag #diadopodcast que foram postados entre as 19h do dia 19/10 e 18h33 do dia 22/10 de 2015 (1138 tweets, 548 retweets, 520 usuários e 45 hashtags relacionadas). Foi necessário pegar uma amostra um pouco maior do que apenas o dia 21 de Outubro para garantir mais segurança na análise das informações. Os dados coletados estão todos nesta [planinha](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/1445638752768.xls).

No caso do grafo abaixo, dá pra observar a rede toda com os diversos _clusters_ (comunidades, grupos conectados). Encontrei 89 “comunidades”, o que é um número imenso, principalmente se considerarmos que se trata de uma rede tão pequena. (Se você participou da conversação em torno da hashtag #diadopodcast e quiser se encontrar no grafo, [baixe a versão em pdf](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/diadopodcast.pdf), dê um zoom, tecle _Ctrl + f_ e pesquise o seu nome de perfil).

<img src="/assets/img/Pasted image 20250311150726.png">
Acesse a [imagem em alta resolução](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/diadopodcast1.png) ou [pdf](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/diadopodcast.pdf) para uma melhor definição.

Coloco aqui alguns detalhes da rede gerada pelo uso da hashtag:

<img src="/assets/img/Pasted image 20250311150810.png">
Detalhe de alguns dos maiores influenciadores. Veja em [melhor qualidade aqui](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/influenciadores1.png).

Observe na imagem acima que os _nós_ maiores representam alguns influenciadores e a conversação gerada na rede a partir deles. De laranja, por exemplo, estão os perfis @mundopod, @diadopodcast e @thiagomiro centralizando boa parte da interação. Já o perfil @scicastpodcast (de azul, no topo da imagem) é o centro de um outro grupo. Ainda que os dois grupos se relacionem, é possível perceber que a conversação se dispersou em alguns pontos, tornando o centro da rede menos intenso do que poderia ser.

Mas ainda assim, as diversas arestas mostram que houve pelo menos um nível razoável de interação entre boa parte dos perfis. É verdade que a rede ainda é pequena e um pouco polarizada (como observamos na imagem), mas é também verdade que o grafo mostra um engajamento significativo de muitos usuários.

<img src="/assets/img/Pasted image 20250311150820.png">
Detalhe de outro grupo de influenciadores. Veja em [melhor qualidade aqui](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/influenciadores2.png).

No grafo acima, de verde, temos outro perfil extremamente influente: @podflixbrasil. Essa influência é compreensível, principalmente se considerarmos que o perfil em questão é um grande divulgador de episódios de podcasts (e claro que um grande número de episódios foram lançados, não por acaso, no dia 21/10). Se clicar na [imagem ampliada](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/influenciadores2.png) você pode observar que todo o grupo de _nós_ próximos (também verdes) são de podcasts ou de participantes de episódios que foram publicados no dia e marcados junto com a hashtag #diadopodcast.

<img src="/assets/img/Pasted image 20250311150832.png">
Um cluster bem pequeno e alguns “nós” isolados. Veja a [imagem ampliada aqui](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/influenciadores4.png).

Na imagem acima, por outro lado, o que se pode observar é uma comunidade bem pequena envolvida na conversação. Nas extremidades vemos também alguns perfis isolados. Voltando para a [primeira imagem](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/diadopodcast1.png) você pode observar esse padrão se repetindo em vários momentos. A presença dos perfis isolados e dos pequenos aglomerados no grafo mostra a situação de uma rede ainda em crescimento. Em contextos diferentes, com muitos perfis envolvidos e com a conversação centralizada por um número pequeno de influenciadores, essa tendência aos _nós_ isolados é geralmente menor.

Outro fator importante que pude observar foram os perfis mais ativos (em números de tweets enviados):

1. @podflix (187)
2. @padrimbr (33)
3. @nildaalcarinque (32)
4. @ivan_pd (28)
5. @diadopodcast (18)
6. @thiagomiro (16)
7. @podcast_br (16)
8. @mundopod (14)
9. @_airechu (12)
10. @algumacoisacast (12)

Portanto, o perfil oficial da ação #diadopodcast foi apenas o quinto em número de tweets. Essa estatística considera apenas os tweets diretos. No caso do perfil @diadopodcast, portanto, foram apenas 18, mas nada que foi retweetado foi contabilizado aqui. Isso não significa, necessariamente, falta de engajamento, já que esse dado desconsidera parte da interação com os outros perfis. De qualquer forma, a ideia aqui é mostrar que existem outros aspectos necessários para se considerar em relação aos principais participantes da conversação.

Um último aspecto que achei interessante ao recolher os dados foi verificar as palavras mais associadas à hashtag #diadopodcast:

<img src="/assets/img/Pasted image 20250311150843.png">
Grafo com as palavras/hashtags mais comuns utilizadas na conversação sobre o #diadopodcast.

Na imagem acima (acesse em [melhor qualidade aqui](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/palavras4.png) e em [pdf aqui](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/palavras%202.pdf)) aparecem algumas palavras/hashtags associadas diretamente ao universo do podcast e outras nem tanto. Observe os _clusters_ separados por cores para identificar esses diversos grupos de hashtags.

A presença de “teologiadeboteco” e “podcrent” (de azul claro no grafo) e “graçacast” (que não aparece associado aos anteriores), mostra o crescimento do engajamento dos podcasts com temática religiosa no Brasil.

Além desse elemento faço ainda o destaque de alguns outros aspectos que achei importantes. O primeiro é a presença de um pequeno grupo relacionado ao filme [De volta para o futuro](https://pt.wikipedia.org/wiki/Back_to_the_Future), o que certamente é esperado, já que o dia 21/10/2015 foi o dia em que Marty Mcfly chegou ao futuro no segundo filme da trilogia. Nesse grupo aparecem as hashtags “backtothefuture”, “bttf”, “atrasado” e “rubinho” (Barrichello?):

<img src="/assets/img/Pasted image 20250311150855.png">
Observe o grupo de “nós” relacionados à “De volta para o futuro”.

Por fim, dois outros grupos isolados chamam a atenção: um com as hashtags “café” e “cafeína” e outro com “rock” e “metal”.

<img src="/assets/img/Pasted image 20250311150905.png">
Café e Rock na vida dos amantes de podcast?

O perfil @jovemnerd — que participou pouco da rede #diadopodcast, mas possui um grande engajamento por parte dos seus fãs — foi um dos que utilizou a palavra “café” associada com a hashtag #diadopodcast. Como esse tweet específico teve mais de oitenta retweets até o momento da coleta, é mais do que justificável a presença do termo aqui. De qualquer forma, parece que mais gente relacionou o podcast com a falta de sono e o excesso de cafeína e rock na veia.

Além dessas palavras que mencionei perceba que aparecem _nós_ específicos que se referem a alguns podcasts ou projetos pontuais, o que mostra talvez a presença grande de pessoas que admiram e ajudam a divulgar esses projetos (como atestam as hashtags “nossocast”, “scicast2anos” e “projetohumanos”, por exemplo).

Mas agora você pensa assim:

> Ok. Vi as imagens. E isso prova o quê?

Não prova nada. Nem era essa a intenção.

<img src="/assets/img/Pasted image 20250311150926.png">
<small>“Como mostra claramente este gráfico…” (Cartoon de @dazzdoc)</small>

Já ouvi algumas vezes a [Raquel Recuero](http://www.raquelrecuero.com) (@raquelrecuero) — professora da UCPel e pesquisadora na área de análise de redes sociais — falar que não adianta só criar um grafo, é necessário criar também estratégias para interpretar essas representações. E, claro, com poucos elementos isso fica bem difícil. Mas essa foi só uma primeira tentativa de compreender a rede de interações entre os amantes do podcast por meio da visualização de uma conversação específica.

O que pude perceber, de forma geral, é que, apesar da comunidade ainda ser bem pequena (fato revelado na quantidade de tweets) a conversação ocorre de forma intensa ainda que mantendo alguns nichos dentro da própria rede.

Se você acessar o [primeiro grafo em maior resolução](https://dl.dropboxusercontent.com/u/49566417/DiaDoPodcast/diadopodcast.pdf) poderá perceber a presença de pequenos grupos setoriais que mantiveram a conversação de forma mais intensa dentro dos seus próprios grupos (ciência, música, cristãos etc). Vale ressaltar também que os dados que consegui — mesmo nesse dia em que os fãs da mídia estavam mobilizados — ainda foram em um número bem pequeno, revelando o que já é óbvio para os podcasters brasileiros: o podcast ainda está longe, muito longe, de ser um fenômeno de massa (mas será que isso é necessariamente ruim?).

Enfim, esse é um primeiro exercício e a ideia é avançar na coleta e análise de dados para entender melhor o desenvolvimento do podcast no Brasil.

#Grafos #pesquisa<div class="leia-tambem" markdown="1">
## Leia também:

- <a href="/visualizando-as-letras-do-bob-dylan">Visualizando as letras do Bob Dylan</a>
- <a href="/visualizando-letras-de-musica-como-networks">Visualizando letras de música como networks</a>
- <a href="/analise-de-um-forum-de-ead">Análise de um Fórum de EAD</a>
</div>