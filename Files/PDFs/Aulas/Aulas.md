# Slides

## Slide 1 - Fundamentos de Pocessamento de Imagens

## Slide 2 - Visão Computacional

## Slide 3 - Operações em Imagens

## Slide 4 - Filtros de Imagens

### Slide 5 - Extração de Características

- Sistema de análise de imagens
- Reconhecimento de elementos e objetos
- Parâmetros quantificáveis
- Cor, posição, orientação, dimensões, textura, etc.

<!-- Imagem -->

---

Etapas de um sistema de reconhecimento de padrões

[Imagem] ->
[Segmentação: Separa objeto ou padrão] ->
[Caracterização] -> [A]
[(BD de Padrões)] -> [A]
[A] ->
[Classificador] ->
[Reconhece o padrão]

#### Segmentação (19)

- Divisão da imagem em regiões que possuem o mesmo conteúdo no contexto de uma aplicação.
- A segmentação baseada em
- Descontinuidades
- Mudanças bruscas de tons
- Similaridades
- Aspectos comuns com limiar
- Limites ou bordas
- Áreas ou regiões

<!-- Imagem -->
<!-- Imagem -->

##### Segmentação baseada em regiões

Partição da imagem baseada no conteúdos de grupos de pixels.

- Premissas:
  1. Homogeneidade da região (com tolerância)
  2. Regiões delimitadas por fronteiras contínuas
  3. Pontos que correspondem a uma única região
  4. O conjunto de todas as regiões deve formar a imagem
- Técnicas:
- Segmentação por crescimento de regiões
- Segmentação por divisão e fusão de regiões
- Segmentação por clusterização
- Segmentação por janelas (windows)

##### Segmentação por crescimento de regiões

- Iniciar a partir de um pixel ou um conjunto de *pixels* (denominado de "semente").
- Para cada semente avalia-se o predicado dos *pixels* vizinhos
- Ex. cor RGB com menos de 5% da variação de 5 *pixels* vizinhos
- A agregação das regiões é feita quando o critério de similaridade ou de decisão do predicado for verdadeiro.
- Critério de parada bem definido

<!-- Imagem -->

##### Segmentação por divisão e fusão de regiões

- Subdivide uma imagem em quadtree
- Verificar se os pixels atendem a algum critério de homogeneidade.
- Os blocos que atenderem ao critério não serão mais divididos.
- O bloco que não atender será subdividido em blocos menores.
- Realiza a junção dos blocos vizinhos homogêneos.

<!-- Imagem -->
<!-- Imagem -->
<!-- Imagem -->

##### Segmentação por "Clusterização"

-|$X_1, X_2, \dots, X_n$|-> [A]
-|Parâmetros|-> [A]
[A] -> C_1(X_4, X_7, ..., X32)
[A] -> C_2(X_10, X_23, ..., X66)
...
[A] -> C_k(X_2, X_55, ..., Xn)

[A]= [Algoritmo de Clusterização]

<!-- Imagem -->

#### Algoritmo K- Means

- Algoritmo de classificação não- supersionada.
- O critério a ser minimizado é definido em função da distância dos elementos em relação aos centros dos agrupamentos.
- Usualmente, a métrica é a distância Euclidiana.
- Quanto menor for este valor, mais homogêneos serão os objetos dentro de cada grupo e melhor será a partição.

---

```mermaid
(Kmeans (X, k)) --
[Select the k initial centers - {ci = Random(X)}_{i=1,...,k}] --
[Copy ci → cci, ∀𝑖 = 1, ..., 𝑘] --
[Clusters gerator with center cci - ∀𝑥 ∈ 𝑋 𝑖𝑛 𝐶1, … , 𝐶𝑘] --
[Re-compute clusters center - 𝑐𝑖 = 𝑀𝑒𝑎𝑛 𝐶𝑖 i=1, ..., k] --
[Varies = Compare (ci, cci)] -->
{Varies} -|Y|-> [Copy]
{Varies} -|N|-> (Solution)
(Solution {C_1,...,C_k})
```

#### Outras técnicas

- Filtragem no domínio espacial
  - Segmentação na própria imagem
    - Sem transformações
    - Uso de medidas calculadas na imagem
- Filtragem no domínio da frequência
  - No espaço de transformada de Fourier
- Transformação para um espaço de medida específico
  - No espaço Euclidiano
    - Transformação linear para outro espaço
      – Ex. transformada de Hough, wavelets
- Baseadas em Morfologia Matemática
  - Transformada watershed (divisor de águas)
- Contornos ativos – ou modelos deformáveis
  - Snakes – extração de bordas de objetos da cena
    - Contorno ajustado a curvas (splines)
    - Inicialmente uma configuración inicial evolui até se ajustar ao objeto de interese

#### Propriedades do Pixel

Retangular ou quadrada. Três aspectos a considerar:

- Vizinhança em Pixel (Vizinhança-4 e Vizinhança-8)
- Medidas de Distância
  - Conectividade * Propriedade de um pixel está conectado a outro

#### Vizinhança em *Pixel* (Vizinhança-4 e Vizinhança-8)

Quais são os vizinhos de um determinado pixel?

- Importante para segmentação e continuidade do objeto
   a. vizinhança-4 de p - $N_4(p)$
   b. vizinhança-D de p – $N_D(p)$
   c. vizinhança-8 de p – $N_8(p)$

<!-- Imagem -->
<!-- Imagem -->
<!-- Imagem -->

#### Medidas de Distância

Distância *city-block*, *Manhattan* ou quarteirão e Distância Euclidiana:

$$
D(X_i, X_j) =
\left[
   \sum^{n}_{l=1}
   |X_{il} - X_{jl}|^r
\right] ^{\frac{1}{r}}
$$

- $X_i$, $X_j$: Vetor de elementos
- $n$: é o número de dimensões
- $r$: "o grau de precisão, talvez"

<!-- Imagem -->

- Distância Euclidiana: $\leq \sqrt{8}$ do *pixel* central
- Distância Manhattan: $D_1 = |X_{ix} - X_{jx}| + |X_{iy} - X_{jy}| $
- $D(p,q) = \max(|x_{ix}–x_{jx}|,|x_{iy}–x_{jy}|) \leq 2$

#### Conectividade

- Dois *pixels* estão conectados se:
  - são adjacentes ($N4(p)$ ou $N8(p)$); e,
  - atributos (níveis de cinza, texturas ou cores) similares.
- Níveis de conectividade:
  - **Conectividade de 4**: $q$ está em $N_4(p)$ e atributos iguais.
  - **Conectividade de 8**: $q$ está em $N_8(p)$ e atributos iguais.

#### Tipos de características

Qual escolher?

<!-- Árvore -->
```mermaid
[Características] -- [De aspecto]
[De aspecto] -- [Rugosidade, Cor, Textura]
[Características] -- [De forma]
[De forma] -- [De contorno]
[De forma] -- [De regiões]
[De regiões] -- [Dimensionais]
[De regiões] -- [Inerciais]
[De regiões] -- [Topológicas]
[Dimensionais] -- [Área, Perímetro, Excentricidade, Compacidade, Raio máximo, Raio mínimo]
[Inerciais] -- [Centro geométrico, Momento, Orientação, Retângulo envolvente, Elipse ajustada]
[Topológicas] -- [Número de furos, Número de Euler, Componentes conectados, Número de vértices]
```

#### Análise de Componentes Principais (PCA)

- Componentes
- principal representa melhor a distribuição dos dado
- secundária é perpendicular à componente principal.

- Passos:
- Obter as n amostras
- Calcular a média
- Calcular a matriz de covariância
- Calcular os autovalores e autovetores da matriz de covariância
- Componente principal e secundaria: autovetores de maior e menor autovalor,
respectivamente.

#### Matriz de covariância

A matriz de covariância para M amostras de vetores pi, com
vetor médio m pode ser calculada de acordo com:

#### O vetor médio pode ser calculado

```c
c_triple_real32 *obbtree_calcula_autovetores(c_triple_real32 *cov, c_real32
*lambda)
c_real32 *calcula_autovalores(c_triple_real32 *cov) {
{ c_uint16 x, y; c_triple_real32 *xy; c_real32 m1, m2;
c_uint16 x, y; c_real32 *lambda; c_real32 m; x =0; y =1;
lambda = aloca_array_real32((c_uint16)2); xy = aloca_array_triple_real32((c_uint16)3);
x =0; y =1; if((lambda[0] == 0.0f) && (lambda[1] == 0.0f)) // se for circulo
m = sqrt(pow((cov[x][x] - cov[y][y]), 2) {
+ 4.0f*pow(cov[x][y], 2)); ca_scala_triple_real32(v_un_x, 1.0f, xy[0]); // vetor unitario (1,0)
lambda[0] = ((cov[x][x] + cov[y][y] + m) / 2.0f); ca_scala_triple_real32(v_un_y, 1.0f, xy[1]); // vetor unitario (0,1)
lambda[1] = ((cov[x][x] + cov[y][y] - m) / 2.0f); } else {
return lambda; xy[0][0] = (c_real32)(- 1.0f * cov[x][y]);
} xy[0][1] = cov[x][x] - lambda[0];
xy[0][2] = 0.0f;
m1 = ca_modulo_triple_real32(xy[0]);
xy[1][0] = (c_real32)(- 1.0f * cov[x][y]);
xy[1][1] = cov[x][x] - lambda[1];
xy[1][2] = 0.0f;
m2 = ca_modulo_triple_real32(xy[1]);
if(m1 > m2) {
m2 = (c_real32)1.0f / m1;
ca_scala_triple_real32(xy[0], m2, xy[0]);
Vetor caixa_retangular(float [][] cov) xy[1][0] = (c_real32)(- 1.0f * xy[0][1]);
{ xy[1][1] = xy[0][0];
calcula_matriz_covariancia_area(vetor pts) } else {
lambda = calcula_autovalores(cov); m1 = (c_real32)1.0f / m2;
ordena_autovetores_para_eixos(lambda); ca_scala_triple_real32(xy[1], m1, xy[1]);
xy = calcula_autovetores(cov, lambda); xy[0][0] = (c_real32)(- 1.0f * xy[1][1]);
} xy[0][1] = xy[1][0];
}
}
return xy;
}
```

#### Autoespaços , autovetores e autovalores

Um vetor v é um autovetor de uma matriz quadrada M se

Escalar - é autovalor de M associado ao autovetor v.

#### Descritores de forma

Área e Retângulos envolventes
É necessário que a imagem tinha sido segmentada

#### Perímetro, Alongamento e Retangularidade

Perímetro - número de pixels conexos que constituem
o contorno da região.

Alongamento - relação de lados do menor retângulo
que envolve o objeto.

Retangularidade - relação entre a área do objeto e
área do menor retângulo que o envolve.

#### Excentricidade, diâmetro, raio máximo e mínimo do objeto

Diâmetro de um objeto - maior
distância entre 2 pontos deste objeto.
Excentricidade - relação entre dois
pontos extremos do objeto que
passem pelo eixo maior e eixo
ortogonal.
Raio máximo e mínimo do objeto -
distâncias máxima e mínima,
respectivamente, da borda ao centro
geométrico.

#### Contornos

(a) (b)
Exemplo de aplicação do filtro de gradiente (b) para acentuar o
contorno em uma imagem de tomografia (a). Neste exemplo
foram realizados procedimentos para ligação de bordas.

#### Código da Cadeia

Vizinhança- 4 de p, N4(p) Vizinhança- 8 de p, N8(p)

#### (a) (b)

Pontos onde o código se diferencia do vizinho.

#### Transformada de Hough

Transformar a imagem do espaço digital (x,y) para uma
representação na forma dos parâmetros descritos pela curva
que se deseja encontrar na imagem
Etapas da aplicação da transformada de Hough para qualquer forma
geométrica.

#### Retas

y = mx + g
yh = m x h + g
yp = m xp + g

yq = m x q + g

yr = m x r + g
espaço (x,y) espaço de parâmetros(m,g)

- Cada ponto no espaço da imagem transforma- se em uma reta no espaço de parâmetro: g = - mx + y.
- Para reta vertical m = 0 ➔ infinita (não funciona)

#### Retas – forma polar: r = x cos + y sin

Plano xy (espaço de imagem) Plano r (espaço de parâmetros)
Cada ponto P(x,y) no espaço da imagem, corresponde a uma
senóide S(,) no espaço de parâmetros.

#### Algoritmo de Hough (para retas)

#### Circulo: (x - a)2 + (y - b)2 = r2

Espaço de imagem
Espaço de parâmetros

#### Histograma de Gradientes Orientados

- HOG (Histogram of Oriented Gradients)
- Histograma local de gradientes
- Áreas regulares na imagem
Células Descritor global
8 x 8 pixels x = (x1,.., x1)
Imagem: 10 x 10
Células

3 4 10 2 7 6 4 2 17 4 3 3
 (x orientação)

#### Gradiente

Kernel:

No Eixo X: −1 0 1
1
No Eixo Y: 0
−1

Variação de intensidades (Altas frequências)
Magnitude
𝑚 𝑥𝑖 , 𝑦𝑖 = 𝜕𝑥 𝑥𝑖 , 𝑦𝑖 2 + 𝜕𝑦 𝑥𝑖 , 𝑦𝑖 2
Orientação
𝜕𝑦 𝑥𝑖 , 𝑦𝑖
𝑎𝑛𝑔 𝑥𝑖 , 𝑦𝑖 = 𝑎𝑇𝑎𝑛
𝜕𝑥 𝑥𝑖 , 𝑦𝑖

#### Processo

Calcular as
HOG de
todas as
células

ang.
3
2
1
16
0 22,5 45 66,5 90 …… 360

#### Normalização

Variações de iluminação → variam os gradientes

1 2

3 4
Bloques
V1 = (x11, …, x1d, x21, …, x2d, x31, …, x3d, x41, …, x4d)
Vn1 = (x11, …, x1d, x21, …, x2d, x31, …, x3d, x41, …, x4d) / || V1 || Norma L2
1
Norma L2: 𝑣 = 𝜀+σ 𝑥𝑖 2 2

#### Vetor HOG

Concatenação
HOG = (x1, …, xn)

#### Efeitos de Superposição

#### Reconhecimento de Padrões em Imagens

- Reconhecimento de Padrões
- Classificação Supervisionada
- Classificação Não Supervisionada
- Redes Neurais Artificiais
- Lógica Fuzzy

## Slide 6 - Textura

Textura
Rivera

### Textura

- Padrão visual que possui algumas propriedades de homogeneidade que
não resultam simplesmente de uma cor ou intensidade. Aspecto visual da
superfície.
- Relacionada com coeficientes de uniformidade, densidade, aspereza,
regularidade, intensidade, dentre outros, oriundos da probabilidade de
ocorrência de variações tonais.

Área mínima: elemento
básico de textura ou
texel ou texton

Textura não pode ser
definida em um pixel,
mas sim através e uma
região de conjunto de
pixels.

### Espaço de Textura

- Pode ser vantajoso assumir que o padrão da imagem se repete fora desse intervalo
T (s, t) = Im [ (1 – s) N mod
N, t M mod M ]

### cor rgb do texel atribuída

ao pixel
texel correspondente ao
ponto

### Mapeamento

A especificação dos vértices dos polígonos e precedida da especificação do
ponto da textura (texel) que ai mapeia.
(1, 1)

1
t
0 s 1 (- 1, - 1)

glBindTexture(GL_TEXTURE_2D,texID);
glBegin(GL_QUADS);
glTexCoord2f(0,0); glVertex3f(- 1.0f, - 1.0f, 0.0f);
glTexCoord2f(1,0); glVertex3f( 1.0f, - 1.0f, 0.0f);
glTexCoord2f(1,1); glVertex3f( 1.0f, 1.0f, 0.0f);
glTexCoord2f(0,1); glVertex3f(- 1.0f, 1.0f, 0.0f);
glEnd();

### - A escolha de coordenadas no espaço das texturas e "livre"

(0.2, 0.8)

1

t
(0.4, 0.2)
(0.8, 0.4)
0 s 1

Espaço de textura Espaço de objeto

### Parametrização da Esfera

Função de mapeamento
z
x( , ) = sin  cos  = π t
y ( , ) = sin  sin = 2π  s
φ
z ( , ) = cos
y

Função de mapeamento inversa
arccos z
x
 = arccos z t=

y
 = arctan arctan
y
x x
s=
2

### Parametrização do Cilindro

Função de mapeamento
z
x = cos = 2π  s
y = sin z =t
z=z
y

Função de mapeamento inversa
x
 = arctan
y
s=
x 2π
z=z t=z

### Parametrizando Objetos Genéricos

- O que fazer quando o objeto não comporta uma
parametrização natural?
- Uma sugestão é usar um mapeamento em 2
estágios [Bier e Sloan]:
- Mapear textura sobre uma superfície simples
como cilindro, esfera, etc aproximadamente
englobando o objeto
- Mapear superfície simples sobre a superfície do
objeto. Pode ser feito de diversas maneiras
- Raios passando pelo centróide do objeto
- Raios normais à superfície do objeto
- Raios normais à superfície simples
- Raios refletidos

### Exemplos

Parametrização Projetada em Projetada em
esférica um cubo um cilindro

### Efeitos especiais com mapeamento de textura - Bump mapping

- Utiliza texturas para perturbar a direção do vetor normal de cada ponto da superfície (Blinn, 1978).
– Não modifica a forma da superfície.
– Modelo de iluminação usa o vetor normal modificado.
Esfera com textura Bump map Esfera com textura difusa
difusa e bump mapping

---

- Simula detalhes na superfície sem
a necessidade de criar geometria.
- Por outro lado:
– Não produz silhuetas corretas.
– Não simula oclusão entre os
detalhes.
– Não simula sombras entre os
detalhes.

### Efeitos especiais com mapeamento de textura - Displacement mapping

- Semelhante ao bump mapping, porém modifica a geometria.
– Cada texel do displacement map é um valor de deslocamento do
vértice ao longo do vetor normal.

### Característica da textura

Entropía (E) da imagem: número avaliador da aleatoriedade

m: número texels na imagem
i =1   pi  pi: probabilidade de i- ésimo texel seja utilizada novamente
0  menos irregular … mais irregular ➔
E=0 E = 0.9149
E = 5.8766 E = 5.9851 E = 6.2731

### Coeficiente de Hurst

Geometria fractal em análise textural

- índice numérico para identificação

ln N
D= N: número de partes de uma imagem I
1
ln   r: factor de escala
r
N=9
Hurst usado para dimenão fractal (DE):

- Determinação da rugosidade de superfície terrestre
- Classificação da imagem
- Tipos de paisagens
- Fraturas de superfícies
- Desgastes, eroção, corroção, etc.

Imagem 7 x 7

---

- Determinar: ∆g → maior diferença de nível de cinza para cada classe
- Buscar o maior e menor tom da região
- determinar a diferença por vez
- Obter os logaritmos de cada diferença
- Obter ajuste da reta y = bx + a

n ln d ln g −  ln d  ln g
b=
n (ln d ) −  (ln d )
2 2
a=
 ln g
−b
 ln d
n n

A reta neste caso tem a
equação: y =
1,2229x+3,1952.
Coeficiente de Hurst:
inclinação da reta,
b=1,2229.

#### Coeficiente de Hurst: inclinação da reta, b=1,2229

De segmento de imagem com C. de Hurst define a mesma altura

## Slide 7 - Compressão de Imagem

Compressão de Imagem
Rivera

### Compressão de Imagem

- Formas de diminuir a área de armazenamento dos dados,
reduzindo a quantidade de bits para representar os dados
(imagem, texto, ou arquivo qualquer).

- Em compressão de imagem define- se como a forma
(algoritmos e métodos) de armazenar informações visuais
mais compactamente.

### Redundâncias na Imagem

Tipos de redundância em imagens:

- De codificação de tons ou cor
- níveis de cinza ou cores da imagem codificados com mais símbolos de
codificação do que o necessário.
- Inter-pixel
- resultantes das relações geométricas entre os objetos na imagem.
- Espectral
- valores espectrais, para a mesma posição na matriz de pixels de cada banda, são
correlacionados.

- Psicovisuais
- relacionadas ao fato do sistema visual humano não responder com a mesma
sensibilidade a todas as informações visuais.

### Compressão de imagens e modelos de cores

- YIQ (para transmissão de televisão);
- RGB (para monitores de computador colorido); CMY (para impressoras
coloridas;
- HSI (Hue, Saturation, Intensity ou matiz, saturação, intensidade);
- HSV (Hue, Saturation, Value) ou matiz, Saturação e Valor;
- YCBCR - compressão de imagens (usado no formato de imagens JPEG).

### Medição do Desempenho

Medida de desempenho - > taxa de compressão
Tamanho(ImagComp) / tamanho(ImagOrig)

- Técnicas sem perda
- quanto maior a taxa de compressão melhor é a técnica de compressão.

- Técnicas com perda
- deve- se considerar também a qualidade do sinal ou dado reconstruído.
- Critérios de fidelidade
- se a remoção de dados causou perda de informação visual.
- Podem ser: quantitativos ou subjetivos.

### Critérios de fidelidade objetivos

Sendo F(x, y) a imagem original e G(x, y) a imagem reconstruída, tem- se:
Erro Total ou absoluto:
M −1 N −1
et =  G( x, y) − F ( x, y)
x =0 y =0

Raiz Quadrada do Quadrado da Média dos Erros:
 1 M −1 N −1
erms =     G( x, y ) − F ( x, y )  2

 MN x =0 y =0
Razão ou Relação Sinal Ruído:
M −1 N −1 M −1 N −1

  G( x, y )
x =0 y =0
2
  G( x, y )
x =0 y =0
2
SNRrms = M −1 N −1 = M −1 N −1

  e( x, y )    G( x, y ) − F ( x, y )
2 2

x =0 y =0 x =0 y =0

### Original Comprida Diferença Diferença

(fractal) e absoluta relativa
reconstruída

Erro rms= 9,7622
SNR rms 10,4823
PSNR (dB)28,3398

### Métodos de Compressão de Imagem

1. Compressão sem perda ou codificação de redundância
   - Preserva todas as informações para reconstrução exata da imagem
   - Explora a redundância entre pixels na codificação
   - Ex. RLE (Run Lenght Encoding), LZ (Lempel Ziv), LZW (Lempel Ziv Wech), algoritmo de Huffman (usadas nos formatos: PCX, PNG, GIF, TIFF).
2. Compressão com perda
   - Há perda de dados durante a compressão da imagem
   - É mais eficiente em relação à área final de armazenamento
   - Não é admissível em aplicações médicas

- Degradação visual na imagem

### Compressão Simétrica e Assimétrica

Classificação quanto ao tempo de compressão e descompressão.

- Compressão simétrica: tempo de compressão é igual ao de descompressão
- Transformadas de Wavelets (WT) e Transformadas de Cossenos (DCT -  Discrete Cosine Transform).

- Compressão assimétrica: tempo de compressão é bem maior que o
tempo de descompressão
- fractal.

### Entropia da Imagem

Seja A = {a1, a2, ...,aJ} tonalidade de cinza ou tabela de cores de RGB
Entropia permite saber se uma imagem tem redundância
J
H ( A) = −  P(a j ) - log P(a j )
j =1
Cor Total Probabilidade
4 4 4 4 64 64 128 128
4 12 12/32=3/8
4 4 4 4 64 64 128 128
16 4 4/32=1/8
4 4 16 16 128 128 128 128
64 4 4/32=1/8
4 4 16 16 128 128 128 128 128 12 12/32=3/8

Imagem 4x8=32 pixels em grayscale Probabilidades para cada nível de cinza

$$
H(A) = – P(4) * log2(P(4)) – P(16) * log2 (P(16)) – P(64) * log2 (P(64)) – P(128) * log2 (P(128))
H(A) = –[3/8 * log2 (3/8) + 1/8 * log2 (1/8) + 1/8 * log2 (1/8) + 3/8 * log2 (3/8)] = 0.81 bits/pixel
$$
Usados 4x8 pixels = 32 pixels ➔ ( 0.81 bits/pixel ) x (32 pixel) = 25 bits
De informação redundante.

### Codificação de Huffman

- Redundância de codificação é eliminada
- Codificação de tamanho variável
- Atribui os códigos de tamanhos menores aos níveis de cinza mais prováveis de ocorrer.

Duas etapas:

1. Redução
   - Cria símbolos juntando dois de menores probabilidades a cada iteração.
2. Codificação
   - Símbolos reduzidos - começando com o de maior probabilidade que será associado ao menor código e voltando para os originais.

### Exemplo

Seja imagem M: 10x10 de 6 tons de cinza (a1 a2 a3 a4 a5 a6)

Primeira etapa: redução

1. Selec. de (a1 a2 a3 a4 a5 a6) 2 de menor prob.
   - p(a4) + p(a6) = 1/16 = p(a7)
2. Selec. de (a1 a2 a3 a5 a7) 2 de menor prob.
   - p(a3) + p(a7) = 5/32 = p(a8)
3. Selec. de (a1 a2 a5 a8) 2 de menor prob.
   - p(a2) + p(a5) = 7/32 = p(a9)
4. Selec. de (a1 a8 a9) 2 de menor prob.
   - p(a8) + p(a9) = 3/8 = p(a10)
5. Selec. de (a1 a10) 2 de menor prob.
   - p(a1) + p(a10) = 1 = p(a11)

### Segunda etapa da codificação de Huffman

Informação Probabilidade Código
a1 5/8=20/32 0
a10 3/8=12/32 1
a9 7/32 10
a8 5/32 11
a5 1/8=4/32 101
a2 3/32 100
a3 3/32 110
a7 2/32 111
a4 1/32 1110
a6 1/32 1111

Uma cadeia de códigos: 110 0 100 0 1111 110 0 101 0 1110
É: a3 a1 a2 a1 a6 a3 a1 a5 a1 a4

### Codificação por LZW

Usa tabela de palavras contendo os símbolos que serão codificados.

Routine LZW_COMPRESS Exemplo:
STRING = get input char Input String = /WED/WE/WEE/WEB/WET
WHILE there are still input chars DO CharInp CodeOut NewCodeVal NewString
CHAR = get input char
/W / 256 /W
IF STRING+CHAR is in the string table THEN
STRING = STRING+CHAR E W 257 WE
ELSE D E 258 ED
output the code for STRING
add STRING+CHAR to the string table / D 259 D/
STRING = CHAR WE 256 260 /WE
END of IF
/ E 261 E/
END of WHILE
output the code for STRING WEE 260 262 /WEE
/W 261 263 E/W

/WED/WE/WEE/WEB/WET EB 257 264 WEB
/ B 265 B/
/WED- E- *- B*T
WET 260 266 /WET
EOF T

### Decodificação LZW

Input Codes: / W E D 256 E 260 261 257 B 260 T
Routine LZW_DECOMPRESS
Input/ STRING/ New
oldCod CHAR
newCod Ouput table entry
Read OLD_COD / / / / /
output OLD_COD W / W W 256 = /W
WHILE there are still input characters DO E W E E 257 = WE
Read NEW_COD D E D D 258 = ED

STRING = get translation of NEW_COD 256 D /W / 259 = D/

output STRING E 256 E E 260 = /WE

CHAR = first character in STRING 260 E /WE / 261 = E/

add OLD_COD + CHAR to the translation table 261 260 E/ E 262 = /WEE

OLD_COD = NEW_COD 257 261 WE W 263 = E/W
B 257 B B 264 = WEB
END of WHILE
260 B /WE / 265 = B/
T 260 T T 266 = /WET

/WED/WE/WEE/WEB/WET

### Transformada Discreta do Co- seno (DCT)

Transforma discreta de co- senos em 2- D : Espacial → frequência
N −1 N −1
(2 y + 1)i (2 x + 1) j
T [i, j ] = c(i)c( j )  I [ y, x] cos cos
x =0 y =0 2N 2N

 2
i, j  0
onde c(i), c( j ) =  N

 1
N i, j = 0

Transformada Inversa IDCT 2- D:

N −1 N −1
(2 y + 1)i (2 x + 1) j
I [ y, x] =   c(i )c( j )T [i, j ] cos cos
i =0 j =0 2N 2N

Essa compressão é usada no formato JPEG padrão com valor de N igual a 8.

### Compressão por Wavelets

Qualquer função, com período 2, pode ser reescrita como a
soma dos termos da Série de Fourier:

a 0 +  (a n cos nt + bn sen nt )
n =1
Os coeficientes são calculados por:
2

 f (t ) dt
2
a0 =
T 0

2

 f (t ) cos(nt )dt
2
an =
T 0

2

 f (t ) sen(nt )dt
2
bn =
T 0

### Análise de Wavelet

- Ferramenta matemática para decomposição em nível hierárquico em aproximações (O) e detalhes (D).
- O nível hierárquico em escala diática (formado por potência de 2).
- Descrição de uma função em termos globais, mais termos que variam de O(1) detalhes globais até detalhes finos.
- A função em questão pode ser uma O(2) D(2) imagem, uma curva ou uma superfície. O(3) D(3)

O(n) D(n)

### Transformada de Wavelet Contínua (TWC)

A Transformada de Wavelets contínua em F(a,b) é:

F (a, b) =  f (t ) a ,b (t ) dt

A função a,b (t ) é denominada wavelet:

1 t −b
a , b (t ) =   , a  0 , b 
a  a 

As funções wavelets são derivadas
segundo os critérios:
−1 2
ˆ (u ) du  
C = 2  u 

### Transformada de Wavelet Discreta

t −b
a , b (t ) = ( j, k )  Z 2
1
 , a=2 ,b=k 2 ,
j j

a  a 
Transformada Wavelet Haar Unidimensional

Resolução Valor Aprox. Coef. Detalhes
4 [ 9 7 3 5 ]
2 [ 8 4 ] [ 1 - 1 ] [ 6 2 1 - 1 ]
1 [ 6 ] [ 2 ]

### Sequência de aproximação e coeficientes de detalhes

Aproximação V4

Espaço de Imagem
V 0  V 1  V 2 ...

Aproximação V3 Coeficientes de detalhes W3
Base de V j

i j ( x) =  (2 j x − i )
Aproximação V2 Coeficientes de detalhes W2
Espaço de Detalhes
W 0 V 0 = V 1

Aproximação V1 Coeficientes de detalhes W1 W 1 V 1 = V 2

Base de W j
 i j ( x) =  (2 j x − i )
Aproximação V0 Coeficientes de detalhes W0

### Bases Haar

### Normalidade

Uma função base u(x) é normalizada se u u =. 1

Haar normalizado:

 i (x ) := 2 2  (2 j x − i ), i = 0, ..., 2 j − 1
j
j

 i (x ) := 2 2  (2 j x − i ), i = 0, ..., 2 j − 1
j
j
Ex. para [6 2 1 - 1], se tornam normalizados:
 1 −1
6 2 
 2 2

### Algoritmo de Transformada Wavelet Haar

Decomposi ( C[1...2^j ])
C c / sqrt (2 ^ j ) // normaliza coef inp DecomposiStep ( C[1...2^j ])
g2^j FOR i = 1 .. 2 ^ (j- 1)
WHILE g >= 2 DO C’ ( C[2i – 1] + C[2i] ) / sqrt (2)
DecomposiStep ( C [1 .. g ]) C’[2^(j- 1) + 1] (C[2i – 1] - C[2i] ) / sqrt (2)
gg/2 END
END C C’
Reconstruc ( C[1...2^j ])
ReconstrucStep ( C[1...2^j ])
g2
FOR i = 1 .. 2 ^ (j- 1)
WHILE g =< 2 ^ j DO
C’[ 2i – 1 ] ( C[ i ] + C[2 ^ (j- 1) + i] ) / sqrt (2)
ReconstrucStep ( C [1 .. g ]) C’[2i] (C[ i ] - C[2 ^ (j –i) + i ] ) / sqrt (2)
g 2g END
END C C’
C C sqrt ( 2 ^ j ) // sem normalização

### Transformada de Wavelet de Haar bidimensional

a. Decomposição padrão
b. Decomposição não padrão.

### Compressão

O objetivo da compressão é expressar um conjunto inicial de dados
usando outro conjunto menor, com ou sem perda de informação.

Seja a imagem f (x) expressa pela soma de funções base :
m
f ( x ) =  ci u i ( x )
i =1
Com m coeficientes ci.
A função que aproxima f(x), com menos coeficientes:
~
m
f (x ) =  c~i u~i (x )  f (x )
~
i =1

### Aproximações e Detalhes

Árvore de Decomposição Árvore de Decomposição Wavelet
Wavelet de um sinal
