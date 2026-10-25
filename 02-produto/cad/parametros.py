"""
Parâmetros dimensionais do extensor. Todas as medidas em milímetros.

ATENÇÃO: os valores abaixo são ESTIMATIVAS feitas a partir de fotos e das
especificações públicas do Epic Extender (copos de 28 a 44 mm, mangas de 21,
26 e 32 mm). Devem ser substituídos pelas medidas reais do levantamento em
02-produto/engenharia/mecanica/levantamento-dimensional.md.

Cada valor tem um status:  EST = estimado | MED = medido no produto real | DEF = definido por nós
"""

# ---------- Base (anel de apoio) ----------
BASE_D_EXT = 80.0        # EST  diâmetro externo do anel
BASE_D_INT = 50.0        # EST  diâmetro interno (passagem)
BASE_ESP = 12.0          # EST  espessura (altura) do anel
BASE_DIST_FUROS = 70.0   # EST  distância entre centros dos furos das hastes
BASE_LUG_D = 16.0        # EST  diâmetro das orelhas onde as hastes se fixam
BASE_FURO_D = 8.2        # EST  furo para a haste (rosca M8 na realidade)
BASE_ALMOFADA_ESP = 6.0  # EST  espessura da almofada

# ---------- Hastes ----------
HASTE_TUBO_D_EXT = 10.0  # EST  tubo externo
HASTE_TUBO_D_INT = 8.0   # EST
HASTE_TUBO_L = 90.0      # EST  comprimento do tubo externo
HASTE_INTERNA_D = 7.8    # EST  tubo/haste interna que desliza
HASTE_INTERNA_L = 90.0   # EST
HASTE_EXTENSAO = 40.0    # DEF  quanto a haste interna está estendida na montagem (0 = retraída)
HASTE_ROSCA_D = 8.0      # EST  pino rosqueado que entra na base
HASTE_ROSCA_L = 10.0     # EST
HASTE_FORCA_MAX_KGF = 5.0  # EST  por haste; Epic anuncia 22 lb (10 kg) no total

# ---------- Jugo (barra superior que une as hastes ao copo) ----------
JUGO_LARG = 16.0         # EST
JUGO_ESP = 8.0           # EST
JUGO_FURO_COPO_D = 10.2  # EST  furo onde o pino do copo encaixa

# ---------- Copos de vácuo ----------
COPO_TAMANHOS = [28, 32, 36, 40, 44]  # MED (especificação pública)  diâmetro interno
COPO_PAREDE = 2.5        # EST
COPO_ALTURA = 45.0       # EST  altura interna
COPO_TOPO_ESP = 4.0      # EST  espessura do fundo (lado do jugo)
COPO_PINO_D = 10.0       # EST  pino de engate no jugo
COPO_PINO_L = 12.0       # EST
COPO_BICO_D = 5.0        # EST  bico lateral para a bomba
COPO_BICO_L = 10.0       # EST
COPO_BICO_FURO_D = 2.5   # EST

# ---------- Membrana de silicone ----------
MEMB_ESP = 1.2           # EST
MEMB_FURO_FRACAO = 0.55  # EST  furo central como fração do diâmetro interno do copo
MEMB_ABA = 3.0           # EST  aba que abraça a borda do copo
MEMB_ABA_ALT = 6.0       # EST

# ---------- Mangas de silicone ----------
MANGA_TAMANHOS = [21, 26, 32]  # MED (especificação pública)  diâmetro interno
MANGA_PAREDE = 3.0       # EST
MANGA_L = 50.0           # EST
