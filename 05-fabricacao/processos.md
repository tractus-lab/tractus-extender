# Como uma fábrica produz uma peça no formato que a gente desenhou

Resumo para quem nunca mandou fabricar nada. O que a fábrica recebe de nós, o que ela faz com isso e o que precisa
estar no desenho para dar certo. Processos na ordem em que aparecem no nosso BOM.

## O que a gente entrega

- **Modelo 3D** em STEP (o `gerar.py` já exporta). É a forma exata, sem ambiguidade. É o arquivo que entra na máquina.
- **Desenho 2D** em PDF com as cotas que importam, tolerâncias (ex.: furo 6,0 +0,1/0), material, acabamento e
  quantidade. É o contrato: é o que o controle de qualidade mede.
- Para corte a laser: **DXF** plano, escala 1:1, só o contorno e os furos.
- Para impressão 3D: **STL** ou STEP, mais o material.
- Para mola: desenho com arame, diâmetro externo, espiras, comprimento livre, constante k e material.

## Injeção de plástico (ferradura, punhos, tampas)

1. A **ferramentaria** recebe o STEP e projeta o **molde**: dois blocos de aço (ou alumínio, para lotes pequenos)
   com uma cavidade que é o negativo da peça. O projetista decide onde fica a **linha de partição** (onde o molde
   abre), por onde o plástico entra (**canal e ponto de injeção**), por onde o ar sai e onde ficam os **pinos
   extratores** que empurram a peça para fora.
2. A cavidade é feita por **fresa CNC** (a máquina lê o modelo e remove metal) e, nos detalhes finos e cantos
   internos, por **eletroerosão** (um eletrodo de grafite com a forma do detalhe "queima" o aço). Depois polimento
   à mão ou **texturização** química (a textura levemente fosca das peças pretas do Epic vem daí).
3. A **injetora** fecha o molde com toneladas de força, derrete o plástico granulado numa rosca aquecida, injeta sob
   pressão, esfria 10 a 40 s, abre e extrai. Um ciclo por peça (ou por 2, 4, 8, se o molde tiver várias cavidades).
4. O molde custa caro (R$ 20 a 50 mil para a ferradura) e demora 4 a 8 semanas; a peça depois custa centavos a
   poucos reais. É por isso que injeção só faz sentido com volume.

O que o desenho precisa respeitar, senão a ferramentaria devolve:
- **Ângulo de saída** de 1 a 2° nas paredes verticais, para a peça soltar do molde.
- **Espessura de parede uniforme** (2 a 3 mm em nylon/ABS); massa grossa encolhe e afunda ("rechupe"). A ferradura
  do Epic é oca por dentro por esse motivo.
- **Nada de rebaixos** (negativos) que travem a abertura, ou o molde precisa de gavetas, que custam mais.
- **Raios** nos cantos internos; canto vivo concentra tensão e quebra.
- **Contração**: o plástico encolhe 0,5 a 2 % ao esfriar; a ferramentaria aumenta a cavidade para compensar. A gente
  informa o material e eles calculam.

## Sobremoldagem (borracha da ferradura)

Mesmo processo, em dois tiros: a peça rígida é injetada, vai para um segundo molde (ou o mesmo molde gira) e o
TPE/silicone é injetado por cima. Precisa de dois moldes. Alternativa barata: moldar a borracha à parte (compressão)
e colar ou encaixar com rebaixos.

## Moldagem de silicone (mangas, face da ferradura)

- **Compressão (HTV)**: uma "massa" de silicone pré-pesada é posta num molde de alumínio quente, prensada e
  vulcanizada por alguns minutos. Molde simples e barato (R$ 5 a 20 mil), ciclo lento, rebarba para tirar à mão. Serve
  para mangas e discos.
- **Injeção de silicone líquido (LSR)**: dois componentes misturados e injetados num molde quente, igual ao plástico.
  Molde mais caro, peça sem rebarba, boa para volume e para grau médico.
- Silicone é flexível, então rebaixos leves são permitidos (a peça é arrancada do molde). Ângulo de saída quase não
  importa.

## Impressão 3D industrial (MJF/SLS), para protótipos e lotes de dezenas a centenas

Não tem molde. A máquina lê o STL, espalha pó de nylon camada por camada (0,08 mm) e funde onde a peça existe.
Qualquer forma, inclusive rebaixos e cavidades internas. Custo por cm³ e não por molde, então uma peça custa igual à
milésima. Tolerância ±0,3 mm e superfície levemente áspera. É a rota A do BOM.

## Torneamento CNC (tambor do pivô)

Um tarugo de inox gira e a ferramenta remove material seguindo um programa gerado do STEP (**CAM**). Rosca interna é
feita com macho ou interpolada. A lingueta do tambor exige uma fresa (centro de usinagem) ou um torno com ferramenta
motorizada. Sem molde; o custo é tempo de máquina, por isso R$ 8 a 15 por peça em lote e R$ 60 a 120 avulso.

## Corte a laser e dobra (ponte, barra superior)

A chapa de alumínio deita na mesa e um laser de fibra segue o DXF; furos e contornos saem na mesma passada, com
±0,1 mm. Depois uma **dobradeira** faz os dois "[" da barra com um raio interno de ~1× a espessura. Anodização preta
é feita por outra empresa (banho eletroquímico). Sem molde, custo baixo mesmo em 10 peças.

## Molas

Uma **enroladeira CNC** puxa o arame e enrola com diâmetro, passo e número de espiras programados; corta, e as molas
vão para o forno de alívio de tensões e depois têm as pontas esmerilhadas para ficarem planas. Mandando o desenho
com k, diâmetro e comprimento, a fábrica programa em minutos; o custo alto em pequena quantidade é o setup.

## Tubo da escala

Tubo extrudado padrão, cortado na serra, pontas rebarbadas, anodizado preto e com a escala gravada a laser (o laser
remove a camada preta e aparece o alumínio claro). Três fornecedores diferentes, ou uma serralheria que subcontrata.

## O que fazer antes de pedir cotação

1. Fechar o STEP de cada peça com ângulos de saída e espessuras já ajustados para o processo escolhido (o CAD atual é
   réplica funcional do Epic, ainda sem essa revisão de DFM).
2. Gerar o desenho 2D com cotas críticas: furos dos pivôs, rosca, encaixe do copo na ponte, abertura da ferradura.
3. Mandar o mesmo pacote para 2 ou 3 fábricas por processo e pedir preço para 50, 500 e 2.000.
4. Pedir sempre uma **amostra** (T1, primeira injeção) antes de aprovar o lote.
