# Slides

## Consertar depois

### Slide 1 - Fundamentos de Pocessamento de Imagens

### Slide 2 - Visão Computacional

### Slide 3 - Operações em Imagens

### Slide 4 - Filtros de Imagens

### Slide 5 - Extração de Características

- Sistema de análise de imagens
- Reconhecimento de elementos e objetos
- Parâmetros quantificáveis
- Cor, posição, orientação, dimensões, textura, etc.

<!-- Imagem -->

---

Etapas de um sistema de reconhecimento de padrões

```mermaid
graph LR;
id1[Imagem]
id2[Segmentação: Separa objeto ou padrão]
id3[Caracterização]
id4[(BD de Padrões)]
id5[Classificador]
id6[Reconhece o padrão]

id1 --> id2 --> id3
id3 & id4 --> id5 --> id6
```

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
flowchart TB;

id1((Kmeans X, k))
id2[Select the k initial centers - ci = Random X _ i=1,...,k ]
id3[Copy ci -> cci, Para todo i = 1, ..., k]
id4[Clusters gerator with center cci - Para todo x \in X in C1, ... , Ck]
id5[Re-compute clusters center - ci = Mean Ci i=1, ..., k]
id6[Varies = Compare ci, cci]
id7[[Varies]]
id8((Solution C_1,...,C_k))

id1 --> id2 --> id3 --> id4 --> id5 --> id6 -->
id7 -->|Y| id3
id7 -->|N| id8
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
  - são adjacentes ($N_4(p)$ ou $N_8(p)$); e,
  - atributos (níveis de cinza, texturas ou cores) similares.
- Níveis de conectividade:
  - **Conectividade de 4**: $q$ está em $N_4(p)$ e atributos iguais.
  - **Conectividade de 8**: $q$ está em $N_8(p)$ e atributos iguais.

#### Tipos de características

Qual escolher?

```mermaid
flowchart LR
    A1[Características]
    B1[De forma]
    B2[De aspecto]
    C1[De contorno]
    C2[De regiões]
    C3[Rugosidade, Cor, Textura]
    D1[Dimensionais]
    D2[Inerciais]
    D3[Topológicas]
    E1[Área, Perímetro, Excentricidade, Compacidade, Raio máximo, Raio mínimo]
    E2[Centro geométrico, Momento, Orientação, Retângulo envolvente, Elipse ajustada]
    E3[Número de furos, Número de Euler, Componentes conectados, Número de vértices]

    A1 --> B1 & B2;
    B1 --> C1 & C2;
    B2 --> C3;
    C2 --> D1 & D2 & D3;
    D1 --> E1;
    D2 --> E2;
    D3 --> E3;
```

#### Análise de Componentes Principais (PCA)

- **Componentes**
  - **principal** representa melhor a distribuição dos dado
  - **secundária** é perpendicular à componente principal.

- Passos:
  - Obter as $n$ amostras
  - Calcular a média
  - Calcular a matriz de covariância
  - Calcular os autovalores e autovetores da matriz de covariância
  - Componente principal e secundaria: autovetores de maior e menor autovalor, respectivamente.

#### Matriz de covariância

A matriz de covariância para $M$ amostras de vetores $P_i$, com o vetor médio $m$ pode ser calculada de acordo com:

$$
C_x = \frac{1}{M} \sum^{M}_{i=1} (x_i -m_x)(y-i - m_y)
$$

O vetor médio pose ser calculado:

$$
m = \frac{1}{M} \sum^{M}_{i=1} p_i
$$

---

```c

c_real32 *calcula_autovalores(c_triple_real32 *cov) {
  c_uint16 x, y; c_real32 *lambda; c_real32 m;
  lambda = aloca_array_real32((c_uint16)2);
  x = 0; y = 1;
  m = sqrt(pow((cov[x][x] - cov[y][y]), 2)
  + 4.0f*pow(cov[x][y], 2));
  lambda[0] = ((cov[x][x] + cov[y][y] + m) / 2.0f);
  lambda[1] = ((cov[x][x] + cov[y][y] - m) / 2.0f);
  return lambda;
}

Vetor caixa_retangular(float [][] cov) {
  calcula_matriz_covariancia_area(vetor pts)
  lambda = calcula_autovalores(cov);
  ordena_autovetores_para_eixos(lambda);
  xy = calcula_autovetores(cov, lambda);
}

c_triple_real32 *obbtree_calcula_autovetores(c_triple_real32 *cov, c_real32 *lambda) {
  c_uint16 x, y; c_triple_real32 *xy; c_real32 m1, m2;
  x = 0; y = 1;
  xy = aloca_array_triple_real32((c_uint16)3);
  if((lambda[0] == 0.0f) && (lambda[1] == 0.0f)){ // se for circulo
    ca_scala_triple_real32(v_un_x, 1.0f, xy[0]);  // vetor unitario (1,0)
    ca_scala_triple_real32(v_un_y, 1.0f, xy[1]);  // vetor unitario (0,1)
  } else {
    xy[0][0] = (c_real32)(-1.0f * cov[x][y]);
    xy[0][1] = cov[x][x] - lambda[0];
    xy[0][2] = 0.0f;
    m1 = ca_modulo_triple_real32(xy[0]);
    xy[1][0] = (c_real32)(-1.0f * cov[x][y]);
    xy[1][1] = cov[x][x] - lambda[1];
    xy[1][2] = 0.0f;
    m2 = ca_modulo_triple_real32(xy[1]);
    if(m1 > m2) {
      m2 = (c_real32)1.0f / m1;
      ca_scala_triple_real32(xy[0], m2, xy[0]);
      xy[1][0] = (c_real32)(-1.0f * xy[0][1]);
      xy[1][1] = xy[0][0];
    } else {
      m1 = (c_real32)1.0f / m2;
      ca_scala_triple_real32(xy[1], m1, xy[1]);
      xy[0][0] = (c_real32)(-1.0f * xy[1][1]);
      xy[0][1] = xy[1][0];
    }
  }
  return xy;
}
```

#### Autoespaços, autovetores e autovalores

Um vetor $v$ é um **autovetor** de uma matriz quadrada $M$ se $Mv = \lambda v$

Escalar $\lambda$ é **autovalor** de $M$ associado ao autovetor $v$.

<!-- Imagem -->

#### Descritores de forma

Área e Retângulos envolventes

É necessário que a imagem seja segmentada

<!-- Imagens -->

#### Perímetro, Alongamento e Retangularidade

**Perímetro**: número de *pixels* conexos que constituem o contorno da região.
**Alongamento**: relação de lados do menor retângulo que envolve o objeto.
**Retangularidade**: relação entre a área do objeto e área do menor retângulo que o envolve.

#### Excentricidade, diâmetro, raio máximo e mínimo do objeto

**Diâmetro de um objeto**: maior distância entre 2 pontos deste objeto.
**Excentricidade**: relação entre dois pontos extremos do objeto que passem pelo eixo maior e eixo ortogonal.
**Raio máximo e mínimo do objeto**: distâncias máxima e mínima, respectivamente, da borda ao centro geométrico.

<!-- Imagem -->

#### Contornos

<!-- Imagens -->

Exemplo de aplicação do filtro de gradiente (b) para acentuar o contorno em uma imagem de tomografia (a). Neste exemplo foram realizados procedimentos para ligação de bordas.

#### Código da Cadeia

<!-- Imagem -->
<!-- Imagem -->

Vizinhança-4 de $p$, $N4(p)$
Vizinhança-8 de $p$, $N8(p)$

---

<!-- Imagem -->
<!-- Imagem -->

Pontos onde o código se diferencia do vizinho.

#### Transformada de Hough

Transformar a imagem do espaço digital $(x,y)$ para uma representação na forma dos parâmetros descritos pela curva que se deseja encontrar na imagem

```mermaid
graph LR;
id1[Identificar fórmula a ser encontrada]
id2[Aplicar a fórmula para cada pixel aceso na imagem]
id3[Incrementar a posição da matriz de parâmetros que satisfizer a fórmula]

id1 --> id2 --> id3
```

Etapas da aplicação da transformada de Hough para qualquer forma geométrica.

#### Retas

$y = mx+g$

<!-- Imagem -->
<!-- Imagem -->

$y_h = m x_h + g$
$y_p = m x_p + g$
$y_q = m x_q + g$
$y_r = m x_r + g$

espaço (x,y)
espaço de parâmetros(m,g)

- Cada ponto no espaço da imagem transforma- se em uma reta no espaço de parâmetro: $g = - mx + y$.
- Para reta vertical $m = 0 \rightarrow$ infinita (não funciona)

##### forma polar

$r = x cos\theta + y sin\theta$

Plano xy (espaço de imagem) <!-- Imagem -->
Plano $\theta r$ (espaço de parâmetros) <!-- Imagem -->

Cada ponto $P(x,y)$ no espaço da imagem, corresponde a uma senóide $S(\rho, \theta)$ no espaço de parâmetros.

##### Algoritmo de Hough (para retas)

Espaço de imagem <!-- Imagem -->
Espaço de parâmetros <!-- Imagem -->

1. Discretizar espaço de parâmetros $S(\theta, r)$ em $(\theta_{min} , \theta_{max}) x (r_min, r_max)$
   - Matriz acumulador A de inteiros
2. Zerar A (valor inicial)
3. Para cada *pixel(x,y)*, com gradiente maior que o limiar zero
   - Calcular as coordenadas $(c\theta, cr)$ de $A$ restrita à linha desejada
   - Incrementar:  $A (c\theta, cr) += 1$
4. Buscar o máximo local em $A \rightarrow (c\theta, cr)$
5. Converter $(c\theta, cr)$ para espaço de imagem

#### Círculo: $(x - a)^2 + (y - b)^2 = r^2$

Espaço de imagem <!-- Imagem -->
Espaço de parâmetros <!-- Imagem -->

- Acumulador $A(\_, \_ , \_)$
- $0 \leq r \leq diag$
  - diag = Diagonal do plano da imagem
- $0 \leq a, b \leq diag$

Usando gradiente:

$$
\frac{\partial}{\partial x}
\left[
  (x-a)^2 + (y-b)^2 = r^2
\right]
$$

#### Histograma de Gradientes Orientados

- HOG (Histogram of Oriented Gradients)
- Histograma local de gradientes
- Áreas regulares na imagem
Células Descritor global
8 x 8 pixels x = (x1,.., x1)
Imagem: 10 x 10 <!-- No histograma tá sobrando o valor um 8*8-(3+4+10+2+7+6+4+2+17+4+3+3) = -1 -->
Células

[Link](https://docplayer.com.br/79936604-Validacao-facial-com-histograma-de-gradiente-orientado.html)

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
m xi , yi = \partialx xi , yi 2 + \partialy xi , yi 2
Orientação
\partialy xi , yi
𝑎𝑛𝑔 xi , yi = 𝑎𝑇𝑎𝑛
\partialx xi , yi

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
0 22,5 45 66,5 90 \dots\dots 360

#### Normalização

Variações de iluminação → variam os gradientes

1 2

3 4
Bloques
V1 = (x11, \dots, x1d, x21, \dots, x2d, x31, \dots, x3d, x41, \dots, x4d)
Vn1 = (x11, \dots, x1d, x21, \dots, x2d, x31, \dots, x3d, x41, \dots, x4d) / || V1 || Norma L2
1
Norma L2: 𝑣 = 𝜀+σ xi 2 2

#### Vetor HOG

Concatenação
HOG = (x1, \dots, xn)

#### Efeitos de Superposição

#### Reconhecimento de Padrões em Imagens

- Reconhecimento de Padrões
- Classificação Supervisionada
- Classificação Não Supervisionada
- Redes Neurais Artificiais
- Lógica Fuzzy

## Slide 6 - Textura

Textura

### Textura

- Padrão visual que possui algumas propriedades de homogeneidade que não resultam simplesmente de uma cor ou intensidade. Aspecto visual da superfície.
- Relacionada com coeficientes de uniformidade, densidade, aspereza, regularidade, intensidade, dentre outros, oriundos da probabilidade de ocorrência de variações tonais.

**Área mínima**: elemento básico de textura ou texel ou texton

Textura não pode ser definida em um pixel, mas sim através e uma região de conjunto de pixels.

<!-- Imagem -->

### Espaço de Textura

- Pode ser vantajoso assumir que o padrão da imagem se repete fora desse intervalo

$T (s, t) = Im \left(  \lfloor (1 – s) N \rfloor \mod N, \lfloor t M \rfloor \mod M \right)$

- $s$: coordenada x da textura
- $t$: coordenada y da textura
- $M$: tamanho x da imagem
- $N$: tamanho y da imagem

<!-- Imagem -->

---

cor rgb do texel atribuída ao pixel

<!-- Imagem -->

$[texel] = [H]^{-1} * [pixel]$

texel correspondente ao ponto

### Mapeamento

A especificação dos vértices dos polígonos e precedida da especificação do ponto da textura (texel) que ai mapeia.

<!-- Imagem -->

```c
  glBindTexture(GL_TEXTURE_2D,texID);
  glBegin(GL_QUADS);
    glTexCoord2f(0,0); glVertex3f(-1.0f, -1.0f, 0.0f);
    glTexCoord2f(1,0); glVertex3f( 1.0f, -1.0f, 0.0f);
    glTexCoord2f(1,1); glVertex3f( 1.0f,  1.0f, 0.0f);
    glTexCoord2f(0,1); glVertex3f(-1.0f,  1.0f, 0.0f);
  glEnd();
```

---

- A escolha de coordenadas no espaço das texturas e "livre".

<!-- Imagem -->

- Espaço de textura
- Espaço de objeto

### Parametrização da Esfera

<!-- Imagem -->

- *Função de mapeamento*
  - $\varphi = t \pi$
  - $\theta = 2 s \pi$
  - $x(\varphi, \theta) = \sin \varphi \cos \theta$
  - $y(\varphi, \theta) = \sin \varphi \sin \theta$
  - $z(\varphi, \theta) = \cos \varphi$
- *Função de mapeamento inversa*
  - $\varphi = \arccos z$
  - $\theta = \arctan \frac{y}{x}$
  - $t = \frac{\arccos z}{\pi}$
  - $s = \frac{\arctan \frac{y}{x}}{2 \pi}$

### Parametrização do Cilindro

<!-- Imagem -->

- *Função de mapeamento*
  - $x = \cos \theta$
  - $y = \sin \theta$
  - $z = z$
  - $\theta = s 2 \pi$
  - $t = z$
- *Função de mapeamento inversa*
  - $s = \frac{\theta}{2 \pi}$
  - $t = z$
  - $z = z$
  - $\theta = \arctan \frac{y}{x}$

### Parametrizando Objetos Genéricos

- O que fazer quando o objeto não comporta uma parametrização natural?
- Uma sugestão é usar um mapeamento em 2 estágios [Bier e Sloan]:
  - Mapear textura sobre uma superfície simples como cilindro, esfera, etc aproximadamente englobando o objeto
  - Mapear superfície simples sobre a superfície do objeto. Pode ser feito de diversas maneiras
    - Raios passando pelo centróide do objeto
    - Raios normais à superfície do objeto
    - Raios normais à superfície simples
    - Raios refletidos

#### Exemplos

- Parametrização esférica <!-- Imagem -->
- Projetada em um cubo <!-- Imagem -->
- Projetada em um cilindro <!-- Imagem -->

### Efeitos especiais com mapeamento de textura

#### Bump mapping

- Utiliza texturas para perturbar a direção do vetor normal de cada ponto da superfície (Blinn, 1978).
  – Não modifica a forma da superfície.
  – Modelo de iluminação usa o vetor normal modificado.

- Esfera com textura difusa <!-- Imagem -->
- *Bump map* <!-- Imagem -->
- Esfera com textura difusa e bump mapping <!-- Imagem -->

---

<!-- Imagem -->

- Simula detalhes na superfície sem a necessidade de criar geometria.
- Por outro lado:
  – Não produz silhuetas corretas.
  – Não simula oclusão entre os detalhes.
  – Não simula sombras entre os detalhes.

#### Displacement mapping

<!-- Imagem -->

- Semelhante ao *bump mapping*, porém modifica a geometria.
– Cada texel do *displacement map* é um valor de deslocamento do vértice ao longo do vetor normal.

### Característica da textura

Entropia (E) da imagem: número avaliador da aleatoriedade

$$
E = \sum_{i=1}^{m}
\left[
  p_i \log_{2}
  \left(
    \frac{1}{p_i}
  \right)
\right]
$$

$m$: número texels na imagem
$p_i$: probabilidade de i-ésimo texel seja utilizada novamente

<!-- Imagem -->

### Coeficiente de Hurst

Geometria fractal em análise textural

- Índice numérico para identificação

$D = \frac{\ln{N}}{\ln \left( \frac{1}{r} \right)}$

<!-- Imagem -->
<!-- Imagem -->

N: Número de partes de uma imagem I
r: Factor de escala

Hurst usado para dimensão fractal (DE):

- Determinação da rugosidade de superfície terrestre
- Classificação da imagem
- Tipos de paisagens
- Fraturas de superfícies
- Desgastes, erosão, corrosão, etc.

---

- Determinar: $\Delta g \rightarrow$ maior diferença de nível de cinza para cada classe
  - Buscar o maior e menor tom da região
    - determinar a diferença por vez
- Obter os logaritmos de cada diferença
- Obter ajuste da reta $y = bx + a$

$$b =
\frac{
  n \sum \ln d \Delta g - \sum \ln d \sum \ln \Delta g
}{
  n \sum (\ln d)^2 - \sum (\ln d)^2
}
$$

$$a =
\frac{\sum \ln \Delta g}{n} - b
\frac{\sum \ln d}{n}
$$

---

<!-- 4x Imagem -->

A reta neste caso tem a equação: y = 1,2229x+3,1952.
**Coeficiente de Hurst**: inclinação da reta, b=1,2229.

---

**Coeficiente de Hurst**: inclinação da reta, b=1,2229

De segmento de imagem com Coeficiente de Hurst define a mesma altura.

a. Imagem Monocromática <!-- Imagem -->
b. Gráfico da imagem <!-- Imagem -->

## Slide 7 - Compressão de Imagem

### Compressão de Imagem

- Formas de diminuir a área de armazenamento dos dados, reduzindo a quantidade de bits para representar os dados (imagem, texto, ou arquivo qualquer).
- Em compressão de imagem define- se como a forma (algoritmos e métodos) de armazenar informações visuais mais compactamente.

### Redundâncias na Imagem

- **Tipos de redundância em imagens**:
  - **De codificação de tons ou cor**
    - Níveis de cinza ou cores da imagem codificados com mais símbolos de codificação do que o necessário.
  - **Inter-pixel**
    - Resultantes das relações geométricas entre os objetos na imagem.
  - **Espectral**
    - Valores espectrais, para a mesma posição na matriz de pixels de cada banda, são correlacionados.
  - **Psicovisuais**
    - Relacionadas ao fato do sistema visual humano não responder com a mesma sensibilidade a todas as informações visuais.

### Compressão de imagens e modelos de cores

- YIQ (para transmissão de televisão);
- RGB (para monitores de computador colorido); CMY (para impressoras coloridas);
- HSI (*Hue*, *Saturation*, *Intensity* ou matiz, saturação, intensidade);
- HSV (*Hue*, *Saturation*, *Value*) ou matiz, Saturação e Valor;
- YCBCR - compressão de imagens (usado no formato de imagens JPEG).

### Medição do Desempenho

- Medida de desempenho $\rightarrow$ taxa de compressão
  - $Tamanho(ImagComp) / tamanho(ImagOrig)$

- Técnicas sem perda
  - Quanto maior a taxa de compressão melhor é a técnica de compressão.
- Técnicas com perda
  - Deve-se considerar também a qualidade do sinal ou dado reconstruído.
- Critérios de fidelidade
  - Se a remoção de dados causou perda de informação visual.
  - Podem ser quantitativos ou subjetivos.

### Critérios de fidelidade objetivos

Sendo $F(x, y)$ a imagem original e $G(x, y)$ a imagem reconstruída, tem-se:

- Erro Total ou absoluto:
  - $$e_t = \sum_{M-1}^{x=0} \sum_{N-1}^{y=0} |G(x,y) - F(x,y)|$$
- Raiz Quadrada do Quadrado da Média dos Erros:

$$
e_{rms} = \sqrt{
  \left[
    \frac{1}{MN}
    \sum_{M-1}^{x=0} \sum_{N-1}^{y=0}
    \left[
      G(x,y) - F(x,y)
    \right]^2
  \right]
}
$$

- Razão ou Relação Sinal Ruído:

$$
SNR_{rms} =
\sqrt{
  \frac{
    \sum_{M-1}^{x=0} \sum_{N-1}^{y=0}
    G(x,y)^2
  }{
    \sum_{M-1}^{x=0} \sum_{N-1}^{y=0}
    e(x,y)^2
  }
} =
\sqrt{
  \frac{
    \sum_{M-1}^{x=0} \sum_{N-1}^{y=0}
    G(x,y)^2
  }{
    \sum_{M-1}^{x=0} \sum_{N-1}^{y=0}
    \left[
      G(x,y) - F(x,y)
    \right]^2
  }
}
$$

---

- Imagens
  - Original <!-- Imagem -->
  - Comprida (fractal e reconstruída) <!-- Imagem -->
  - Diferença absoluta <!-- Imagem -->
  - Diferença relativa <!-- Imagem -->

- Erro rms = 9,7622
- SNR rms 10,4823
- PSNR (dB)28,3398

### Métodos de Compressão de Imagem

1. Compressão sem perda ou codificação de redundância
   - Preserva todas as informações para reconstrução exata da imagem
   - Explora a redundância entre pixels na codificação
   - Ex. RLE (*Run Lenght Encoding*), LZ (*Lempel Ziv*), LZW (*Lempel Ziv Wech*), algoritmo de Huffman (usadas nos formatos: PCX, PNG, GIF, TIFF).
2. Compressão com perda
   - Há perda de dados durante a compressão da imagem
   - É mais eficiente em relação à área final de armazenamento
   - Não é admissível em aplicações médicas
   - Degradação visual na imagem

### Compressão Simétrica e Assimétrica

Classificação quanto ao tempo de compressão e descompressão.

- **Compressão simétrica**: tempo de compressão é igual ao de descompressão
  - *Transformadas de Wavelets* (WT) e Transformadas de Cossenos (DCT - *Discrete Cosine Transform*).
- **Compressão assimétrica**: tempo de compressão é bem maior que o tempo de descompressão
  - fractal.

### Entropia da Imagem

Seja $A = \{a_1, a_2, \dots,a_J\}$ tonalidade de cinza ou tabela de cores de RGB
Entropia permite saber se uma imagem tem redundância

$$
H(A) = - \sum_{J}^{j=1} P (a_j)  \log P (a_j)
$$

Imagem 4x8=32 pixels em *grayscale*

| 4   | 4   | 4   | 4   | 64  | 64  | 128 | 128 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4   | 4   | 4   | 4   | 64  | 64  | 128 | 128 |
| 4   | 4   | 16  | 16  | 128 | 128 | 128 | 128 |
| 4   | 4   | 16  | 16  | 128 | 128 | 128 | 128 |

Probabilidades para cada nível de cinza

| Cor | Total | Probabilidade |
| --- | ----- | ------------- |
| 4   | 12    | 12/32 = 3/8   |
| 16  | 4     | 4/32 = 1/8    |
| 64  | 4     | 4/32 = 1/8    |
| 128 | 12    | 12/32 = 3/8   |

$$
H(A) = – P(4) *
\log_{2}(P(4))  – P(16) *
\log_{2}(P(16)) – P(64) *
\log_{2}(P(64)) – P(128) *
\log_{2}(P(128))
$$

$$
H(A) = –[3/8 *
\log_{2} (3/8) + 1/8 *
\log_{2} (1/8) + 1/8 *
\log_{2} (1/8) + 3/8 *
\log_{2} (3/8)] =
0.81 bits/pixel
$$

Usados 4x8 pixels = 32 pixels $\rightarrow$ ( 0.81 bits/pixel ) x (32 pixel) = 25 bits De informação redundante.

### Codificação de Huffman

- Redundância de codificação é eliminada
- Codificação de tamanho variável
- Atribui os códigos de tamanhos menores aos níveis de cinza mais prováveis de ocorrer.

Duas etapas:

1. Redução
   - Cria símbolos juntando dois de menores probabilidades a cada iteração.
2. Codificação
   - Símbolos reduzidos - começando com o de maior probabilidade que será associado ao menor código e voltando para os originais.

#### Exemplo

Seja imagem M: 10x10 de 6 tons de cinza $(a_1, a_2, a_3, a_4, a_5, a_6)$

Primeira etapa: *redução*

1. Selec. de $(a_1 a_2 a_3 a_4 a_5 a_6)$ 2 de menor prob.
   - $p(a_4) + p(a_6) = 1/16 = p(a_7)$
2. Selec. de $(a_1 a_2 a_3 a_5 a_7)$ 2 de menor prob.
   - $p(a_3) + p(a_7) = 5/32 = p(a_8)$
3. Selec. de $(a_1 a_2 a_5 a_8)$ 2 de menor prob.
   - $p(a_2) + p(a_5) = 7/32 = p(a_9)$
4. Selec. de $(a_1 a_8 a_9)$ 2 de menor prob.
   - $p(a_8) + p(a_9) = 3/8 = p(a_10)$
5. Selec. de $(a_1 a_10)$ 2 de menor prob.
   - $p(a_1) + p(a_10) = 1 = p(a_11)$

---

Segunda etapa da codificação de Huffman

| Informação | Probabilidade | Código |
| ---------- | ------------- | ------ |
| $a_1$      | 5/8=20/32     | 0      |
| $a_10$     | 3/8=12/32     | 1      |
| $a_9$      | 7/32          | 10     |
| $a_8$      | 5/32          | 11     |
| $a_5$      | 1/8=4/32      | 101    |
| $a_2$      | 3/32          | 100    |
| $a_3$      | 3/32          | 110    |
| $a_7$      | 2/32          | 111    |
| $a_4$      | 1/32          | 1110   |
| $a_6$      | 1/32          | 1111   |

Uma cadeia de códigos: 110 0 100 0 1111 110 0 101 0 1110
É: $a_3 a_1 a_2 a_1 a_6 a_3 a_1 a_5 a_1 a_4$

### Codificação por LZW

Usa tabela de palavras contendo os símbolos que serão codificados.

```python
def LZW_COMPRESS:
  STRING = get input char
  while there are still input chars:
    CHAR = get input char
    if STRING+CHAR is in the string table:
      STRING = STRING + CHAR
    else:
      output the code for STRING
      add STRING+CHAR  to the string table
      STRING = CHAR
  output the code for STRING
```

input:  /WED/WE/WEE/WEB/WET
output: /WED-E-*-B*T

Exemplo:

Input String = /WED/WE/WEE/WEB/WET

| CharInp | CodeOut | NewCodeVal | NewString |
| ------- | ------- | ---------- | --------- |
| \W      | /       | 256        | /W        |
| E       | W       | 257        | WE        |
| D       | E       | 258        | ED        |
| /       | D       | 259        | D/        |
| WE      | 256     | 260        | WE        |
| /       | E       | 261        | E/        |
| WEE     | 260     | 262        | /WEE      |
| /W      | 261     | 263        | E/W       |
| EB      | 257     | 264        | WEB       |
| /       | B       | 265        | B/        |
| WET     | 260     | 266        | /WET      |
| EOF     | T       |            |           |

### Decodificação LZW

```python
def LZW_DECOMPRESS:
  Read OLD_COD
  output OLD_COD
  while there are still input characters:
    Read NEW_COD
    STRING = get translation of NEW_COD
    output STRING
    CHAR = first character in STRING
    add OLD_COD + CHAR  to the translation table
    OLD_COD = NEW_COD
```

Input Codes: / W E D 256 E 260 261 257 B 260 T

| Input/newCod | oldCod | STRING/Output | CHAR | New table entry |
| ------------ | ------ | ------------- | ---- | --------------- |
| /            | /      | /             | /    | /               |
| W            | /      | W             | W    | 256 = /W        |
| E            | W      | E             | E    | 257 = WE        |
| D            | E      | D             | D    | 258 = ED        |
| 256          | D      | /W            | /    | 259 = D/        |
| E            | 256    | E             | E    | 260 = /WE       |
| 260          | E      | /WE           | /    | 261 = E/        |
| 261          | 260    | E/            | E    | 262 = /WEE      |
| 257          | 261    | WE            | W    | 263 = E/W       |
| B            | 257    | B             | B    | 264 = WEB       |
| 260          | B      | /WE           | /    | 265 = B/        |
| T            | 260    | T             | T    | 266 = /WET      |

Output code (?): /WED/WE/WEE/WEB/WET

### Transformada Discreta do Cosseno (DCT)

Transforma discreta de co- senos em 2-D : Espacial $\rightarrow$ frequência

$$
T [i, j]
=
c(i)c(j)
\sum_{x=0}^{N-1}
\sum_{y=0}^{N-1}
I [y, x]
\cos \frac{(2y+1) i\pi}{2N}
\cos \frac{(2x+1) j\pi}{2N}
$$

onde

$$
c(i), c(j) =
\begin{cases}
  \sqrt{\frac{2}{N}} & i, j \neq 0 \\
  \sqrt{\frac{1}{N}} & i, j = 0 \\
\end{cases}

$$

Transformada Inversa IDCT 2-D:

$$
I [y, x]
=
\sum_{i=0}^{N-1}
\sum_{j=0}^{N-1}
c(i)c(j)
T [i, j]
\cos \frac{(2y+1) i\pi}{2N}
\cos \frac{(2x+1) j\pi}{2N}
$$

Essa compressão é usada no formato JPEG padrão com valor de $N$ igual a 8.

### Compressão por Wavelets

Qualquer função, com período $2\pi$, pode ser reescrita como a soma dos termos da Série de Fourier:

$$

$$

Os coeficientes são calculados por:

$$

$$

#### Análise de Wavelet

- Ferramenta matemática para decomposição em nível hierárquico em aproximações (O) e detalhes (D).
- O nível hierárquico em escala diática (formado por potência de 2).
- Descrição de uma função em termos globais, mais termos que variam de detalhes globais até detalhes finos.
- A função em questão pode ser uma imagem, uma curva ou uma superfície.

<!-- Imagem -->
<!-- Imagem -->

#### Transformada de Wavelet Contínua (TWC)

A Transformada de Wavelets contínua em $F(a, b)$ é:

$F (a, b) =  f (t ) a ,b (t ) dt$

A função $a,b (t )$ é denominada *wavelet*:

$$
1 t −b
a , b (t ) =   , a  0 , b 
a  a 
$$

As funções wavelets são derivadas segundo os critérios:

$$
−1 2
ˆ (u ) du  
C = 2 \pi u 
$$

<!-- Imagem -->
<!-- Imagem -->
<!-- Imagem -->

#### Transformada de Wavelet Discreta

$$
t −b
a , b (t ) = ( j, k )  Z 2
1
 , a=2 ,b=k 2 ,
j j
a  a 
$$

- **Transformada Wavelet Haar Unidimensional**

| Resolução | Valor Aprox.   | Coef. Detalhes |
| --------- | -------------- | -------------- |
| 4         | [ 9, 7, 3, 5 ] |                |
| 2         | [ 8, 4 ]       | [ 1, -1 ]      |
| 1         | [ 6 ]          | [ 2 ]          |

[ 6, 2, 1, -1 ]

---

- Sequência de aproximação e coeficientes de detalhes

<!-- Ele pulou -->

Aproximação $V4$

Espaço de Imagem
$V $0  $V $1  $V $2 ...

Aproximação $V3$ Coeficientes de detalhes W3
Base de $V $j

i j ( x) =  (2 j x − i )
Aproximação $V2$ Coeficientes de detalhes W2
Espaço de Detalhes
W 0 $V $0 = $V $1

Aproximação $V1$ Coeficientes de detalhes W1 W 1 $V $1 = $V $2

Base de W j
 i j ( x) =  (2 j x − i )
Aproximação $V0$ Coeficientes de detalhes W0

### Bases Haar

### Normalidade

Uma função base $u(x)$ é normalizada se $\lang u|u \rang = 1$

- Haar normalizado:

$$
\phi
$$

$$
\Psi
$$

- Ex. para $[6, 2, 1, -1]$, se tornam normalizados:

$$
\begin{bmatrix}
  6 && 2 && \frac{1}{\sqrt{2}} && \frac{-1}{\sqrt{2}}
\end{bmatrix}
$$

### Algoritmo de Transformada Wavelet Haar

```python
Decomposi ( C[1...2^j ])
C c / sqrt (2 ^ j )     // normaliza coef inp
g 2 ^ j 
WHILE g >= 2  DO
DecomposiStep ( C [1 .. g ])
g g / 2
END
```

```python
DecomposiStep ( C[1...2^j ])
FOR i = 1 .. 2 ^ (j-1)
C’ ( C[2i – 1] + C[2i] ) / sqrt (2) 
C’[2^(j-1) + 1] (C[2i – 1] - C[2i] ) / sqrt (2)
END
C C’
```

```python
Reconstruc ( C[1...2^j ])
g 2
WHILE g =< 2 ^ j   DO
ReconstrucStep ( C [1 .. g ])
g 2g
END
C C sqrt ( 2 ^ j )   // sem normalização
```

```python
ReconstrucStep ( C[1...2^j ])
FOR i = 1 .. 2 ^ (j-1)
C’[ 2i – 1 ] ( C[ i ] + C[2 ^ (j-1) + i] ) / sqrt (2) 
C’[2i] (C[ i ] - C[2 ^ (j –i) + i ] ) / sqrt (2)
END
C C’
```

### Transformada de Wavelet de Haar bidimensional

- Imagens
  a. Decomposição padrão <!-- Imagem -->
  b. Decomposição não padrão. <!-- Imagem -->

### Compressão

O objetivo da compressão é expressar um conjunto inicial de dados usando outro conjunto menor, com ou sem perda de informação.

Seja a imagem $f(x)$ expressa pela soma de funções base:

$$
f ( x ) =  ci u i ( x )
i =1
$$

Com $m$ coeficientes $c_i$.
A função que aproxima $f(x)$, com menos coeficientes:

$$
\tilde{f}
=
\sum_{}^{\tilde{m}}
$$

### Aproximações e Detalhes

- Árvore de Decomposição *Wavelet* <!-- Imagem -->
- Árvore de Decomposição *Wavelet* de um sinal <!-- Imagem -->
