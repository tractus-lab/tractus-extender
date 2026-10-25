"""Peças do extensor em build123d (modo álgebra). Cada função devolve um sólido."""
from build123d import *
import parametros as P


def base():
    """Anel de apoio com duas orelhas furadas para as hastes."""
    anel = Cylinder(P.BASE_D_EXT / 2, P.BASE_ESP) - Cylinder(P.BASE_D_INT / 2, P.BASE_ESP)
    for sx in (-1, 1):
        x = sx * P.BASE_DIST_FUROS / 2
        anel += Pos(x, 0, 0) * Cylinder(P.BASE_LUG_D / 2, P.BASE_ESP)
        anel -= Pos(x, 0, 0) * Cylinder(P.BASE_FURO_D / 2, P.BASE_ESP)
    return anel


def almofada():
    """Almofada que fica sob o anel (lado do corpo)."""
    return Cylinder(P.BASE_D_EXT / 2, P.BASE_ALMOFADA_ESP) - Cylinder(P.BASE_D_INT / 2, P.BASE_ALMOFADA_ESP)


def haste_externa():
    """Tubo externo com pino rosqueado na base. Origem na face inferior do pino."""
    pino = Pos(0, 0, P.HASTE_ROSCA_L / 2) * Cylinder(P.HASTE_ROSCA_D / 2, P.HASTE_ROSCA_L)
    tubo = Pos(0, 0, P.HASTE_ROSCA_L + P.HASTE_TUBO_L / 2) * (
        Cylinder(P.HASTE_TUBO_D_EXT / 2, P.HASTE_TUBO_L) - Cylinder(P.HASTE_TUBO_D_INT / 2, P.HASTE_TUBO_L)
    )
    return pino + tubo


def haste_interna():
    """Haste que desliza dentro do tubo externo (onde fica a mola, na realidade)."""
    return Pos(0, 0, P.HASTE_INTERNA_L / 2) * Cylinder(P.HASTE_INTERNA_D / 2, P.HASTE_INTERNA_L)


def jugo():
    """Barra superior que une as duas hastes e segura o copo."""
    comp = P.BASE_DIST_FUROS + P.JUGO_LARG
    barra = Box(comp, P.JUGO_LARG, P.JUGO_ESP)
    for sx in (-1, 1):
        barra -= Pos(sx * P.BASE_DIST_FUROS / 2, 0, 0) * Cylinder(P.HASTE_INTERNA_D / 2 + 0.1, P.JUGO_ESP)
    barra -= Cylinder(P.JUGO_FURO_COPO_D / 2, P.JUGO_ESP)
    return barra


def copo(d_int: float):
    """Copo de vácuo. Boca em z=0 (voltada para -z), fundo e pino para cima."""
    r_ext = d_int / 2 + P.COPO_PAREDE
    h_total = P.COPO_ALTURA + P.COPO_TOPO_ESP
    corpo = Pos(0, 0, h_total / 2) * Cylinder(r_ext, h_total)
    cavidade = Pos(0, 0, P.COPO_ALTURA / 2) * Cylinder(d_int / 2, P.COPO_ALTURA)
    copo = corpo - cavidade
    pino = Pos(0, 0, h_total + P.COPO_PINO_L / 2) * Cylinder(P.COPO_PINO_D / 2, P.COPO_PINO_L)
    copo += pino
    # bico lateral para a bomba, a meia altura
    z_bico = P.COPO_ALTURA * 0.6
    bico = Pos(r_ext + P.COPO_BICO_L / 2 - 1, 0, z_bico) * Rot(0, 90, 0) * Cylinder(P.COPO_BICO_D / 2, P.COPO_BICO_L + 2)
    furo_bico = Pos(r_ext / 2 + P.COPO_BICO_L / 2, 0, z_bico) * Rot(0, 90, 0) * Cylinder(P.COPO_BICO_FURO_D / 2, r_ext + P.COPO_BICO_L + 2)
    copo = copo + bico - furo_bico
    return copo


def membrana(d_int: float):
    """Membrana de silicone com furo central e aba que abraça a boca do copo."""
    r_ext_copo = d_int / 2 + P.COPO_PAREDE
    disco = Pos(0, 0, -P.MEMB_ESP / 2) * Cylinder(r_ext_copo + P.MEMB_ABA, P.MEMB_ESP)
    furo = Cylinder(d_int * P.MEMB_FURO_FRACAO / 2, 10)
    aba = Pos(0, 0, P.MEMB_ABA_ALT / 2) * (
        Cylinder(r_ext_copo + P.MEMB_ABA, P.MEMB_ABA_ALT) - Cylinder(r_ext_copo, P.MEMB_ABA_ALT)
    )
    return disco + aba - furo


def manga(d_int: float):
    """Manga de silicone (alternativa ao copo)."""
    return Pos(0, 0, P.MANGA_L / 2) * (
        Cylinder(d_int / 2 + P.MANGA_PAREDE, P.MANGA_L) - Cylinder(d_int / 2, P.MANGA_L)
    )


def montagem(copo_d: float = 36):
    """Conjunto montado: base, almofada, hastes, jugo, copo e membrana."""
    partes = []
    partes.append(("almofada", Pos(0, 0, -P.BASE_ALMOFADA_ESP / 2) * almofada()))
    partes.append(("base", Pos(0, 0, P.BASE_ESP / 2) * base()))
    z_topo_tubo = P.BASE_ESP + P.HASTE_ROSCA_L + P.HASTE_TUBO_L
    z_topo_interna = z_topo_tubo + P.HASTE_EXTENSAO
    for nome, sx in (("haste_esq", -1), ("haste_dir", 1)):
        x = sx * P.BASE_DIST_FUROS / 2
        partes.append((nome + "_externa", Pos(x, 0, P.BASE_ESP - P.HASTE_ROSCA_L) * haste_externa()))
        partes.append((nome + "_interna", Pos(x, 0, z_topo_interna - P.HASTE_INTERNA_L) * haste_interna()))
    z_jugo = z_topo_interna - P.JUGO_ESP / 2
    partes.append(("jugo", Pos(0, 0, z_jugo) * jugo()))
    # copo pendurado no jugo, boca para baixo
    z_boca = z_jugo - P.JUGO_ESP / 2 - (P.COPO_ALTURA + P.COPO_TOPO_ESP)
    partes.append((f"copo_{copo_d}", Pos(0, 0, z_boca) * copo(copo_d)))
    partes.append((f"membrana_{copo_d}", Pos(0, 0, z_boca) * membrana(copo_d)))
    return partes
