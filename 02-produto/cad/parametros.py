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
# Mecanismo (descrição do usuário, 2026-10-27, confirmado pela foto 08):
#   a haste roscada é UMA peça por lado, fixa no tambor do pivô e na barra; não gira.
#   O punho é a castanha: rosca interna curta embaixo e furo liso em cima. Girar o punho
#   muda o comprimento do aparelho. Dentro do punho há uma mola de compressão em volta da
#   haste, que continua para dentro do tubo da escala e apoia no porta-copo (o tubo é aberto
#   embaixo: uma mola só no punho não teria curso de 40 mm). O tubo é fixo ao porta-copo e entra
#   deslizando no punho; sob tração a mola comprime e a borda do punho aponta a força (lb).
ROSCA_D = 6.0            # FOTO  haste roscada, provavelmente M6 (porca 10 mm entre faces)
PORCA_AF = 10.0          # FOTO  porca sextavada (contraporca), medida entre faces
PORCA_ESP = 5.0          # FOTO
ROSCA_INF_EXPOSTA = 64.0 # FOTO  rosca visível entre a porca do pivô e o punho (foto 08; varia com o ajuste)
PUNHO_D = 26.0           # FOTO  punho serrilhado (castanha)
PUNHO_L = 68.0           # FOTO  (foto 08)
PUNHO_PORCA_L = 13.0     # EST   trecho com rosca interna, na parte de baixo do punho
PUNHO_FURO_D = 18.5      # EST   furo liso onde o tubo da escala desliza (folga de 0,25 mm no raio)
TUBO_MOLA_D = 18.0       # FOTO  tubo com a escala em libras (0 a 22 lb)
TUBO_MOLA_PAREDE = 1.0   # EST
TUBO_MOLA_VISIVEL = 50.0 # FOTO  trecho fora do punho em repouso
TUBO_DENTRO_PUNHO = 12.0 # EST   trecho dentro do punho em repouso; comprimento total = visível + dentro
CURSO_ESCALA = 40.0      # FOTO  deslocamento do 0 ao 22 lb (distância entre as marcas na foto 08)
ESCALA_LB_MAX = 22       # MED   especificação pública e impressa no tubo
MOLA_D_EXT = 15.0        # EST   mola de compressão em volta da haste (furo interno > 6 mm)
MOLA_ARAME_D = 1.6       # EST
MOLA_ESPIRAS = 14        # EST   espiras ativas (comprimento livre ~105 mm, 65 mm a 22 lb, bloco ~22 mm)
MOLA_K = ESCALA_LB_MAX * 4.448 / CURSO_ESCALA  # N/mm, calculado: ~2,4 N/mm (0,25 kgf/mm)
CARGA_LB = 0.0           # DEF   estado mostrado na montagem: 0 = repouso; 22 = escala toda
ROSCA_SUP_EXPOSTA = 40.0 # FOTO  rosca visível entre o porta-copo e a barra (foto 08), em repouso
ROSCA_NA_BARRA = 30.0    # EST   quanto a haste entra no cilindro da barra
ROSCA_NO_TAMBOR = 10.0   # EST   quanto a haste entra no tambor do pivô

# ---------- Porta-copo (um bloco por haste, entre o tubo da escala e a rosca superior) ----------
PORTA_LARG_X = 22.0      # FOTO  largura do bloco no sentido entre as hastes (foto 08)
PORTA_LARG_Y = 20.0      # EST   largura perpendicular; medir
PORTA_ESP = 13.0         # FOTO  espessura ao longo da haste (Z)
PORTA_BRACO_ESP = 8.0    # EST   espessura do braço curvo (Y)
PORTA_BRACO_X_PONTA = 18.0  # FOTO  distância do eixo do copo até a ponta do braço (onde a alça engancha)
PORTA_BRACO_Z_PONTA = -12.0 # FOTO  ponta do braço abaixo do centro do bloco (voltada para a base)

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
