# Processamento de imagem

## Aula 1 - 07/03/23 - 1/4 - [14h06, 14h56] - Não teve por poucos alunos

## Aula 2 - 09/03/23 - 2/4 - [14h10, 16h10]

### Processamento de imagens

Computação Gráfica VS Computação visual

Grandes áreas da computação gráfica: Análise de imagens X Síntese de Imagens X Processamento de imagens

Síntese: Criar imagens
Análise:
Processamento:

<!-- GIF de clustering -->
<!-- GIF de neurônios processando quais números foram manuscritos -->

### Imagem digital

- A imagem é representada em uma região discreta.
- Conjuntos de tuplas RGB definem os pontos
- Pode ser Uni, bi ou tri dimensional -> Um único pixel, uma imagem, um voxel
- Binária, monocromática, multibanda ou colorida -> Preto e branco; Escalas de cinza; RGB
- Vetorial ou matricial (SVG vs Raster)

### Off-topic

Leandro foi pro IMPA e agora tá em Coimbra
Rivera queria ir para a Inglaterra ou Canadá, mas deixaram ele na fila de espera. No Brasil logo aceitaram ele na PUC. Ele também passou pro sul, mas teria que esperar dois meses para começar a receber bolsa, então ele foi pra PUC.
Drones que percorrem a selva para analisar bichinhos através de padrões.
Câmeras em sala de aula para identificar o comportamento dos alunos
Análise de imagens é que nem uma aeromoça passar na frente de uma turbina de avião. Entra uma coisa e sai outra coisa.
Geraldo faleceu há pouco tempo. Era um bom matemático
Em 2015 fizeram um projeto financiado para analisar as assinaturas por diversos métodos diferentes
Na época em que ele fazia faculdade não havia tira teima de jogo de futebol. O Globo financiou. Se mapeia o jogo e coloca sobre um mapa pré desenhado. Isso em 1998. Não sabe se atualmente continua sendo do trabalho que ele fez só que aprimorado ou se é algo novo.
Todo mundo está abrindo a porta, o que será que está acontecendo? Procurando algum ladrãozinho?

### Relação entre áreas

Mineração em banco de dados X visão computacional X IA

<!-- Imagem grandona -->

### Sistemas de imagens digitais

#### Processamento de imagens - PI

- Manipulação de imagens
- Refere-se aos dados de entrada, e também os de saída
- Rearranjo dos pontos/pixels da imagem
- Exemplo: Redução de ruído, realce de imagem, restauração de imagens, etc.

Para detectar ruído, precisa-se de alguma heurística para determinar os padrões.

#### Análise de imagens - AI

- Interpretação de informações da imagem através de algoritmos computacionais
- Tomam imagens como entradas, mas produzem outros tipos de saída
- Obter parâmetros descritivos da imagem
- Usada para realização de reconhecimento de padrões, visão computacional ou de extração de conhecimento das imagens (Mineração de imagens)

#### Síntese de imagens - SI

- Criação de imagens por computador
- Transforma dados em imagens, que podem ser consideradas na forma vetorial ou matricial como as iamgens médicas de ressonância magnética, ultrassom e tomografias.
- Pode usar técnicas de AI que inserem objetos reais e modelos de textura nos objetos e cenas geradas

#### Visão computacional - VC

- Extração de informações de imagens (AI) e identificação e classificação de objetos nesta imagem.
- Aplicações: reconhecimento de pessoas , de assinaturas e de objetos; inspeção de peças em linhas de monstagem; orientação de movimentos de robôs em indústrias automatizadas; etc.
- Utiliza AI e IA (ou técnicas de tomada de decisão).

## Aula 3 - 14/03/23 - 2/4 - [14h20, 15h38]

### Visão computacional (slide)

#### Etapas de um Sistema de Visão computacional (Pattern Recognition)

Análise qualitativa:
    Aquisição/Digitalização
    -(pixels)->
    Restauração/Realce
    -(Pixels)->
    Segmentação
    ->
    Grupos de Pixels
Análise quantitativa:
    Grupos de Pixels
    Extração de atributos/características ->
    -(Dados)->
    Classificação/Reconhecimento
    -(Grupos de dados)->
    Decisão

Diferença entre quantização e segmentação: (ele explicou mas eu tava tentando fazer o diagrama)

A diferença é:

Segmentação: separar regiões da imagem que apresentem características em comum para dar uma amenizada na quantidade de informações de alguma forma.
Quantização: Redução da gama de cores disponíveis para apenas um determinado valor em um intervalo de 0 a 255.

#### Aquisição de imagens

A aquisição de imagens se dá através da conversão da cena real (3D) em uma imagem (2D), sendo essa a função da câmera.

- Imagem
  - Energia luminosa distribuída numa posição espacial, podendo ela ser dada por $R+T+A=1$, onde:
    - $A$: Absorvida
    - $T$: Transmitida
    - $R$: Refletida
  - Pontos (x, y) da imagem com itensidade é dado por $intensidade(x, y) = I(x, y) * R(x, y)$, onde:
    - $I$: Iluminação
    - $R$: Refletância
  - Pontos que definem a imagem:
    - Discreto: amostragem ou quantização
    - Resolução: maior ou menor

#### Amostragem e quantização

- Amostragem
  - Pelo que entendi, diferente da amostragem da estatística que pega um conjunto de dados aleatoriamente, nesse caso ele meio que cria parcelas de pixels próximos e cria meio que uma média delas.
  - Dá para fazer isso em situações de maior curvatura (observando a derivada), e criando segmentos mais largos quando a variabilidade for baixa e segmentos mais finos quando a variedade é grande.
- Quantização
  - Definição da quantidade de níveis de tons atribuídos a cada ponto
- Imagens reais apresentam númeors ilimitados de cores e tons
- Imagens computacionais
  - Limitado nível de cores ou tons
  - Um pixel seria uma amostra de uma quantização

#### Resolução

Quanto maior a resolução, maior o número de pixels. Geralmente associado à uma boa qualidade de imagem, entretanto, também significando um maior número de informações.

#### Quantização

A variação da gradação tonal afeta a qualidade da imagem.
Haver grande resolução e gradação tonal permite imagem nítida.

A quantização acontece da seguinte forma:
primeiro pega todos os 256 níveis de cinza
depois conta quantos pixels de cada nível existem
pega os 16 com maior quantidade e então esses englobam os outros pontos.

#### Realce e restauração

- Operações básicas em processamento de imagens
  - Realce
    - Destacar detalhes da imagem como contorno
  - Restauração
    - Destaque de segmentos deteriorados
    - Compensa deficiências na aquisição
    - Busca modelo formal (matemático) para restaurar

Paramos aqui

## Aula 4 - 16/03/23 - 1/4 - [14h27, 16h01]

### OffTopic

Fernando Linhares é sobrinho de Pedro Linhares, que era da primeira turma
Outro que também era da primeira turma é o Élisson

### Visão computacional (slide) (2)

#### Segmentação

- Isolar regiões de pontos da imagem pertencentes a objetos para posterior extração de atributos e cálculos de parâmetros descritivos

Operação: limiarização ou separação por tom do corte.
limiarização: conseguir definir os limites
Exemplo: objeto e fundo, através da limiarização binária (thresholding) 0 e 1

##### Processo de segmentação

Algoritmo:

Para cada pixel, se a escala de cinza de um pixel é menor que o limiar, converte para preto, senão, pra preto.

Como determinar valor de limiar? "Várias formas"

Uma delas seria fazer um histograma das escalas de cinza, traçar um gráfico e selecionar algum dos vales que trace uma boa divisão entre a quantidade de brancos e pretos

Vetor de histograma (VU) é usado para definir o limiar.

Pode-se usar o vetor de histograma para usar o método de tsu (ou tzu).

Análise de profundidade: vai varrendo características em comum para tentar alcançar algum tipo específico de resultado.

#### Extração de atributos ou Características

A partir de imagens já segmentadas ou binárias, busca obter dados relevantes ou atributos das regiões ou objetos destacados.
Exemplos:

- Número de objetos
- Dimensões - Medidas X e Y
- Geometria
- Propriedades de luminosidade e textura
  - Cores
  - Nível de intensidade médio
    - Distribuição tonal
    - Histograma dos canais da imagem
  - Desvio padrão de cada banda da região
  - Outros momentos estatísticos: formas de definir onde estão as concentrações de dados

Uma forma de analisar assinaturas seria fazer um histograma de quantos pretos e brancos, (ou quantas trocas de preto pra branco e de branco pra preto) existem em cada uma das colunas e linhas.

Outra forma seria calcular o centro de massa

##### Momentos invariantes

Se fizermos espelho, translação, escala e rotação, o momento estatístico se mantém.

Calcula-se através de Momentos de Hu. Que são momentos estatísticos. Resultando em 7 valores diferentes

Um aluno da primeira turma usou isto para fazer uma rede neural de entendimento dos gestos de mão para interagir com um jogo.

Geometria projetiva: considerando um espaço máximo e mínimo de movimentação da mão, dá para definir o espaço por onde o cursor pode passar como uma interpolação da escala da mão

Usando a normalização ele conseguiu lidar bem com os valores

FIM DA AULA

## Aula 5 - 21/03/23 - 1/4 - [14h24, 15h59]

### Offtopic

Mulheres têm mais hormônios e sentem muita coisa, "agora, voltando aos juízes", elas têm os fatores que afetam a percepção, que podem fazer com que tomem decisões erradas.

### Visão computacional (slide) (3)

#### Classificação e reconhecimento

- Distinguir objetos na imagem agrupando parâmetros de acordo com sua semelhança para cada região de pixels encontrada.
- Objetos
  - Como sendo do mesmo grupo classificados em uma base de imagens
  - Novos apresentados para o sistema reconhece com parando com as estabelecidas previamente

Machine-Learning pode ser por treino supervisionado ou não-supervisionado

Supervisionado tem diversos atributos e seus respectivos valores. Já o não-supervisionado não apresenta os valores

Algoritmos:

- ANN - Artificial Neuron Network
- HMM - Hidden Markov Model
- SVM - Support Virtual Machine
- FR - Random Forest
- Deep Learning
  - Convolução: A multiplicação de uma matriz de valores por outra matriz de valores.

Alguns algoritmos permitem o processo reverso de conversão de vetores descritores para imagens de volta. Outros não.

#### Decisão

- Tomar decisões usando extração de informaçõs do mundo real através de imagens
- A tomada de decisão a partir dos parâmetros extraídos dos objetos
  - Indagação trivial
  - Algoritmos mais complexos de IA
  - Conferir informações de banco de dados

#### Visão humana X Computacional

Cena -> Olho -> Cérebro (Conhecimento)

Fatores que afetam a visão: posição e fadiga

Entrada: Cena e olho
Processamento e armazenamento: Olho e cérebro

#### Características

- Adaptabilidade
  - Se ajusta às operações de acordo com os parâmetros
    - Humano: dar uma segunda olhada
    - Visão computacional: rígida
- Tomada de decisão
  - Avaliação prévia e análise dos parâmetros
    - Humano: interpretação pode variar de um olhar para outra
    - Visão computacional: de acordo com as informações
- Qualidade das medições
  - De acordo com a consistência dos resultados
    - Humano: limitações de medir as variações e tonalidades
    - Visão computacional: alto poder de medição
- Velocidade de Resposta
  - Dependendo das informações, a visão computacional pode ser maior que do humano
- Percepção dos Espectros
  - Humano só percebe espectro de luz visível
  - Visão computacional pode perceber outros níveis de luz
- Dimensão dos Objetos
  - Humano percebe a distância, 3D, etc.
  - Visão computacional é deficiente em distância e 3D (visão estéreo)

#### Imagem Digital

- Origens
  - Do latim imago - Representação visual de um objeto
  - Do grego eitos - a ideia da coisa
    - Platão (idealismo): ideia (projeção na mente) da coisa
    - Aristóteles (realismo): representação mental dos objetos reais
- Imagem pode ser adquirida ou gerada pelo ser humano
  - Artística, fotomecânico, ...
- Uma imagem consistee em qualquer forma visual de expressão de uma ideia
  - Origens diversas
    - Radiação eletromagnética (câmera)
    - Ondas sonoras de alta frequência (ultra-som)

- Imagem digital
  - Formatação de sua representação para serem manipulados por rpocessadores
  - Digitalização: Imagem contínua (real) -> Imagem discreta (digital)
  - Reconstrução: Imagem discreta -> Imagem contínua (aproximada)
  - Codificação: Transformação em formato apropriado para seu uso
  - Decodificação: Inversa de codificação (perda ou sem perda de informação)

## Aula 6 - 23/03/23 - 0/4 - Faltei pra fazer prova da Daedalus

## Aula 7 - 28/03/23 - 1/4 - [14h31, 15h53] - Cheguei atrasado

### Offtopic 7

- "Eu quando era estudante, era político"
- "Um cara barbudo como jesus cristo, era suíço, fumava duas caixas por dia"
- Filosofia matemática

### FPI3 - Visão computacional (slide 4)

#### Imagem Digital (2)

Técnica de difusão:

$$
[a][b]
[a][a1][b1][b]

leopold kronecker

[a][b]
[c][d]
=
[aa][ab][ab][bb]
[ac][ad][cb][db]
[ac][bc][ad][bd]
[cc][dc][cd][dd]
$$

#### Reconstrução da imagem (2)

<!-- Imagens e gráficos -->

Quantização por interpolação:

- Vizinho mais próximo
- Linear (bilinear)
- Bi-cúbica

#### Amostragem e quantificação

- Uma imagem difital é descrita por uma matriz NxM de valores de pixel (p(x,y)) inteiros positivos, que indica a intensidade de cor em cada posição [x,y] da imagem

#### Resolução Espacial

Imagem digitalizada tem um tamanho adimentsional, em pixels.
Tamanho da amostragem (r: resolução)
r=p/m
Razão entre o número de pixels (p) e o tamanho da imagem real (m) no filme fotográfico ou equivalente.

p = r*m

Resolução espacial é medida em pontos por polegada ou dpi (dots per inch)

#### Aliasing

Ocorre quando a frequência de amostragem é inferior à maior frequência de variação da função contínua

<!-- imagens -->

Solução aproximada: superamostragem

#### Imagens monocromáticas

São imagens digitais onde cada pixel possui apenas uma banda espectral
Binárias: 0 ou 1
Escala cinza (depende de bits)
1 bit -> preto e branco (0,1)
variações (2, 3, 4, ... 8 bits) 2^bits tons

Pode ser representada geometricamente também por valores reais quanto à posição dos pixels como no gráfico G(f) da função f:

G(f): {(x,y,z); (x,y) \in U; z = f(x,y)}

Dá para estimar profundidade de imagens de acordo com a análise da imagem 2D.

#### Imagens coloridas

São imagens digitais onde cada pixel possui n bandas espectrais.

Três bandas visíveis (RGB) tem-se uma imagem colorida aos olhos humanos.

#### Histograma de imagem digital

Um conjunto de números indicando o percentual de pixels na imagem que representa um determinado nível de cinza ou cor

<!-- Imagens -->

Fornece uma indicação de sua qualidade quanto ao nível de contraste e quanto ao seu brilho médio

Alto contraste: distribui mais igualmente as cores
Baixo contraste: reduz a gama de cores, tornado elas mais centralizadas
Alta luminosidade: arrasta as cores mais para o branco
Baixa luminosidade: arrasta as cores mais para o preto

## Aula 8 - 30/03/23 - 1/4 - [14h45, 16h04] - OpenCV

### Offtopic 8

- A tela multitouch fazia a mudança dos rabiscos lentamente em python, mas rapidamente em C.
- Parece o dedo do Deus: fininho
- Jonas e Luis Velho foram convidados para O Globo
  - Nessa época Globeleza não existia ainda.

### FPI3 - Visão computacional (slide 4) - Aula 8

#### Sistema de visão binária

<!-- Imagem em tons de cinza -->
<!-- Imagem binária -->

- Agrupamento por limiar (limiarização)
  - Objeto de tonalidade bem diferente do funda da imagem
    - Impor um limiar entre as duas tonalidades
    - Fundamental o ponto de corte

- O limiar nem sempre é facilmente determinado
  - Objetos bem diferenciados (separados por vales)
  - Objetos não bem diferenciadas (perda de informação)
  - Limiarização multinível (multilevel thresholding)

#### Processo de limiarização

- Imagem f - original
  - f(x,y) de N níveis de cinza
- Imagem g - Limiarizada ou posteriorizada
  - f(x,y) de M ( $\less$N ) níveis de cinza

No limite, g(x,y), terá só dois níveis de cinza, como na equação:

g(x,y) = {
  {R_1 se f(x,y) <= T}
  {R_2 se f(x,y) > T}
}

- R_1 e R_2: valores estipulados (0 e 255) imagem binarizada
- T: tom de cinza definido por limiar
  - T = T[x, y, p(x,y), f(x,y)]
  - p(x,y) propriedade local de x,y

<!-- Fim -->

## Aula 9 - 04/04/23 - 1/4 - [14h21, 15h58]

### FPI3 - Visão computacional (slide 4) - Aula 9

#### Algoritmo de Otsu

- Método de thresholding global: melhor constante $k$
- Histograma com função densidade de probabilidade
  - $Pr(r_q)=n_q/n$ para $q=0,1,2,...,L-1$; sendo $L \leq 256$
  - Onde:
    - $n$:    Total de pixels da imagem
    - $n_q$:  Total de pixels de intensidade $r_q$
    - $L$:    Total de níveis de intensidades na imagem
  - Escolhe-se valor de $k$, tal que maximiza a variância
    - $\sigma^2 = \omega_{0} (\mu_{0} -\mu_{r})^2 + \omega_{1} (\mu_{1} -\mu_{r})^2$
    - Sendo:

$$\omega_{0} = \sum_{q=0}^{k-1} Pr(r_q)$$
$$\omega_{1} = \sum_{q=k}^{L-1} Pr(r_q)$$
$$\mu_{0} =    \sum_{q=0}^{k-1} \frac{q*Pr(r_q)}{\omega_{0}}$$
$$\mu_{1} =    \sum_{q=k}^{L-1} \frac{q*Pr(r_q)}{\omega_{1}}$$
$$\mu_{r} =    \sum_{q=0}^{L-1} q*Pr(r_q)$$

##### Pseudocódigo

```c

int obter_melhor_k_Otsu() {
  int kk = var = 0;
  mu_T = calcular_Mu_T();
  for (0<k<L){
    mu_0 = calcular_mu_0(k)
    mu_1 = calcular_mu_1(k)
    omega_0 = calcular_omega_0(k)
    omega_1 = calcular_omega_1(k)

    vv = omega_0*(mu_0-mu_T)²+omega_1*(mu_1-mu_T)²
    if(var < vv) {
      var = vv;
      kk = k;
    }
  }
  return k;
}

```

##### Outras coisas

<!-- Imagens -->
<!-- Imagens -->

- Problema: selecionar valor de T de forma a gerar melhor segmentação
  - Geralmente envolve várias tentativas
- Limiarização multinível global (análise de valores da imagem)
  - Menos confiável do que limiarização adaptativa
- Algoritmo de valor fixo: $T_i$ escolhidos pelo programador
- Algoritmo automático: $T_i$ escolhidos em função de intensidades (histograma)

## Aula 10 - 06/04/23 - Feriado

## Aula 11 - 11/04/23 - 1/4 - [14h10, 15h56]

### FPI3 - Operações de imagens - Aula 11

#### Operações em imagens

- 3 tipos de operações nas imagens
  - Pontuais nos pixels
  - Em partes da imagem
  - Em toda a imagem
- Por área de processamento
  - Por imagem: quantização, histogramas, etc.
  - 2 imagens: operação binária
  - n imagens: detecção de contornos
- Tipos de operações
  - Binárias: aritméticas/booleanas
  - Geométricas
  - Convolução/linear/não linear/morfológica/...

#### Operações pontuais

O pixel na posição (xi, yi), da imagem resultante depende apenas do pixel na imagem original.

<!-- Imagens -->

- Ajuda cor ou luminância
- Brilho, contraste, saturação, limiarização, posterização, etc.

#### Operações binárias

- Aritméticas
  - Geralmente somando ou subtraindo

<!-- Imagens -->

- Booleanas: y, x, x e y, x ou y, x xou y, nao x ou y

#### Operações locais

- Um pixel da imagem resultante depende de uma vizinhança do mesmo pixel na imagem original

<!-- Imagem -->
Uso de um KERNEL ou máscara de convolução.

Exemplo: Operação local em uma área em torno do pixel (xi, yi).

Operações: Suavização (blur), realce (sharpen), detecção de bordas, etc.

Kernel é tipo serigrafia
O kernel é meio que colocar um 3x3 a um pixel e seus vizinhos, calcular a média dos produtos dos valores do pixel.

Exemplo:

f(1,1) (processar o 5)
[1|2|3]   [1|1|1] =
[4|5|6] * [1|1|1] = 1 x (1+2+3+4+5+6+7+8+9)/9 = novo valor do f(1,1)
[7|8|9]   [1|1|1] =

Exemplo: redução do ruído

<!-- Imagens -->

#### Operações globais

Um pixel da imagem resultante depende de um processamento realizado em todos os pixels da imagem original.

Operações que mudam domínio de descrição

- Transformadas de: Fourier, Wavelet, Hough
- Cosenos (usada para codificação)
- Funções interativas ou fractal

#### Deformações e Morphing

Deformação: mudança de posição da imagem a respeito de seus vértices e forma dos objetos envolventes como referência.
Morphing: deformação aliado à decomposição de suas cores.

##### Deformações

Regiões triangulares são simples de deformar

Coordenadas baricêntricas: um ponto v = c1v1 + c2*v2 + c3*v3
c1+c2+c3 = 1
c1, c2, c3 > 0, para v interior do triângulo

Transformação de V para @:

w1 = Mvi + b

Satisfaz w = c1w1 + c2w2 + c3w3, onde c1+c2+c3 = 1

###### Fazendo triangulações

Uma imagem em várias regiões triangulares e deformar cada região de uma maneira diferente

Formas de triangulação
Deformações permitidas e não permitidas

<!-- Imagem -->

## Aula 12 - 13/04/23 - 1/4 - [14h30, 16h03]

### Offtopic 12

- Rivera subtituiu "ceguinho" por "cego"
- Rivera que pediu a sala 101 e Annabell de u pra LCMat
- Professora Wilma também pediu sala
- Oscar também
- A geladeira de Annabell era de Sahúdy Rivera
- Estamos no melhor momento
- "A chefia tem que ser líder"
- Não vai ter prova

### FPI3 - Operações de imagens - Aula 12

#### Deformações dependentes do Tempo

- Conjunto de deformações geradas quando os pontos de vértice da imagem inicial são movidos continuamente ao longo do tempo desde suas posições originais até posições originais até posições finais especificadas.

Movimento em reta (combinação convexa)

$u_i(t) = (1-t)v_i + tw_i$

Movimento em curva

#### Morphing

O termo *morph* tem como origem a palavra grega *morphos* que significa forma, sendo a ciência que estuda as formas chamada de Morgologia. *Morphing* é uma redução da palavra *metamorfose*.

- Envolve dois tipos de transformação
  - de deformação (warping)
    - Mapeamento de vértices
  - de tons (cross-dissolve ou decomposição cruzada)
    - Cores são interpoladas entre origem (o) e destino (d)
      - Intermediarias
        - r_novo = (r_origem + r_destino)/2
        - g_novo = (g_origem + g_destino)/2
        - b_novo = (b_origem + b_destino)/2

##### Transformação de *pixels* origem em destino

<!-- Imagem -->

### FPI4 - Filtros de imagens - Aula 12

#### Filtragem em imagens

- Filtros são usados para melhorar a qualidade das imagens
  - Ampliação de seu contraste
  - Eliminação de padrões periódicos ou aleatórios
  - Foco e acentuação de características
- Classificação
  - Domínio ou espaço em que atuam: da frequência ou espacial.
  - Tipo de frequência: filtros que permitem passar determinada gama de frequências. Como por exemplo permitindo passar apenas baixas frequências, altas frequências.
  - Linearidade: lineares ou inversíveis ou não lineares
  - Tipo de aplicação: suavização; constraste; adaptativos; globais; janelados; ou, locais.

#### Filtragem no domínio da frequência

1. A imagem é transformada do domínio espacial para o da frequência (transformada de Fourier)
2. Operações de filtragem são realizadas nessa imagem
3. Realiza-se o processo inverso, onde a imagem no domínio da frequência é transformada para o domínio espacial

Imagem (f(x,y)) -> Transformação -> Processamento -> Transformação-inversa -> Imagem (g(x,y))

Transformada de Fourier é converter imagens em suas ondas

#### Domínio da Frequência

<!-- Imagens -->

## Aula 13 - 18/04/23 - 1/4 - [14h23, ...]

### Offtopic 13

- "onde posso pegar uma buceta para uenf?"
- Pinga significa "pene" no peru
- Troca é puteiro
- Aí o gatinho está só 'Meow 😿'

### FPI4 - Filtros de imagens - Aula 13

#### Domínio da frequência

- Sinal no domínio espacial é a soma de faces de senos variados
- Cada componente contribui na imagem

<!-- Imagem -->

#### Transformada de Fourier

Dada a função contínua $f: \real \rightarrow \real$, a transformada de Fourier de $f$ é:

$$
F(u) = \int^{\infty}_{-\infty} f(x) e^{-j 2 \pi u x} dx
$$

onde $j = \sqrt{-1}$ e $u$ é frequência

$$
F(u) = \int^{\infty}_{-\infty} f(x) \left[\cos(2 \pi u x) - j \sin(2 \pi u x)\right] dx
$$

A transformada inversa de Fourier:

$$
F(x) = \int^{\infty}_{-\infty} f(u) e^{j 2 \pi u x} du
$$

$$
F(x) = \int^{\infty}_{-\infty} f(u) \left[\cos(2 \pi u x) + j \sin(2 \pi u x)\right] du
$$

<!-- Imagens -->

A transformada de Fourier de uma função é uma função complexa:

$F(u) = R(u) + j I(u)$

com a forma exponencial tem-se $F(u) = |F(U)| e^{j\theta (u)}$

- Espectro de Fourier (amplitude ou magnitude): $|F(u)| = \left[ R²(u) + I²(u) \right]^{1/2}$
- ângulo de fase da função: $\phi(u) = \tan^{-1} \left[ I(u)/R(u) \right]  $

#### Transformação Discreta de Fourier (DFT - Discrete Fourier Transform)

<!-- Imagem -->

$$
F(u) = \sum_{0 \leq x \leq N-1} f(x) \left[ \cos(2\pi u x /N) - j \sin(2\pi ux/N) \right], 0 \leq u \leq N-1
$$

$$
F(x) = \frac{1}{N} \sum_{0 \leq u \leq N-1} f(u) \left[ \cos(2\pi u x /N) - j \sin(2\pi ux/N) \right], 0 \leq x \leq N-1
$$

## Aula 14 - 20/04/23 - 1/4 - [14h34, 15h58] - próxima

### Offtopic 14

- "Se for imagem, é o quanto brilha. Se for um som é o *Rivera geme*"
- Tenho um miau *meow🐈* mas quero transformar para que seja como de um dinossauro **MEOW!🦖**
- Maria Betânia cantou a abertura de Pantanal

### FPI4 - Filtros de imagens - Aula 14

#### Transformada de Fourier para uma função bidimensional

Transformada de Fourier para uma função bidimensional:

$$
F(u,v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{ \left[ -j2\pi (ux+vy) \right] } dx dy
\\
F(u,v) = \frac{1}{NM} \sum_{X=0}^{M-1} \sum_{Y=0}^{N-1} F(x,y) e^{ \left[ -j2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right) \right] }
$$
$$
F(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(u,v) e^{ \left[ j2\pi (ux+vy) \right] } du dv
\\
F(x,y) = \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{ \left[ j2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right) \right] }
$$

Espectro e ângulo de fase:

$$
|F(u,v)| = \left[ R^2*(u,v) + I^2(u,v) \right]^{1/2}
$$
$$
\phi(u,v) = \tan^{-1} \left[ I(u,v) / R(u,v) \right]
$$

#### Processamento de imagens no domínio de Fourier

- Transformação da imagem $I(x,y)$ para o **domínio de Fourier** $F(u,v)$
- $F(u,v)$ é convoluída com o filtro $H(u,v) \rightarrow F(u,v)*H(u,v)$
- Ao produto $F(u,v) H(u,v)$ é aplicada a inversa da transformada de Fourier para retornar ao domínio espacial, onde se tem a imagem processada $I'(x,y)$.

Imagem I(x,y) -> DFT (FFT) -> (X) -F(u,v)H(u,v)-> (DFT)^{-1} -> Imagem processada I'(x,y)
Filtro H(u,v) -> (X)

$$
F(u,v)*H(u,v) = \frac{1}{NM} \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} F(m,n) H(u-m, v-m)

$$

## Aula 15 - 25/04/23 - 1/4 - [....., .....] - próxima

### Offtopic (15)

- Não querem comer minha irmã, né? [...] de tristeza, né, cara?
- "lati e corri para gravar"

### FPI4 - Filtros de imagens - Aula 15

#### Filtros e espectro de Fourier

- Informação no domínio de Fourier
  - Determinar um filtro apropriado
- Energia da imagem
  - Baixas frequências concentradas no centro
  - Altas frequências afastadas do centro

<!-- Imagens -->

##### Filtragem passa baixa

- Corrigir de detalhes da imagem que geram altas frequências
  - Bordas e transições abruptas
- Filtro passa baixa
  - Imagem menos nítida ou suavizada
  - Remoção de altas frequências

<!-- Imagens -->

$$
H(u, v) =
\begin{cases}
  1 se u^2+v^2 < r^2 \\
  0 se u^2+v^2 \geq r^2
\end{cases}
$$

##### Filtragem passa Alta

> Os componentes de alta frequência da transformada de Fourier não são alterados, enquanto os de baixa frequência são removidos.

- Os detalhes finos da imagem são enfatizados

<!-- Imagens -->

$$
H(u, v) =
\begin{cases}
  1 se u^2+v^2 \geq r^2 \\
  0 se u^2+v^2 < r^2
\end{cases}
$$

##### Outros filtros no domínio de frequência

<!-- Imagens -->

- Espectro de Fourier da Imagem
- Resultado da filtragem utilizando filtro circular não centrado na origem

- Espectro de Fourier da Imagem
- Filtragem utilizando filtro setor angular

#### Imagens de impressão digital no domínio Fourier

- No espectro de Fourier de uma impressão digital
  - Acúmulo de energia em torno de um anel
  - As cristas se comportam como senóides

- Nos espectros de Fourier, de partes desta imagem, aparecem dois picos de intensidade simétricos, em relação à origem.

#### Filtro de Gabor

- Filtro linear bi-dimensional e não variante ao deslocamento.
- Pode ser entendido como o produto de uma função gaussiana, simétrica em relação à origem e uma função cossenoidal.
<!-- Imagem -->
- Aplicações
  - Segmentação de imagens
  - Reconhecimento de faces
  - Reconhecimento de assinaturas
  - Melhoria e identificação de impressões digitais

<!-- Equação -->
$$
G(x,y,f,\theta,\sigma)=
e^{
  - \frac{1}{2}
  \left(
    \frac{x^2_\theta}{\sigma^2_x}
    +
    \frac{y^2_\theta}{\sigma^2_y}
  \right)
}
e^{2 \pi j f x_{\theta}}
$$

Onde:

- $x_\theta = x \cos\theta + y\sin\theta$
- $y_\theta = -x \sin\theta + y\cos\theta$
- $x, y$ são as coordenadas espaciais da imagem, $j = \sqrt{-1}$

Parâmetros:

1. $f$ é a frequência da onda no plano senoidal
2. $\theta$ é a orientação do filtro
3. $\sigma = (\sigma_{x}, \sigma_{y})$ é o desvio padrão da função gaussiana ao longo dos eixos $x$ e $y$, respectivamente.

#### Filtro decomposto em componentes reais e imaginários

<!-- Mais equações -->

Filtro passa banda: G = Fourier(W) * Fourier(V)

Realça as senoides com frequências em torno de f, suprimindo seus ruídos.

## Aula 16 - 27/04/23 - 1/4 - [....., .....] - próxima
