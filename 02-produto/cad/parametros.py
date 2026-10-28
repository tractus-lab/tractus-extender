"""
Parâmetros dimensionais do extensor. Todas as medidas em milímetros.

Status de cada valor:
  FOTO = estimado a partir das fotos de 2026-10-27 sobre papel milimetrado (±2 mm em comprimentos;
         diâmetros saem 2 a 4 mm maiores por sombra e desfoque: punho 26→21,6, tubo 18→15,6 medidos)
  EST  = chute sem base fotográfica
  MED  = medido com paquímetro no produto real
  DEF  = definido por nós (não é medida do Epic)

Sistema de coordenadas da montagem: base no plano XY, hastes ao longo de +Z,
abertura da ferradura voltada para -Y. Eixo da articulação das hastes ao longo de X.
"""

# ---------- Acabamento ----------
RAIO_ARESTA = 2.0        # DEF   raio de arredondamento das arestas externas das peças grandes (requisito: nada pontudo)
RAIO_ARESTA_PEQ = 1.0    # DEF   idem, peças pequenas (olhais, tampas, boca do copo)

# ---------- Base (ferradura) ----------
BASE_R_EXT = 52.0        # FOTO  raio externo do arco (largura total ~106)
BASE_R_INT = 30.0        # FOTO  raio interno (abertura ~60)
BASE_ESP = 14.0          # EST   espessura total (altura em Z); medir
BASE_BORRACHA_ESP = 7.0  # EST   metade de baixo da ferradura, em borracha firme (contato com a virilha); metade de cima em plástico (usuário, 2026-10-27)
BASE_ABERTURA = 31.0     # FOTO  vão entre os lobos
BASE_LOBO_R = 15.0       # FOTO  raio dos lobos arredondados
BASE_LOBO_X = 32.0       # FOTO  posição X do centro de cada lobo
BASE_LOBO_Y = -36.0      # FOTO  posição Y do centro de cada lobo

# ---------- Articulação (pivô) ----------
# O pivô fica EM CIMA do lobo da ferradura, não dentro dele (usuário, 2026-10-27): uma caixa de
# articulação com rasgo, onde o tambor gira em torno de um pino transversal (eixo X). A cabeça do
# pino é escondida por uma tampa redonda de plástico na face externa da caixa.
HASTE_X = 41.5           # FOTO  meia distância entre hastes (entre eixos ~83)
PIVO_TAMBOR_D = 12.1     # MED   paquímetro (2026-10-27)
PIVO_TAMBOR_L = 31.0     # FOTO  comprimento total do tambor
PIVO_CAIXA_X = 17.6      # MED   largura da caixa de articulação no sentido do pino (paquímetro, 2026-10-27)
PIVO_CAIXA_Y = 20.0      # EST   profundidade da caixa (perpendicular ao pino); medir
PIVO_CAIXA_ALT = 16.0    # EST   altura da caixa acima da superfície da ferradura; medir
PIVO_PINO_ALT = 9.0      # EST   altura do eixo do pino acima da superfície da ferradura
PIVO_TAMBOR_ABAIXO_PINO = 6.0  # EST  quanto o tambor desce abaixo do eixo do pino
PIVO_RASGO = 13.0        # EST   largura do rasgo da caixa (tambor 12,1 + folga); sobra ~2,3 mm de parede por lado
PIVO_PINO_D = 4.0        # EST   pino transversal; medir
PIVO_TAMPA_D = 10.0      # EST   tampa redonda de plástico na face externa; medir
PIVO_TAMPA_ESP = 1.5     # EST

# ---------- Hastes (de baixo para cima) ----------
# Mecanismo (descrição do usuário, 2026-10-27, confirmado pela foto 08):
#   a haste roscada é UMA peça por lado, fixa no tambor do pivô e na barra; não gira.
#   O punho é a castanha: rosca interna curta embaixo e furo liso em cima. Girar o punho
#   muda o comprimento do aparelho. Dentro do punho há uma mola de compressão em volta da
#   haste, que continua para dentro do tubo da escala e apoia no porta-copo (o tubo é aberto
#   embaixo: uma mola só no punho não teria curso de 40 mm). O tubo é fixo ao porta-copo e entra
#   deslizando no punho; sob tração a mola comprime e a borda do punho aponta a força (lb).
ROSCA_D = 6.0            # MED   paquímetro 5,9 mm no Epic (2026-10-27) = M6 comercial; nominal 6,0
ROSCA_PASSO = 1.0        # MED   M6 x 1,0 (diâmetro 5,9 confirma; 10 voltas = 9,3 mm foi erro de régua)
PORCA_AF = 10.0          # FOTO  porca sextavada (contraporca), medida entre faces
PORCA_ESP = 5.0          # FOTO
ROSCA_INF_EXPOSTA = 64.0 # FOTO  rosca visível entre a porca do pivô e o punho (foto 08; varia com o ajuste)
PUNHO_D = 21.6           # MED   paquímetro (2026-10-27); a foto dava 26
PUNHO_L = 68.0           # FOTO  (foto 08)
PUNHO_PORCA_L = 13.0     # EST   trecho com rosca interna, na parte de baixo do punho
PUNHO_FURO_D = 16.1      # EST   furo liso onde o tubo da escala desliza (tubo 15,6 + folga)
TUBO_MOLA_D = 15.6       # MED   paquímetro (2026-10-27); a foto dava 18
TUBO_MOLA_PAREDE = 1.0   # EST
TUBO_MOLA_VISIVEL = 50.0 # FOTO  trecho fora do punho em repouso
TUBO_DENTRO_PUNHO = 12.0 # EST   trecho dentro do punho em repouso; comprimento total = visível + dentro
CURSO_ESCALA = 39.5      # MED   2 kg = 8,0 mm e 4 kg = 15,4 mm (régua, 2026-10-27) → 0,255 kgf/mm → 10 kg ≈ 39,5 mm
ESCALA_LB_MAX = 22       # MED   escala em libras numa face do tubo; na face oposta há escala em kg (0 a ~10)
MOLA_D_EXT = 12.5        # EST   mola em volta da haste M6, dentro do tubo (furo interno do tubo ~13,6)
MOLA_ARAME_D = 1.4       # EST
MOLA_ESPIRAS = 14        # EST   espiras ativas (comprimento livre ~105 mm, 65 mm a 22 lb, bloco ~22 mm)
MOLA_K = ESCALA_LB_MAX * 4.448 / CURSO_ESCALA  # MED   ~2,5 N/mm (0,255 kgf/mm); linear nos dois pontos medidos
CARGA_LB = 0.0           # DEF   estado mostrado na montagem: 0 = repouso; 22 = escala toda
ROSCA_SUP_EXPOSTA = 40.0 # FOTO  rosca visível entre o porta-copo e a barra (foto 08), em repouso
ROSCA_NA_BARRA = 30.0    # EST   quanto a haste entra no cilindro da barra
ROSCA_NO_TAMBOR = 10.0   # EST   quanto a haste entra no tambor do pivô

# ---------- Ponte (plataforma única entre as hastes, no topo dos tubos da escala) ----------
# Descrição do usuário: plataforma com um rebaixo circular no meio, aberto de um lado, onde
# encaixa a parte cilíndrica de cima do copo (o pescoço). A alça de arame não segura o copo.
PONTE_COMP = 112.0       # FOTO  comprimento em X (passa pelas duas hastes)
PONTE_LARG = 20.0        # EST   largura em Y; medir
PONTE_ESP = 13.0         # FOTO  espessura em Z
PONTE_ENTALHE_D = 14.0   # EST   diâmetro do rebaixo circular (pescoço 13 mm + folga); medir
PONTE_ENTALHE_LADO = -1  # EST   para que lado o entalhe abre: -1 = -Y (lado da abertura da ferradura), +1 = +Y
PONTE_FURO_HASTE_D = 6.6 # EST   furo liso: a ponte desliza na haste

# ---------- Barra superior "EPIC" ----------
BARRA_BOSS_D = 16.0      # FOTO  cilindros das pontas
BARRA_BOSS_L = 39.0      # FOTO  (foto 08)
BARRA_TIRA_ESP = 4.0     # EST   espessura da tira entre os cilindros
BARRA_TIRA_ALT = 17.0    # FOTO  altura da tira (em Z)
BARRA_TIRA_DESLOC_Y = -6.0  # EST  tira deslocada para um lado do eixo das hastes
BARRA_OLHAL_D = 11.0     # FOTO  olhal nas pontas
BARRA_OLHAL_FURO_D = 5.0 # FOTO
BARRA_OLHAL_ESP = 4.0    # EST

# ---------- Copo de vácuo (o fotografado; tamanho a confirmar) ----------
COPO_TAMANHOS = [28, 32, 36, 40, 44]  # MED  especificação pública (diâmetro interno)
COPO_FOTO_D_EXT = 39.4   # MED   diâmetro EXTERNO do corpo (paquímetro, 2026-10-27); foto dava 47
COPO_PAREDE = 2.5        # EST
COPO_SINO_L = 43.6       # MED   altura do sino (cilindro + domo), sem pescoço e válvula (paquímetro, 2026-10-27)
COPO_DOMO_L = 14.0       # EST   altura do domo (parte abaulada, formato de glande); cilindro = sino - domo
COPO_CORPO_L = COPO_SINO_L - COPO_DOMO_L  # parte cilíndrica, onde ficam os anéis e a manga
COPO_OVAL = 0.93         # EST   seção levemente oval: diâmetro em Y = COPO_OVAL x diâmetro em X (usuário: "meio oval")
COPO_OMBRO_L = COPO_DOMO_L  # compatibilidade: o antigo ombro cônico virou domo
COPO_ANEIS_N = 3         # FOTO  anéis externos junto à boca
COPO_ANEIS_PASSO = 9.5   # FOTO
COPO_ANEIS_ALT = 2.0     # EST   quanto o anel sobressai
COPO_ANEIS_LARG = 2.0    # EST
COPO_PESCOCO_D = 13.0    # FOTO
COPO_PESCOCO_L = 7.0     # FOTO
VALVULA_D = 20.0         # FOTO  corpo da válvula (branco, com marca vermelha) (válvula GIRATÓRIA: abre/fecha a passagem de ar para a sucção; geometria interna a levantar)
VALVULA_L = 28.0         # FOTO
# Alça de arame do copo: não modelada (é de outro sistema de tração; fora do projeto)

# ---------- Membrana e mangas (ainda não fotografadas) ----------
MEMB_ESP = 1.2           # EST
MEMB_FURO_FRACAO = 0.55  # EST
MANGA_TAMANHOS = [21, 26, 32]  # MED  especificação pública
MANGA_PAREDE = 2.5       # MED   paquímetro (2026-10-27)
MANGA_L = 83.4           # MED   altura (paquímetro, 2026-10-27)
MANGA_FOTO_D = 27.4      # MED   diâmetro INTERNO em repouso = 32,4 externo (paquímetro, 2026-10-27) - 2 x 2,5 de parede; estica ~44% para vestir o copo de 39,4
MANGA_SOBRE_COPO = 25.0  # EST   quanto a manga sobe sobre a boca do copo (cobre os 3 anéis)
MANGA_TRANSICAO = 8.0    # EST   trecho em que a manga passa do diâmetro esticado ao de repouso (foto 09)
