"""Peças do extensor em build123d (modo álgebra), versão 0.5 (ponte única com entalhe para o pescoço do copo)."""
from build123d import *
import parametros as P


def _cil_entre(p1, p2, d):
    """Cilindro de diâmetro d entre dois pontos (para a alça de arame)."""
    p1, p2 = Vector(*p1), Vector(*p2)
    v = p2 - p1
    return Plane(origin=p1 + v / 2, z_dir=v) * Cylinder(d / 2, v.length)


def _porca(af, esp):
    return extrude(RegularPolygon(af / 2 / 0.8660254, 6), esp)


# ---------------- Base ----------------
def base():
    """Ferradura com lobos e rasgos para os tambores do pivô. Centrada em Z."""
    h = P.BASE_ESP
    b = Cylinder(P.BASE_R_EXT, h) - Cylinder(P.BASE_R_INT, h)
    # abertura entre os lobos
    b -= Pos(0, -(P.BASE_R_EXT + 10) / 2, 0) * Box(P.BASE_ABERTURA, P.BASE_R_EXT + 10, h + 2)
    for sx in (-1, 1):
        b += Pos(sx * P.BASE_LOBO_X, P.BASE_LOBO_Y, 0) * Cylinder(P.BASE_LOBO_R, h)
    # rasgos onde os tambores do pivô se alojam (abertos para cima e para +Y)
    for sx in (-1, 1):
        b -= Pos(sx * P.HASTE_X, P.PIVO_RASGO / 2, 0) * Box(P.PIVO_RASGO, P.PIVO_RASGO * 2, h + 2)
    return b


def pivo_tambor():
    """Tambor de inox que recebe a rosca da haste. Origem na base do tambor, eixo Z."""
    t = Pos(0, 0, P.PIVO_TAMBOR_L / 2) * Cylinder(P.PIVO_TAMBOR_D / 2, P.PIVO_TAMBOR_L)
    t -= Pos(0, 0, P.PIVO_TAMBOR_L / 2) * Cylinder(P.ROSCA_D / 2, P.PIVO_TAMBOR_L)
    return t


def pivo_pino():
    return Rot(0, 90, 0) * Cylinder(P.PIVO_PINO_D / 2, P.PIVO_PINO_L)


# ---------------- Haste ----------------
def porca():
    return _porca(P.PORCA_AF, P.PORCA_ESP)


def rosca(comp):
    """Haste roscada (fuso), uma peça por lado, modelada lisa. Nome comercial: barra roscada M6 inox 304.
    Origem na base, eixo Z."""
    return Pos(0, 0, comp / 2) * Cylinder(P.ROSCA_D / 2, comp)


def punho():
    """Punho serrilhado = castanha. Rosca interna curta embaixo (modelada como furo de 6 mm) e
    furo liso de PUNHO_FURO_D em cima, onde a mola fica e o tubo da escala desliza. Origem na base."""
    p = Pos(0, 0, P.PUNHO_L / 2) * Cylinder(P.PUNHO_D / 2, P.PUNHO_L)
    p -= Pos(0, 0, P.PUNHO_PORCA_L / 2) * Cylinder(P.ROSCA_D / 2, P.PUNHO_PORCA_L)
    furo_l = P.PUNHO_L - P.PUNHO_PORCA_L
    p -= Pos(0, 0, P.PUNHO_PORCA_L + furo_l / 2 + 0.5) * Cylinder(P.PUNHO_FURO_D / 2, furo_l + 1)
    return p


def tubo_mola():
    """Tubo da escala: aberto nas duas pontas (a mola passa por dentro), fixo à ponte em cima.
    Entra deslizando no punho. Origem na ponta de baixo, eixo Z."""
    L = P.TUBO_MOLA_VISIVEL + P.TUBO_DENTRO_PUNHO
    t = Pos(0, 0, L / 2) * Cylinder(P.TUBO_MOLA_D / 2, L)
    t -= Pos(0, 0, L / 2) * Cylinder(P.TUBO_MOLA_D / 2 - P.TUBO_MOLA_PAREDE, L + 1)
    return t


def mola(comp):
    """Mola helicoidal de compressão com o comprimento dado (varia com a carga). Origem na base, eixo Z."""
    passo = (comp - P.MOLA_ARAME_D) / P.MOLA_ESPIRAS
    r = (P.MOLA_D_EXT - P.MOLA_ARAME_D) / 2
    caminho = Helix(pitch=passo, height=comp - P.MOLA_ARAME_D, radius=r)
    secao = Plane(origin=caminho @ 0, z_dir=caminho % 0) * Circle(P.MOLA_ARAME_D / 2)
    return Pos(0, 0, P.MOLA_ARAME_D / 2) * sweep(secao, caminho)


def ponte():
    """Plataforma única entre as hastes. Furos lisos para as hastes e, no meio, um rebaixo circular
    aberto para um lado, onde o pescoço do copo encaixa. Centrada na origem."""
    g = Box(P.PONTE_COMP, P.PONTE_LARG, P.PONTE_ESP)
    for sx in (-1, 1):
        g -= Pos(sx * P.HASTE_X, 0, 0) * Cylinder(P.PONTE_FURO_HASTE_D / 2, P.PONTE_ESP + 1)
    g -= Cylinder(P.PONTE_ENTALHE_D / 2, P.PONTE_ESP + 1)
    g -= Pos(0, P.PONTE_ENTALHE_LADO * P.PONTE_LARG / 2, 0) * Box(P.PONTE_ENTALHE_D, P.PONTE_LARG, P.PONTE_ESP + 1)
    return g


def barra_superior():
    """Barra 'EPIC': dois cilindros com olhais, unidos por uma tira. Origem na base dos cilindros."""
    L = P.BARRA_BOSS_L
    b = None
    for sx in (-1, 1):
        boss = Pos(sx * P.HASTE_X, 0, L / 2) * Cylinder(P.BARRA_BOSS_D / 2, L)
        boss -= Pos(sx * P.HASTE_X, 0, L / 2) * Cylinder(P.ROSCA_D / 2, L)
        x_olhal = sx * (P.HASTE_X + P.BARRA_BOSS_D / 2 + P.BARRA_OLHAL_D / 2 - 2)
        olhal = Pos(x_olhal, 0, L - P.BARRA_OLHAL_D / 2) * Rot(90, 0, 0) * Cylinder(P.BARRA_OLHAL_D / 2, P.BARRA_OLHAL_ESP)
        olhal -= Pos(x_olhal, 0, L - P.BARRA_OLHAL_D / 2) * Rot(90, 0, 0) * Cylinder(P.BARRA_OLHAL_FURO_D / 2, P.BARRA_OLHAL_ESP + 1)
        b = boss + olhal if b is None else b + boss + olhal
    tira = Pos(0, P.BARRA_TIRA_DESLOC_Y, L / 2) * Box(2 * P.HASTE_X, P.BARRA_TIRA_ESP, P.BARRA_TIRA_ALT)
    return b + tira


# ---------------- Copo ----------------
def copo(d_ext=None):
    """Copo em forma de sino com anéis na boca, pescoço, válvula e alça de arame.
    Boca em z=0 voltada para -Z; o copo se estende para +Z."""
    d_ext = d_ext or P.COPO_FOTO_D_EXT
    r = d_ext / 2
    ri = r - P.COPO_PAREDE
    rp = P.COPO_PESCOCO_D / 2
    Lc, Lo, Lp = P.COPO_CORPO_L, P.COPO_OMBRO_L, P.COPO_PESCOCO_L
    perfil_ext = [(0, 0), (r, 0), (r, Lc), (rp, Lc + Lo), (rp, Lc + Lo + Lp), (0, Lc + Lo + Lp)]
    perfil_int = [(0, -1), (ri, -1), (ri, Lc - 1), (rp - 1.5, Lc + Lo - 2), (rp - 1.5, Lc + Lo + Lp + 1), (0, Lc + Lo + Lp + 1)]
    solido = revolve(Plane.XZ * Polygon(*perfil_ext, align=None), Axis.Z)
    cav = revolve(Plane.XZ * Polygon(*perfil_int, align=None), Axis.Z)
    c = solido - cav
    for i in range(P.COPO_ANEIS_N):
        z = 3 + i * P.COPO_ANEIS_PASSO
        c += Pos(0, 0, z) * (Cylinder(r + P.COPO_ANEIS_ALT, P.COPO_ANEIS_LARG) - Cylinder(r - 0.1, P.COPO_ANEIS_LARG))
    z_valv = Lc + Lo + Lp
    c += Pos(0, 0, z_valv + P.VALVULA_L / 2) * Cylinder(P.VALVULA_D / 2, P.VALVULA_L)
    # alça triangular de arame, no plano XZ, presa ao corpo da válvula
    z_pe = z_valv + P.VALVULA_L * 0.35
    apice = (0, 0, z_valv + P.ALCA_COMP)
    pe_e = (-P.ALCA_LARG / 2, 0, z_pe)
    pe_d = (P.ALCA_LARG / 2, 0, z_pe)
    d = P.ALCA_ARAME_D
    c += _cil_entre(pe_e, apice, d) + _cil_entre(pe_d, apice, d)
    c += _cil_entre(pe_e, pe_d, d)  # travessa que atravessa o corpo da válvula
    c += Pos(*apice) * Sphere(d / 2)
    return c


def membrana(d_ext=None):
    """Membrana de silicone sobre a boca (geometria ainda não observada)."""
    d_ext = d_ext or P.COPO_FOTO_D_EXT
    r = d_ext / 2 + P.COPO_ANEIS_ALT + 1
    m = Pos(0, 0, -P.MEMB_ESP / 2) * Cylinder(r, P.MEMB_ESP)
    m -= Cylinder((d_ext - 2 * P.COPO_PAREDE) * P.MEMB_FURO_FRACAO / 2, 10)
    return m


def manga(d_int):
    return Pos(0, 0, P.MANGA_L / 2) * (Cylinder(d_int / 2 + P.MANGA_PAREDE, P.MANGA_L) - Cylinder(d_int / 2, P.MANGA_L))


# ---------------- Montagem ----------------
def montagem(com_copo=True, carga_lb=None):
    """Conjunto em posição de uso: hastes perpendiculares à base. carga_lb desloca o tubo
    para dentro do punho (0 = repouso, ESCALA_LB_MAX = curso todo)."""
    carga = P.CARGA_LB if carga_lb is None else carga_lb
    desloc = P.CURSO_ESCALA * carga / P.ESCALA_LB_MAX
    partes = [("base", base())]
    z_base_topo = P.BASE_ESP / 2
    z_tambor0 = z_base_topo - P.PIVO_TAMBOR_DENTRO
    z = {}
    for nome, sx in (("esq", -1), ("dir", 1)):
        x = sx * P.HASTE_X
        partes.append((f"pivo_tambor_{nome}", Pos(x, 0, z_tambor0) * pivo_tambor()))
        partes.append((f"pivo_pino_{nome}", Pos(x, 0, z_tambor0 + P.PIVO_TAMBOR_DENTRO / 2) * pivo_pino()))
        z0 = z_tambor0 + P.PIVO_TAMBOR_L                       # topo do tambor
        partes.append((f"porca_pivo_{nome}", Pos(x, 0, z0) * porca()))
        z1 = z0 + P.PORCA_ESP                                  # início da rosca exposta
        z2 = z1 + P.ROSCA_INF_EXPOSTA                          # base do punho
        partes.append((f"punho_{nome}", Pos(x, 0, z2) * punho()))
        z_punho_topo = z2 + P.PUNHO_L
        z_tubo0 = z_punho_topo - P.TUBO_DENTRO_PUNHO - desloc  # ponta de baixo do tubo
        partes.append((f"tubo_mola_{nome}", Pos(x, 0, z_tubo0) * tubo_mola()))
        z4 = z_tubo0 + P.TUBO_MOLA_VISIVEL + P.TUBO_DENTRO_PUNHO  # topo do tubo = base da ponte
        z_mola0 = z2 + P.PUNHO_PORCA_L                         # mola: do fundo do furo do punho até a ponte
        partes.append((f"mola_{nome}", Pos(x, 0, z_mola0) * mola(z4 - z_mola0)))
        z["ponte"] = z4 + P.PONTE_ESP / 2
        z["barra"] = z_punho_topo + P.TUBO_MOLA_VISIVEL + P.PONTE_ESP + P.ROSCA_SUP_EXPOSTA  # fixa: não depende da carga
        partes.append((f"porca_barra_{nome}", Pos(x, 0, z["barra"] - P.PORCA_ESP) * porca()))
        comp_rosca = (z["barra"] + P.ROSCA_NA_BARRA) - (z0 - P.ROSCA_NO_TAMBOR)
        partes.append((f"rosca_{nome}", Pos(x, 0, z0 - P.ROSCA_NO_TAMBOR) * rosca(comp_rosca)))
    partes.append(("ponte", Pos(0, 0, z["ponte"]) * ponte()))
    partes.append(("barra_superior", Pos(0, 0, z["barra"]) * barra_superior()))
    if com_copo:
        # pescoço do copo encaixado no entalhe da ponte (centrado na espessura dela)
        z_boca = z["ponte"] - P.COPO_PESCOCO_L / 2 - (P.COPO_CORPO_L + P.COPO_OMBRO_L)
        partes.append(("copo", Pos(0, 0, z_boca) * copo()))
    return partes
