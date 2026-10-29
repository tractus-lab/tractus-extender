"""Peças do extensor em build123d (modo álgebra), versão 0.9.3 (ferradura: anel > 180°, curva para fora, pás paralelas, abaulada)."""
import math
from build123d import *
import parametros as P


def _cil_entre(p1, p2, d):
    """Cilindro de diâmetro d entre dois pontos (para a alça de arame)."""
    p1, p2 = Vector(*p1), Vector(*p2)
    v = p2 - p1
    return Plane(origin=p1 + v / 2, z_dir=v) * Cylinder(d / 2, v.length)


def _arred(forma, r, arestas=None):
    """Arredonda arestas (fillet). Se o kernel não conseguir com esse raio, tenta a metade; se ainda
    assim falhar, devolve a forma sem arredondar (avisa no console)."""
    for raio in (r, r / 2, r / 4):
        try:
            return fillet(arestas if arestas is not None else forma.edges(), raio)
        except Exception:
            continue
    print(f"  (aviso: arredondamento de {r} mm não aplicado)")
    return forma


def _porca(af, esp):
    return extrude(RegularPolygon(af / 2 / 0.8660254, 6), esp)


# ---------------- Base ----------------
def _arred_2d(face, r, ignorar_x0=True):
    """Arredonda os vértices de uma face 2D um a um (r, r/2, r/4), pulando os que o OCCT recusa e os do eixo x=0."""
    for v in list(face.vertices()):
        if ignorar_x0 and abs(v.X) < 1.0:
            continue
        for rr in (r, r / 2, r / 4):
            try:
                alvo = [w for w in face.vertices() if (Vector(w.X, w.Y, 0) - Vector(v.X, v.Y, 0)).length < 1e-3]
                if not alvo:
                    break
                face = fillet(alvo, rr)
                break
            except Exception:
                continue
    return face


def _p(c, r, ang):
    return (c[0] + r * math.cos(math.radians(ang)), c[1] + r * math.sin(math.radians(ang)))


def _arco(c, r, a1, a2):
    """Arco de circunferência (centro c, raio r) do ângulo a1 ao a2, em graus, no sentido indicado."""
    return ThreePointArc(_p(c, r, a1), _p(c, r, (a1 + a2) / 2), _p(c, r, a2))


def _contorno_base():
    """Ferradura em planta, como na foto 07: o anel (faixa de 20,2 mm) segue além de 180° por BASE_ARCO_EXTRA em
    cada lado; aí cada braço faz uma curva para fora (linha média com raio BASE_R_DOBRA, tangente ao anel) até ficar
    vertical, e desce como pá reta, paralela ao eixo, até BASE_PONTA_Y com cantos arredondados. Tudo tangente:
    nenhum vértice vivo, para o abaulado 3D passar sem reclamar."""
    w = P.BASE_R_EXT - P.BASE_R_INT
    rm = (P.BASE_R_EXT + P.BASE_R_INT) / 2
    ro, ri = P.BASE_R_DOBRA - w / 2, P.BASE_R_DOBRA + w / 2
    beta = P.BASE_ARCO_EXTRA
    c = _p((0, 0), rm + P.BASE_R_DOBRA, -beta)       # centro da curva para fora, lado direito (colinear com a origem)
    cl = (-c[0], c[1])
    xo, xi = P.BASE_PA_X + w / 2, P.BASE_PA_X - w / 2
    yq = c[1]                                        # altura em que a pá fica vertical
    yc = P.BASE_PONTA_Y + P.BASE_R_PONTA
    rp = P.BASE_R_PONTA
    arestas = [
        _arco((0, 0), P.BASE_R_EXT, 90, -beta),                       # anel externo, lado direito (horário)
        _arco(c, ro, 180 - beta, 180),                                # curva para fora, borda externa
        Line((xo, yq), (xo, yc)),
        _arco((xo - rp, yc), rp, 0, -90),
        Line((xo - rp, P.BASE_PONTA_Y), (xi + rp, P.BASE_PONTA_Y)),
        _arco((xi + rp, yc), rp, -90, -180),
        Line((xi, yc), (xi, yq)),
        _arco(c, ri, 180, 180 - beta),                                # curva para fora, borda interna
        _arco((0, 0), P.BASE_R_INT, -beta, 180 + beta),               # anel interno, passando pelo topo
        _arco(cl, ri, beta, 0),
        Line((-xi, yq), (-xi, yc)),
        _arco((-xi - rp, yc), rp, 0, -90),
        Line((-xi - rp, P.BASE_PONTA_Y), (-xo + rp, P.BASE_PONTA_Y)),
        _arco((-xo + rp, yc), rp, -90, -180),
        Line((-xo, yc), (-xo, yq)),
        _arco(cl, ro, 0, beta),
        _arco((0, 0), P.BASE_R_EXT, 180 + beta, 90),
    ]
    return make_face(arestas)


def _placa_base():
    """Ferradura inteira (sem os garfos do pivô), centrada em Z, com as bordas de cima e de baixo abauladas."""
    b = extrude(_contorno_base(), P.BASE_ESP / 2, both=True)
    grupos = b.edges().group_by(Axis.Z)
    return _arred(b, P.BASE_ABAULADO_R, grupos[0] + grupos[-1])


def _caixa_pivo(x):
    """Garfo de articulação em cima da ferradura: bloco com topo arredondado (raio = metade do comprimento no sentido
    da rotação), duas bochechas de PIVO_BOCHECHA_ESP separadas pelo vão onde entra a lingueta do tambor, e furo do pino."""
    z_topo = P.BASE_ESP / 2
    z_pino = z_topo + P.PIVO_PINO_ALT
    alt = P.PIVO_PINO_ALT + P.BASE_ABAULADO_R                      # começa dentro da placa, abaixo do abaulado
    caixa = Pos(x, 0, z_pino - alt / 2) * Box(P.PIVO_CAIXA_X, P.PIVO_CAIXA_Y, alt)
    caixa += Pos(x, 0, z_pino) * Rot(0, 90, 0) * Cylinder(P.PIVO_CAIXA_Y / 2, P.PIVO_CAIXA_X)
    caixa = _arred(caixa, P.RAIO_ARESTA_PEQ)
    # vão entre as bochechas: atravessa todo o Y (a lingueta gira nele) e desce até pouco abaixo da ponta da lingueta
    z_piso = z_pino - P.PIVO_TAMBOR_ABAIXO_PINO - 0.5
    alt_vao = P.PIVO_CAIXA_Y + P.PIVO_PINO_ALT + 2
    caixa -= Pos(x, 0, z_piso + alt_vao / 2) * Box(P.PIVO_GARFO_VAO, P.PIVO_CAIXA_Y + 2, alt_vao)
    caixa -= Pos(x, 0, z_pino) * Rot(0, 90, 0) * Cylinder(P.PIVO_PINO_D / 2, P.PIVO_CAIXA_X + 2)
    return caixa


def base_plastico():
    """Metade de cima da ferradura (plástico) com as caixas do pivô. z de -BASE_ESP/2+BASE_BORRACHA_ESP até o topo das caixas."""
    plano = Plane.XY.offset(-P.BASE_ESP / 2 + P.BASE_BORRACHA_ESP)
    b = split(_placa_base(), bisect_by=plano, keep=Keep.TOP)
    for sx in (-1, 1):
        b += _caixa_pivo(sx * P.HASTE_X)
    return b


def base_borracha():
    """Metade de baixo da ferradura, em borracha firme: é a face que encosta na virilha."""
    plano = Plane.XY.offset(-P.BASE_ESP / 2 + P.BASE_BORRACHA_ESP)
    return split(_placa_base(), bisect_by=plano, keep=Keep.BOTTOM)


def base():
    """Ferradura completa (plástico + borracha), para exportação individual."""
    return base_plastico() + base_borracha()


def pivo_tambor():
    """Tambor de inox que recebe a rosca da haste. A ponta de baixo é rebaixada por dois planos numa lingueta de
    PIVO_LINGUETA_ESP (sentido X, do pino) com a ponta arredondada em torno do eixo do pino; furo transversal para o pino.
    Origem na ponta de baixo da lingueta, eixo Z."""
    t = Pos(0, 0, P.PIVO_TAMBOR_L / 2) * Cylinder(P.PIVO_TAMBOR_D / 2, P.PIVO_TAMBOR_L)
    t -= Pos(0, 0, P.PIVO_TAMBOR_L / 2) * Cylinder(P.ROSCA_D / 2, P.PIVO_TAMBOR_L)
    d = P.PIVO_TAMBOR_D + 2
    for sx in (-1, 1):  # os dois planos da lingueta
        t -= Pos(sx * (P.PIVO_LINGUETA_ESP / 2 + d / 2), 0, P.PIVO_LINGUETA_L / 2 - 1) * Box(d, d, P.PIVO_LINGUETA_L + 2)
    # ponta arredondada: abaixo do pino só fica o que está dentro do raio PIVO_TAMBOR_ABAIXO_PINO em torno do eixo do pino
    z_pino = P.PIVO_TAMBOR_ABAIXO_PINO
    canto = Pos(0, 0, z_pino / 2 - 1) * Box(d, d, z_pino + 2) - Pos(0, 0, z_pino) * Rot(0, 90, 0) * Cylinder(z_pino, d)
    t -= canto
    t -= Pos(0, 0, z_pino) * Rot(0, 90, 0) * Cylinder(P.PIVO_PINO_D / 2, d)
    return t


def pivo_pino():
    """Pino transversal (eixo X), centrado na origem."""
    return Rot(0, 90, 0) * Cylinder(P.PIVO_PINO_D / 2, P.PIVO_CAIXA_X)


def pivo_tampa(lado=1):
    """Tampa redonda de plástico numa face do garfo (lado=+1 ou -1 em X), escondendo o pino. Há uma em cada face. Centrada no eixo do pino."""
    t = _arred(Cylinder(P.PIVO_TAMPA_D / 2, P.PIVO_TAMPA_ESP), P.PIVO_TAMPA_ESP * 0.45)
    return Pos(lado * (P.PIVO_CAIXA_X / 2 + P.PIVO_TAMPA_ESP / 2), 0, 0) * Rot(0, 90, 0) * t


# ---------------- Haste ----------------
def porca():
    return _porca(P.PORCA_AF, P.PORCA_ESP)


def rosca(comp):
    """Haste roscada (fuso), uma peça por lado. Nome comercial: barra roscada M6 inox 304. Origem na base, eixo Z.
    Com ROSCA_COM_FIO, o fio helicoidal ISO (perfil 60°, passo ROSCA_PASSO) é gerado pelo bd_warehouse e fica como
    segunda forma do mesmo conjunto, sem fundir ao núcleo: a fusão booleana leva ~36 s por haste e não muda nada visualmente."""
    if not P.ROSCA_COM_FIO:
        return Pos(0, 0, comp / 2) * Cylinder(P.ROSCA_D / 2, comp)
    from bd_warehouse.thread import IsoThread
    fio = IsoThread(major_diameter=P.ROSCA_D, pitch=P.ROSCA_PASSO, length=comp, external=True, end_finishes=("fade", "fade"))
    nucleo = Pos(0, 0, comp / 2) * Cylinder(fio.min_radius, comp)
    return Compound(children=[nucleo, fio])


def punho():
    """Punho serrilhado = castanha. Rosca interna curta embaixo (modelada como furo de 6 mm) e
    furo liso de PUNHO_FURO_D em cima, onde a mola fica e o tubo da escala desliza. Origem na base."""
    p = Pos(0, 0, P.PUNHO_L / 2) * Cylinder(P.PUNHO_D / 2, P.PUNHO_L)
    p = _arred(p, P.RAIO_ARESTA)
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
    """Chapa única entre as hastes (4,5 mm) com um cubo em volta de cada haste (furo liso: desliza).
    No meio: furo/rasgo em U de 12 mm para o pescoço do copo, aberto para um lado, e na face de cima um
    rebaixo circular fechado de 20 mm x 1,5 mm onde o corpo da válvula assenta sob tração (fechadura).
    Origem: eixo entre as hastes, z = 0 na base dos cubos; a face de cima da chapa fica em z = PONTE_CUBO_ESP."""
    topo = P.PONTE_CUBO_ESP
    chapa = Pos(0, 0, topo - P.PONTE_ESP / 2) * Box(P.PONTE_COMP, P.PONTE_LARG, P.PONTE_ESP)
    g = _arred(chapa, min(P.RAIO_ARESTA, P.PONTE_ESP / 2 - 0.3))
    for sx in (-1, 1):
        cubo = _arred(Pos(sx * P.HASTE_X, 0, topo / 2) * Cylinder(P.PONTE_CUBO_D / 2, topo), P.RAIO_ARESTA_PEQ)
        g += cubo
        g -= Pos(sx * P.HASTE_X, 0, topo / 2) * Cylinder(P.PONTE_FURO_HASTE_D / 2, topo + 2)
    g -= Pos(0, 0, topo / 2) * Cylinder(P.PONTE_ENTALHE_D / 2, topo + 2)
    g -= Pos(0, P.PONTE_ENTALHE_LADO * P.PONTE_LARG / 2, topo / 2) * Box(P.PONTE_ENTALHE_D, P.PONTE_LARG, topo + 2)
    g -= Pos(0, 0, topo) * Cylinder(P.PONTE_REBAIXO_D / 2, 2 * P.PONTE_REBAIXO_PROF)
    return g


def barra_superior():
    """Barra 'EPIC': dois cilindros com olhais, unidos por uma tira. Origem na base dos cilindros."""
    L = P.BARRA_BOSS_L
    b = None
    for sx in (-1, 1):
        boss = _arred(Pos(sx * P.HASTE_X, 0, L / 2) * Cylinder(P.BARRA_BOSS_D / 2, L), P.RAIO_ARESTA)
        boss -= Pos(sx * P.HASTE_X, 0, L / 2) * Cylinder(P.ROSCA_D / 2, L)
        x_olhal = sx * (P.HASTE_X + P.BARRA_BOSS_D / 2 + P.BARRA_OLHAL_D / 2 - 2)
        olhal = Pos(x_olhal, 0, L - P.BARRA_OLHAL_D / 2) * Rot(90, 0, 0) * Cylinder(P.BARRA_OLHAL_D / 2, P.BARRA_OLHAL_ESP)
        olhal -= Pos(x_olhal, 0, L - P.BARRA_OLHAL_D / 2) * Rot(90, 0, 0) * Cylinder(P.BARRA_OLHAL_FURO_D / 2, P.BARRA_OLHAL_ESP + 1)
        b = boss + olhal if b is None else b + boss + olhal
    # tira em '[' (planta): perna saindo de cada cilindro para o lado, travessa cruzando no desvio
    e, dy = P.BARRA_TIRA_ESP, P.BARRA_TIRA_DESLOC_Y
    planta = Pos(0, dy) * Rectangle(2 * P.HASTE_X + e, e)
    for sx in (-1, 1):
        planta += Pos(sx * P.HASTE_X, dy / 2) * Rectangle(e, abs(dy) + e)
    planta = _arred_2d(planta.face(), P.BARRA_DOBRA_R, ignorar_x0=False)
    tira = _arred(extrude(planta, P.BARRA_TIRA_ALT / 2, both=True).moved(Pos(0, 0, L / 2)), P.RAIO_ARESTA_PEQ)
    return b + tira


# ---------------- Copo ----------------
def _perfil_sino(r, rp, Lc, Ld, z0=0.0, folga_topo=0.0):
    """Meio perfil (plano XZ) de um sino: base plana em z0, parede cilíndrica até Lc, domo suave
    (spline, formato de glande) até o raio do pescoço rp em Lc+Ld. Fechado no eixo."""
    topo = Lc + Ld + folga_topo
    pts = [Line((0, z0), (r, z0)), Line((r, z0), (r, Lc)),
           Spline((r, Lc), (r * 0.80, Lc + Ld * 0.62), (rp, Lc + Ld), tangents=((0, 1), (-1, 0.25)))]
    if folga_topo > 0:
        pts.append(Line((rp, Lc + Ld), (rp, topo)))
    pts += [Line((rp, topo), (0, topo)), Line((0, topo), (0, z0))]
    return make_face([Plane.XZ * e for e in pts])


def copo(d_ext=None):
    """Copo em forma de glande: cilindro com anéis na boca, domo abaulado, pescoço e válvula.
    Seção levemente oval (COPO_OVAL). Boca em z=0 voltada para -Z; o copo se estende para +Z."""
    d_ext = d_ext or P.COPO_FOTO_D_EXT
    r = d_ext / 2
    ri = r - P.COPO_PAREDE
    rp = P.COPO_PESCOCO_D / 2
    Lc, Ld, Lp = P.COPO_CORPO_L, P.COPO_DOMO_L, P.COPO_PESCOCO_L
    sino = revolve(_perfil_sino(r, rp, Lc, Ld), Axis.Z)
    cav = revolve(_perfil_sino(ri, rp - 1.5, Lc - 1, Ld, z0=-1, folga_topo=Lp + 2), Axis.Z)
    c = sino - cav
    c = _arred(c, P.RAIO_ARESTA_PEQ, c.edges().filter_by(Plane.XY).filter_by_position(Axis.Z, -0.5, 0.5))  # boca
    for i in range(P.COPO_ANEIS_N):
        z = 3 + i * P.COPO_ANEIS_PASSO
        c += Pos(0, 0, z) * (Cylinder(r + P.COPO_ANEIS_ALT, P.COPO_ANEIS_LARG) - Cylinder(r - 0.1, P.COPO_ANEIS_LARG))
    if P.COPO_OVAL != 1.0:
        c = scale(c, by=(1.0, P.COPO_OVAL, 1.0))  # seção oval; o pescoço e a válvula ficam redondos
    # pescoço redondo (encaixa no rebaixo circular da ponte), furado
    c += Pos(0, 0, Lc + Ld + Lp / 2) * (Cylinder(rp, Lp) - Cylinder(rp - 1.5, Lp + 1))
    Lo = Ld
    z_valv = Lc + Lo + Lp
    c += Pos(0, 0, z_valv + P.VALVULA_L / 2) * Cylinder(P.VALVULA_D / 2, P.VALVULA_L)
    # A alça triangular de arame do copo original foi deixada de fora: serve a outro sistema de tração
    # (cinta/elástico), não à ponte. Decisão do usuário em 2026-10-27.
    return c


def membrana(d_ext=None):
    """Membrana de silicone sobre a boca (geometria ainda não observada)."""
    d_ext = d_ext or P.COPO_FOTO_D_EXT
    r = d_ext / 2 + P.COPO_ANEIS_ALT + 1
    m = Pos(0, 0, -P.MEMB_ESP / 2) * Cylinder(r, P.MEMB_ESP)
    m -= Cylinder((d_ext - 2 * P.COPO_PAREDE) * P.MEMB_FURO_FRACAO / 2, 10)
    return m


def manga(d_int):
    """Manga de silicone em repouso: tubo reto. Origem na ponta de baixo, eixo Z."""
    return Pos(0, 0, P.MANGA_L / 2) * (Cylinder(d_int / 2 + P.MANGA_PAREDE, P.MANGA_L) - Cylinder(d_int / 2, P.MANGA_L))


def manga_montada(d_int_repouso, d_ext_copo):
    """Manga vestida no copo (foto 09): o trecho de cima está esticado sobre os anéis do copo,
    há uma transição curta e o resto fica no diâmetro de repouso. Parede afina onde estica.
    Origem na ponta de baixo, eixo Z; a boca do copo fica em z = MANGA_L - MANGA_SOBRE_COPO."""
    L, S, T = P.MANGA_L, P.MANGA_SOBRE_COPO, P.MANGA_TRANSICAO
    ri, re = d_int_repouso / 2, d_int_repouso / 2 + P.MANGA_PAREDE
    ri2 = d_ext_copo / 2 + P.COPO_ANEIS_ALT + 0.1
    re2 = ri2 + P.MANGA_PAREDE * (ri / ri2)  # volume de parede conservado, aproximado
    ext = [(0, 0), (re, 0), (re, L - S - T), (re2, L - S), (re2, L), (0, L)]
    inte = [(0, -1), (ri, -1), (ri, L - S - T), (ri2, L - S), (ri2, L + 1), (0, L + 1)]
    return revolve(Plane.XZ * Polygon(*ext, align=None), Axis.Z) - revolve(Plane.XZ * Polygon(*inte, align=None), Axis.Z)


# ---------------- Montagem ----------------
def montagem(com_copo=True, carga_lb=None):
    """Conjunto em posição de uso: hastes perpendiculares à base. carga_lb desloca o tubo
    para dentro do punho (0 = repouso, ESCALA_LB_MAX = curso todo)."""
    carga = P.CARGA_LB if carga_lb is None else carga_lb
    desloc = P.CURSO_ESCALA * carga / P.ESCALA_LB_MAX
    partes = [("base_plastico", base_plastico()), ("base_borracha", base_borracha())]
    z_base_topo = P.BASE_ESP / 2
    z_pino = z_base_topo + P.PIVO_PINO_ALT
    z_tambor0 = z_pino - P.PIVO_TAMBOR_ABAIXO_PINO
    z = {}
    for nome, sx in (("esq", -1), ("dir", 1)):
        x = sx * P.HASTE_X
        partes.append((f"pivo_tambor_{nome}", Pos(x, 0, z_tambor0) * pivo_tambor()))
        partes.append((f"pivo_pino_{nome}", Pos(x, 0, z_pino) * pivo_pino()))
        partes.append((f"pivo_tampa_ext_{nome}", Pos(x, 0, z_pino) * pivo_tampa(sx)))   # tampa na face externa do garfo
        partes.append((f"pivo_tampa_int_{nome}", Pos(x, 0, z_pino) * pivo_tampa(-sx)))  # e outra na face interna (usuário, 2026-10-28)
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
        z["ponte"] = z4                                        # base dos cubos da ponte = topo dos tubos
        z["barra"] = z_punho_topo + P.TUBO_MOLA_VISIVEL + P.PONTE_CUBO_ESP + P.ROSCA_SUP_EXPOSTA  # fixa: não depende da carga
        partes.append((f"porca_barra_{nome}", Pos(x, 0, z["barra"] - P.PORCA_ESP) * porca()))
        comp_rosca = (z["barra"] + P.ROSCA_NA_BARRA) - (z0 - P.ROSCA_NO_TAMBOR)
        partes.append((f"rosca_{nome}", Pos(x, 0, z0 - P.ROSCA_NO_TAMBOR) * rosca(comp_rosca)))
    partes.append(("ponte", Pos(0, 0, z["ponte"]) * ponte()))
    partes.append(("barra_superior", Pos(0, 0, z["barra"]) * barra_superior()))
    if com_copo:
        # copo em posição de uso (tracionado): corpo da válvula assentado no piso do rebaixo da ponte
        z_valv = z["ponte"] + P.PONTE_CUBO_ESP - P.PONTE_REBAIXO_PROF + P.COPO_FOLGA_ASSENTO
        z_boca = z_valv - (P.COPO_CORPO_L + P.COPO_OMBRO_L + P.COPO_PESCOCO_L)
        partes.append(("copo", Pos(0, 0, z_boca) * copo()))
        # manga de silicone esticada sobre a boca do copo (anéis dão o atrito), descendo para a pele
        partes.append(("manga", Pos(0, 0, z_boca - (P.MANGA_L - P.MANGA_SOBRE_COPO)) * manga_montada(P.MANGA_FOTO_D, P.COPO_FOTO_D_EXT)))
    return partes
