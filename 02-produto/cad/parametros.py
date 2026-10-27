"""
Parâmetros dimensionais do extensor. Todas as medidas em milímetros.

Status de cada valor:
  FOTO = estimado a partir das fotos de 2026-10-27 sobre papel milimetrado (±2 mm)
  EST  = chute sem base fotográfica
  MED  = medido com paquímetro no produto real
  DEF  = definido por nós (não é medida do Epic)

Sistema de coordenadas da montagem: base no plano XY, hastes ao longo de +Z,
abertura da ferradura voltada para -Y. Eixo da articulação das hastes ao longo de X.
"""

# ---------- Base (ferradura) ----------
BASE_R_EXT = 52.0        # FOTO  raio externo do arco (largura total ~106)
BASE_R_INT = 30.0        # FOTO  raio interno (abertura ~60)
BASE_ESP = 14.0          # EST   espessura (altura em Z); medir
BASE_ABERTURA = 31.0     # FOTO  vão entre os lobos
BASE_LOBO_R = 15.0       # FOTO  raio dos lobos arredondados
BASE_LOBO_X = 32.0       # FOTO  posição X do centro de cada lobo
BASE_LOBO_Y = -36.0      # FOTO  posição Y do centro de cada lobo

# ---------- Articulação (pivô) ----------
HASTE_X = 41.5           # FOTO  meia distância entre hastes (entre eixos ~83)
PIVO_TAMBOR_D = 12.0     # FOTO  tambor de inox onde a haste rosqueia
PIVO_TAMBOR_L = 31.0     # FOTO
PIVO_TAMBOR_DENTRO = 10.0  # EST  quanto do tambor fica dentro do rasgo da base
PIVO_RASGO = 13.0        # EST  largura do rasgo na base
PIVO_PINO_D = 4.0        # EST  pino da articulação (eixo X)
PIVO_PINO_L = 26.0       # EST

# ---------- Hastes (de baixo para cima) ----------
ROSCA_D = 6.0            # FOTO  haste roscada, provavelmente M6 (porca 10 mm entre faces)
PORCA_AF = 10.0          # FOTO  porca sextavada, medida entre faces
PORCA_ESP = 5.0          # FOTO
ROSCA_INF_EXPOSTA = 53.0 # FOTO  rosca visível entre a porca do pivô e o punho
PUNHO_D = 26.0           # FOTO  punho serrilhado (porca longa de ajuste)
PUNHO_L = 65.0           # FOTO
TUBO_MOLA_D = 18.0       # FOTO  tubo com a escala em libras (0 a 22 lb)
TUBO_MOLA_L = 50.0       # FOTO
TUBO_SOBRE_PUNHO = 0.0   # DEF   quanto o tubo desliza sobre o punho (mola comprimida); 0 = sem carga
ROSCA_SUP_EXPOSTA = 43.0 # FOTO  rosca visível entre a guia central e a barra
ESCALA_LB_MAX = 22       # MED   especificação pública e impressa no tubo

# ---------- Guia central (peça de duas metades no topo dos tubos) ----------
GUIA_COMP = 112.0        # FOTO  comprimento total em X
GUIA_LARG = 20.0         # EST   largura em Y; medir
GUIA_ESP = 13.0          # FOTO  espessura em Z
GUIA_FURO_CENTRAL_D = 13.0  # FOTO  entalhe central (provável passagem do pescoço do copo)

# ---------- Barra superior "EPIC" ----------
BARRA_BOSS_D = 16.0      # FOTO  cilindros das pontas
BARRA_BOSS_L = 38.0      # FOTO
BARRA_TIRA_ESP = 4.0     # EST   espessura da tira entre os cilindros
BARRA_TIRA_ALT = 17.0    # FOTO  altura da tira (em Z)
BARRA_TIRA_DESLOC_Y = -6.0  # EST  tira deslocada para um lado do eixo das hastes
BARRA_OLHAL_D = 11.0     # FOTO  olhal nas pontas
BARRA_OLHAL_FURO_D = 5.0 # FOTO
BARRA_OLHAL_ESP = 4.0    # EST

# ---------- Copo de vácuo (o fotografado; tamanho a confirmar) ----------
COPO_TAMANHOS = [28, 32, 36, 40, 44]  # MED  especificação pública (diâmetro interno)
COPO_FOTO_D_EXT = 47.0   # FOTO  diâmetro externo do corpo do copo fotografado
COPO_PAREDE = 2.5        # EST
COPO_CORPO_L = 44.0      # FOTO  altura da parte cilíndrica
COPO_OMBRO_L = 7.0       # FOTO  transição cônica até o pescoço
COPO_ANEIS_N = 3         # FOTO  anéis externos junto à boca
COPO_ANEIS_PASSO = 9.5   # FOTO
COPO_ANEIS_ALT = 2.0     # EST   quanto o anel sobressai
COPO_ANEIS_LARG = 2.0    # EST
COPO_PESCOCO_D = 13.0    # FOTO
COPO_PESCOCO_L = 7.0     # FOTO
VALVULA_D = 20.0         # FOTO  corpo da válvula (branco, com marca vermelha)
VALVULA_L = 28.0         # FOTO
ALCA_ARAME_D = 2.0       # FOTO  alça de arame inox
ALCA_COMP = 39.0         # FOTO  do corpo da válvula até o ápice
ALCA_LARG = 33.0         # FOTO  largura na base do triângulo

# ---------- Membrana e mangas (ainda não fotografadas) ----------
MEMB_ESP = 1.2           # EST
MEMB_FURO_FRACAO = 0.55  # EST
MANGA_TAMANHOS = [21, 26, 32]  # MED  especificação pública
MANGA_PAREDE = 3.0       # EST
MANGA_L = 50.0           # EST
