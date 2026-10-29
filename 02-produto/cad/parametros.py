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
BASE_R_EXT = 48.0        # MED   raio externo do arco: largura externa 96 mm (paquímetro, 2026-10-28)
BASE_R_INT = 27.8        # MED   raio interno = 48 − 20,2 (faixa do arco com 20,2 mm de largura radial, paquímetro, 2026-10-28)
BASE_ESP = 18.0          # MED   altura total da ferradura em Z, plástico + borracha (paquímetro, 2026-10-28)
BASE_BORRACHA_ESP = 9.0  # EST   metade de baixo da ferradura, em borracha firme (contato com a virilha); metade de cima em plástico (usuário, 2026-10-27)
# Forma em planta (foto 07): anel + braço reto descendo inclinado para dentro + pá arredondada apontando para a abertura.
# O furo central fica em "buraco de fechadura": redondo em cima e um pescoço estreito entre as pás.
BASE_BRACO_Y0 = -9.0     # EST   onde o braço sai do anel (abaixo dos garfos do pivô, que ficam em y=0)
BASE_BRACO_Y1 = -20.0    # EST   onde o braço vira pá
BASE_PONTA_Y = -32.0     # FOTO  ponta das pás (altura total em planta ~80 mm; foto 07, perspectiva)
BASE_PA_X = 21.5         # FOTO  centro de cada pá em X
BASE_PA_LARG = 21.0      # FOTO  largura da pá
BASE_PA_INCL = 10.0      # EST   inclinação da pá, ponta virada para fora (graus)
BASE_R_JUNCAO = 10.0     # EST   raio das curvas em S nas junções anel–braço–pá
BASE_ABERTURA = 2 * (BASE_PA_X - BASE_PA_LARG / 2)  # 22: pescoço entre as pás (foto 07; antes 31, de outra foto)

# ---------- Articulação (pivô) ----------
# O pivô fica EM CIMA do lobo da ferradura, não dentro dele (usuário, 2026-10-27): uma caixa de
# articulação com rasgo, onde o tambor gira em torno de um pino transversal (eixo X). A cabeça do
# pino é escondida por uma tampa redonda de plástico na face externa da caixa.
HASTE_X = 37.85          # MED   meia distância entre eixos das hastes: 81,6 de borda externa a externa − 5,9 de rosca = 75,7 (paquímetro, 2026-10-28); a foto dava 83
PIVO_TAMBOR_D = 12.1     # MED   paquímetro (2026-10-27)
PIVO_TAMBOR_L = 31.0     # FOTO  comprimento total do tambor
PIVO_CAIXA_X = 14.8      # MED   largura do garfo no sentido do pino = 2 bochechas de 4,2 + lingueta de 5,6 + 0,8 de folga (paquímetro, 2026-10-28)
PIVO_CAIXA_Y = 17.6      # MED   comprimento do garfo no sentido da rotação, perpendicular ao pino (paquímetro, 2026-10-28)
PIVO_BOCHECHA_ESP = 4.2  # MED   espessura de cada bochecha (lado) do garfo onde o tambor se conecta (paquímetro, 2026-10-28)
PIVO_LINGUETA_ESP = 5.6  # MED   espessura da lingueta: ponta do tambor rebaixada com dois chanfros planos, entra entre as bochechas (paquímetro, 2026-10-28)
PIVO_GARFO_VAO = PIVO_CAIXA_X - 2 * PIVO_BOCHECHA_ESP  # 6,4: vão entre as bochechas; 0,4 mm de folga por lado da lingueta
PIVO_CAIXA_ALT = 16.0    # EST   altura da caixa acima da superfície da ferradura; medir
PIVO_PINO_ALT = 9.0      # EST   altura do eixo do pino acima da superfície da ferradura
PIVO_TAMBOR_ABAIXO_PINO = 6.0  # EST  quanto a lingueta desce abaixo do eixo do pino (ponta arredondada nesse raio)
PIVO_LINGUETA_L = PIVO_TAMBOR_ABAIXO_PINO + PIVO_CAIXA_Y / 2 + 1.0  # comprimento rebaixado do tambor: passa do topo arredondado do garfo para poder girar
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
ROSCA_COM_FIO = True     # DEF   modelar o fio helicoidal ISO de verdade (bd_warehouse); False = cilindro liso, mais leve e rápido
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
# Encaixe do copo (usuário, 2026-10-27): rasgo em U, aberto de um lado, por onde o pescoço entra; na
# face de cima, um rebaixo circular FECHADO onde o corpo da válvula assenta. O pescoço é mais alto que
# o piso do rebaixo, então o copo tem folga para subir e descer. Sob tração o copo desce, a válvula
# assenta no rebaixo e o copo fica preso (não sai pelo lado). Com folga, sobe e sai pelo rasgo.
PONTE_COMP = 2 * HASTE_X + 29.0  # FOTO  comprimento em X: ~14,5 mm além de cada haste (foto); acompanha o entre-eixos medido
PONTE_LARG = 20.0        # EST   largura em Y; medir
PONTE_ESP = 4.5          # MED   espessura da chapa (paquímetro, 2026-10-27)
PONTE_CUBO_ESP = 13.0    # FOTO  altura do cubo em volta de cada haste (o que a foto 08 mostrava como bloco de 13 mm); a confirmar
PONTE_CUBO_D = 20.0      # EST   diâmetro do cubo em volta da haste
PONTE_ENTALHE_D = 12.0   # MED   furo/rasgo por onde passa o pescoço (paquímetro, 2026-10-27)
PONTE_ENTALHE_LADO = -1  # EST   para que lado o rasgo abre: -1 = -Y (lado da abertura da ferradura), +1 = +Y
PONTE_REBAIXO_D = 20.0   # MED   diâmetro do rebaixo circular (paquímetro, 2026-10-27); o encaixe do copo tem o mesmo tamanho, com folga pequena
PONTE_REBAIXO_PROF = 1.5 # MED   chapa 4,5 - 3,0 no rebaixo (paquímetro, 2026-10-27)
PONTE_FURO_HASTE_D = 6.6 # EST   furo liso: a ponte desliza na haste

# ---------- Barra superior "EPIC" ----------
BARRA_BOSS_D = 16.0      # FOTO  cilindros das pontas
BARRA_BOSS_L = 39.0      # FOTO  (foto 08)
BARRA_TIRA_ESP = 4.0     # EST   espessura da tira entre os cilindros
BARRA_TIRA_ALT = 17.0    # FOTO  altura da tira (em Z)
BARRA_TIRA_DESLOC_Y = -27.6  # MED  desvio da tira para fora do plano das hastes (usuário, 2026-10-28): a tira sai de cada cilindro,
                             #      anda 27,6 mm para o lado e só então cruza de um lado ao outro, formando um '[' visto de cima.
                             #      Sem isso a tira bateria na válvula do copo quando a ponte sobe. Lado (−Y, o da abertura da ponte): EST
BARRA_DOBRA_R = 3.0          # EST  raio das dobras da tira em planta
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
COPO_PESCOCO_D = 11.5    # EST   passa no furo de 12 da ponte com folga
COPO_PESCOCO_L = 7.0     # FOTO  mais alto que o piso do rebaixo (3 mm): sobra ~4 mm para o copo subir e sair pelo rasgo; medir
VALVULA_D = 19.9         # DEF   encaixe do copo no rebaixo de 20 da ponte com 0,1 mm de folga no diâmetro (usuário, 2026-10-27)
COPO_FOLGA_ASSENTO = 0.1 # DEF   folga vertical entre o corpo da válvula e o piso do rebaixo na montagem (usuário: não ficar rente)
VALVULA_L = 28.0         # FOTO
# Alça de arame do copo: não modelada (é de outro sistema de tração; fora do projeto)

# ---------- Membrana e mangas (ainda não fotografadas) ----------
MEMB_ESP = 1.2           # EST
MEMB_FURO_FRACAO = 0.55  # EST
MANGA_TAMANHOS = [21, 26, 32]  # MED  especificação pública
MANGA_PAREDE = 2.5       # MED   paquímetro (2026-10-27)
MANGA_L = 83.4           # MED   altura (paquímetro, 2026-10-27)
MANGA_FOTO_D = 27.4      # MED   diâmetro INTERNO em repouso = 32,4 externo (paquímetro, 2026-10-27) - 2 x 2,5 de parede; estica ~44% para vestir o copo de 39,4
MANGA_SOBRE_COPO = 25.0  # DEF   quanto a manga sobe sobre a boca do copo; posição arbitrária no uso real (usuário, 2026-10-28), só precisa cobrir os 3 anéis
MANGA_TRANSICAO = 8.0    # EST   trecho em que a manga passa do diâmetro esticado ao de repouso (foto 09)
