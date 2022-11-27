# ***Saúde e Saneamento no Brasil - Mendonça e Motta***

- ***Objetivo:*** demonstrar que a redução da mortalidade infantil associada às doenças de veiculação hídrica foi alcançada com a melhoria na cobertura dos serviços de saneamento e também devido ao acesso aos serviços de educação e saúde.
	- ***Método:*** modelo de estrutura epidemiológica
	- ***Objetivo auxiliar***: Estimar, para cada tipo de serviço, o custo médio de salvar uma vida.

- ***Fonte de dados:***
	- ***Datasus*** para os dados relacionados ao número de casos associados à mortalidade, morbidade e número de leitos.
	- ***Sistema de Informações sobre Mortalidade (SIM)*** para a taxa de mortalidade.
	- ***Censos Geográficos 1980 - 2000 (IBGE)***  para os dados referentes à população.
	- ***Pesquisa Nacional por Amostra de Domicílios (PNAD) + Ipeadata*** para as variáveis de saneamento e as variáveis socioeconômicas
	- ***Secretaria do Tesouro Nacional (STN) + Ministério da Fazenda (MF)*** para os gastos estaduais de saúde.

## ***Fichamento***

> A literatura sobre saúde indica claramente que a falta de condições adequadas de saneamento no que se refere a água e esgotamento sanitário é uma das principais causas da mortalidade na infância.

>O objetivo deste estudo é estimar um modelo econométrico utilizando técnicas de painel que correlaciona indicadores de saúde com indicadores de saneamento para o período 1981-2001. Um procedimento clássico para a análise desse tipo de problema deriva do uso da chamada <mark style="background: #ABF7F7A6;">função “dose-resposta”</mark> , que ***permite obter uma relação entre os casos de mortalidade e as condições de saneamento.***

> Assim, controlando por outros determinantes, ***poderemos comparar os gastos preventivos com os gastos em saneamento para uma redução equivalente na incidência de doenças de veiculação hídrica.***

### ***Diferenciais deste artigo:***

> 1. Desenvolver uma análise extensiva com base no modelo de dados de painel para os estados brasileiros; ***a metodologia de dados em painel permite considerar de modo mais eficiente o efeito específico dos estados nas variáveis não observadas;***
> 2. Ao cobrir um longo período, de 1981 a 2001, o presente estudo contempla inúmeras mudanças nas políticas de saúde e saneamento
> 3. Permite comparar o custo efetividade da provisão adequada dos serviços de saneamento em relação à provisão dos serviços de educação e saúde, os quais igualmente afetam a taxa de mortalidade infantil.

### ***Achados da Análise Exploratória de Dados:***

- Ele apresenta os dados da análise exploratória como tabelas. Trazer como gráficos.
- ***Tabela 01:*** Brasil – cobertura de serviços de saneamento (1970-2000) (Em % total da população)
	- *"A evolução da cobertura dos serviços de saneamento no Brasil desde os anos 1970 foi significativa... Nos últimos 30 anos estenderam-se os serviços de água a 90% da população urbana, equivalente a mais de 30 milhões de domicílios. Na coleta de esgoto triplicou-se a cobertura para 56%, cobrindo quase 20 milhões de famílias."*
	- *"O país, entretanto, é ainda incipiente, em termos internacionais, no tratamento de esgoto. E nas áreas rurais a cobertura continua muito pequena, tal como mostram os dados da tabela 1."*
- ***Tabela 02:*** Brasil – cobertura de serviços de saneamento por classe de renda (2000) (Em % total de domicílios)
	- *"A despeito de todo esse crescimento na cobertura dos serviços de água, o acesso das camadas mais pobres da população é ainda muito abaixo daquele usufruído pelos mais ricos."*
	- Um ponto importante é que o autor diz, na frase abaixo, que a diferença chega a quase 100%. Isso é só uma forma de dizer que a diferença de cobertura entre as classes dobra.
		- *"A tabela 2 mostra que as famílias com renda acima de 10 salários mínimos (SMs) têm cobertura de água 50% maior, enquanto no caso da coleta de esgoto a diferença chega a quase 100%."*

> A comparação do número de casos de mortes por idade no tempo deve considerar a evolução da distribuição etária da população, pois se uma doença recai sobre uma faixa de idade específica e a distribuição etária se altera ao longo do período, apenas a normalização pelo total de habitantes para cada faixa levará a análise comparativa naturalmente a um resultado distorcido. <mark style="background: #ABF7F7A6;">Para tal, se utiliza a técnica de padronização da população, que consiste em corrigir o indicador pela razão entre os percentuais da população para certa faixa etária referentes a dois períodos distintos.</mark> 

- ***Tabela 03:*** evolução da *taxa padronizada* de mortalidade por doenças relacionadas à falta de condições adequadas de saneamento por região
	- Esta tabela é bem densa e acredito que explicar essa técnica de padronizar a idade é interessante.
		- [Referência](http://cc04-10.med.up.pt/Epidemiologiapraticas/Aula3_Nova.pdf) A técnica de padronizar a taxa de mortalidade serve ao propósito de manter comparáveis populações de diferentes grandezas. No artigo ele não específica qual tipo de padronização utilizou, mas a dinâmica básica pode ser lida na referência.
	- *"De 1980 a 1990, houve uma redução de mais de 50% na taxa de mortalidade; enquanto no período 1990-2000, a redução chegou perto de 80%."*
	- *"No que se refere aos idosos, o período 1980-1990 mostra um avanço na taxa de mortalidade, enquanto de 1990 a 2000 essa taxa decresce muito pouco nessa faixa etária. Somente a região Norte apresenta um efetivo declínio na mortalidade no período. Em relação às pessoas entre 15 e 64 anos, não houve variação na taxa no período 1980-1990, excetuando-se o caso da região Norte, que mostrou um declínio significativo desse indicador. De 1990 a 2000, a queda na mortalidade abrangeu também a região Nordeste, ficando a variação na taxa inalterada para as outras regiões do país."*

- ***Tabela 04:*** Correlação entre variáveis – dados agrupados (1981-2001)
	- Tentar reproduzir dados dessa tabela sem possuir acesso aos dados originais e fazê-la na forma de uma matriz de correlação.

### ***O Modelo Econométrico***

- ***Objetivo:*** e isolar a contribuição da melhoria de acesso a serviços de saneamento nas variações dos indicadores de mortalidade associada a doenças de veiculação hídrica.
	- Assim, seguindo a literatura sobre funções epidemiológicas para estimativas do custo econômico da saúde – vamos correlacionar a incidência de mortalidade com os indicadores de saneamento e os de outras variáveis que se supõe estarem relacionadas com a taxa de mortalidade, tais como os serviços de educação e saúde.

- Estrutura do modelo:
	- $$Y_{it} = \alpha + \beta S_{it} + \delta X_{it} + \underbrace{(a_i + u_{it})}_{\varepsilon_{it}}$$
		- Utilizaremos um ***estimador de efeitos fixos*** se $cov(a, X) = 0$. Caso contrário, utilizaremos um ***estimador de efeitos aleatórios***. 
		- $\alpha_i \sim (0, \sigma^2_\alpha)$ e $u_{it} \sim (0, \sigma^2_u)$
	- $Y$ é a taxa de mortalidade definida como a razão entre o número de casos de mortes pela população (população infantil).
	- $S$ representa o vetor de variáveis ligadas ao saneamento.
		- *"Utilizaremos aqui como variáveis representativas da escala de saneamento os percentuais da população atendida por condições adequadas de água (ÁGUA) e esgotamento sanitário (ESGOTO)"*
	- $X$ é o vetor de variáveis do modelo não associadas ao saneamento
		- *"As variáveis que permitem captar influências exógenas sobre a ocorrência de mortes não diretamente associadas ao saneamento seriam: escolaridade (ESCOL); taxa de urbanização (URB); gastos públicos com saúde (GSAUDE) e o número de leitos da rede hospitalar (LEITOS)."*
		- *"<mark style="background: #ABF7F7A6;">Sabe-se a partir dos estudos ligados a retorno em educação que existe uma forte relação entre renda e escolaridade</mark> (Sachsida; Loureiro; Mendonça, 2004) <mark style="background: #ABF7F7A6;">e que a existência de condições adequadas de saneamento está fortemente ligada à renda do indivíduo</mark> (Mendonça; Sachsida; loureiro, 2004). Logo essas variáveis representam indicadores de renda. Da mesma forma, gastos com saúde e número de leitos hospitalares vão aproximar-se de uma medida de renda dos estados."*
			- As variáveis de renda utilizadas, são:
				- *Escolaridade de mãe:* $\text{ESCOLM25}$
				- *Taxa de analfabetismo para mulheres >= 15 anos:* $\text{ANALFM15}$
		- ***Efeito escala:*** Quando uma variável parece ser bem mais relevante só porque está em uma unidade de medida diferente que outra váriavel.
			- Um ponto interessante é que os autores decidem entrar com as variáveis de gastos de saúde e leitos com seu valor em nível. A justificativa disso é que isso minimizaria o ***efeito escala***. Isso aconteceria aqui porque a análise dos dados per capita mascararia a capacidade de atendimento distinta de dois municípios com tamanhos diferentes.
- Os autores fazem uma breve menção ao foto de que os grupos de variáveis altamente correlacionados (como água e escolaridade e água e urbanização) não serão utilizadas no mesmo modelo para evitar multicolinearidade.

### ***Resultados Econométricos***

- Como sempre, estimaram um MQO para usar como baseline. Além disso:

> ***A estimação por MQO permite também identificar multicolinearidade entre as variáveis explicativas a partir do emprego da estatística Variance Inflation Factor (VIF)***, que calcula o impacto sobre a variância de cada variável decorrente das correlações advindas da presença dos outros regressores (Judge et al., 1982).

*Sobre a presença do efeito fixo:* 

> Primeiro, a necessidade do uso de dados em painel para estimar o modelo é corroborada pelo teste de Breusch-Pagan, cuja hipótese nula de que a variância do componente individual seja igual a zero, assinala a heterogeneidade do efeito individual. ***Ver coluna 03*** 
> 
> O resultado desse teste indica claramente a presença de componente individual (*efeito fixo*) no modelo.
> 
> Segundo, *a presença do componente individual é também corroborado pelo valor do coeficiente RHO*, a proporção da variância estimada do componente individual em relação à variância estimada do distúrbio, que é alto tanto no modelo por efeitos aleatórios como por efeito fixo.

- ***Em qual caso o teste de Breusch-Pagan é utilizado?***

*Sobre o estimador:*

> Uma vez verificado que a metodologia de dados em painel é mais adequada que a estimação por MQO, a questão agora está na escolha da estimação por efeito aleatório ou fixo. Nesse caso, o teste de Hausman põe à prova a hipótese de correlação do efeito individual com os regressores. No caso de a hipótese nula ser verdadeira, isso assinala que a estimação do modelo por efeito aleatório não é um estimador consistente para o modelo. De acordo com o que se verifica na coluna (3) o teste de Hausman indica que o estimador de efeito fixo é o mais adequado para se estimar o modelo.

- Dados o parágrafo acima, a interpretação será feita em cima das colunas 04 e 05.

- ***Qual técnica de estimação de efeitos fixos eles utilizaram?***
- ***Para quê serve e como é feito o teste de Hausman?***

### ***Custo de Redução da Mortalidade***

- Algo legal desta parte do trabalho é que eles criam uma tabela contendo a interpretação de cada coeficiente. Gostei bastante

### ***Críticas***

- Os autores não reportaram os graus de liberdade .
