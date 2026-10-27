"""Peças do extensor em build123d (modo álgebra), versão 0.3 (foto 08: porta-copos com braço curvo; copo pendurado entre as hastes)."""
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
    """Trecho de haste roscada (modelada lisa). Origem na base, eixo Z."""
    return Pos(0, 0, comp / 2) * Cylinder(P.ROSCA_D / 2, comp)


def punho():
    """Punho serrilhado (porca longa). Origem na base, eixo Z."""
    p = Pos(0, 0, P.PUNHO_L / 2) * Cylinder(P.PUNHO_D / 2, P.PUNHO_L)
    p -= Pos(0, 0, P.PUNHO_L / 2) * Cylinder(P.ROSCA_D / 2, P.PUNHO_L)
    return p


def tubo_mola():
    """Tubo da escala, que abriga a mola e desliza sobre o punho. Origem na base, eixo Z."""
    t = Pos(0, 0, P.TUBO_MOLA_L / 2) * Cylinder(P.TUBO_MOLA_D / 2, P.TUBO_MOLA_L)
    t -= Pos(0, 0, P.TUBO_MOLA_L / 2) * Cylinder(P.TUBO_MOLA_D / 2 - 1.0, P.TUBO_MOLA_L)
    return t


def porta_copo(lado=1):
    """Bloco preto que fica sobre o tubo da escala, com furo para a rosca e um braço curvo
    voltado para o eixo do copo. A alça de arame do copo engancha na ponta do braço.
    Origem no eixo da haste, centro do bloco em z=0. lado=+1 (haste direita) ou -1."""
    b = Box(P.PORTA_LARG_X, P.PORTA_LARG_Y, P.PORTA_ESP)
    b -= Cylinder(P.ROSCA_D / 2 + 0.2, P.PORTA_ESP + 1)
    # braço no plano XZ (coordenadas locais da haste direita), depois espelhado se lado=-1
    xi = -P.PORTA_LARG_X / 2                      # face interna do bloco
    xp = -(P.HASTE_X - P.PORTA_BRACO_X_PONTA)     # ponta do braço, no eixo da haste
    zp = P.PORTA_BRACO_Z_PONTA
    pts = [(xi, 3.0), (xi, -P.PORTA_ESP / 2),
           (xp + 4, zp - 3), (xp - 2, zp - 1), (xp - 1, zp + 4), (xp + 6, zp + 2)]
    braco = extrude(Plane.XZ * Polygon(*pts, align=None), P.PORTA_BRACO_ESP / 2, both=True)
    b += braco
    if lado < 0:
        b = mirror(b, Plane.YZ)
    return b


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
def montagem(com_copo=True):
    """Conjunto em posição de uso: hastes perpendiculares à base, sem carga na mola."""
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
        z1 = z0 + P.PORCA_ESP
        partes.append((f"rosca_inf_{nome}", Pos(x, 0, z1) * rosca(P.ROSCA_INF_EXPOSTA)))
        z2 = z1 + P.ROSCA_INF_EXPOSTA
        partes.append((f"punho_{nome}", Pos(x, 0, z2) * punho()))
        z3 = z2 + P.PUNHO_L - P.TUBO_SOBRE_PUNHO
        partes.append((f"tubo_mola_{nome}", Pos(x, 0, z3) * tubo_mola()))
        z4 = z3 + P.TUBO_MOLA_L
        partes.append((f"rosca_sup_{nome}", Pos(x, 0, z4 + P.PORTA_ESP) * rosca(P.ROSCA_SUP_EXPOSTA)))
        z5 = z4 + P.PORTA_ESP + P.ROSCA_SUP_EXPOSTA
        partes.append((f"porca_barra_{nome}", Pos(x, 0, z5 - P.PORCA_ESP) * porca()))
        z["porta"] = z4 + P.PORTA_ESP / 2
        partes.append((f"porta_copo_{nome}", Pos(x, 0, z["porta"]) * porta_copo(sx)))
        z["barra"] = z4 + P.PORTA_ESP + P.ROSCA_SUP_EXPOSTA
    partes.append(("barra_superior", Pos(0, 0, z["barra"]) * barra_superior()))
    if com_copo:
        # pés da alça enganchados nas pontas dos braços dos porta-copos
        z_pe = z["porta"] + P.PORTA_BRACO_Z_PONTA
        z_valv = z_pe - P.VALVULA_L * 0.35
        z_boca = z_valv - (P.COPO_CORPO_L + P.COPO_OMBRO_L + P.COPO_PESCOCO_L)
        partes.append(("copo", Pos(0, 0, z_boca) * copo()))
    return partes
