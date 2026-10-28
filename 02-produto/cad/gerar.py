"""
Gera todos os arquivos de saída:
  saida/step/   -> STEP de cada peça e da montagem (para FreeCAD e fabricantes)
  saida/stl/    -> STL de cada peça (para impressão 3D)
  preview/      -> SVG e PNG da montagem (para ver sem abrir CAD)

Uso:  .venv/bin/python gerar.py
"""
import os
from build123d import *
import parametros as P
import pecas

AQUI = os.path.dirname(os.path.abspath(__file__))
STEP = os.path.join(AQUI, "saida", "step")
STL = os.path.join(AQUI, "saida", "stl")
PREV = os.path.join(AQUI, "preview")
for d in (STEP, STL, PREV):
    os.makedirs(d, exist_ok=True)


def salvar(nome, solido):
    export_step(solido, os.path.join(STEP, f"{nome}.step"))
    export_stl(solido, os.path.join(STL, f"{nome}.stl"))
    bb = solido.bounding_box()
    print(f"  {nome:18s} {bb.size.X:6.1f} x {bb.size.Y:6.1f} x {bb.size.Z:6.1f} mm  vol {solido.volume/1000:7.2f} cm³")


print("Peças individuais:")
salvar("base", pecas.base())
salvar("pivo_tambor", pecas.pivo_tambor())
salvar("porca", pecas.porca())
salvar("punho", pecas.punho())
salvar("tubo_mola", pecas.tubo_mola())
salvar("mola_repouso", pecas.mola(105.0))
salvar("ponte", pecas.ponte())
salvar("barra_superior", pecas.barra_superior())
salvar("copo_foto", pecas.copo())
salvar("membrana_foto", pecas.membrana())
salvar("manga_montada_no_copo", pecas.manga_montada(P.MANGA_FOTO_D, P.COPO_FOTO_D_EXT))
for d in P.MANGA_TAMANHOS:
    salvar(f"manga_{d}", pecas.manga(d))

print("Montagem:")
partes = pecas.montagem()
conjunto = Compound(children=[s for _, s in partes])
export_step(conjunto, os.path.join(STEP, "montagem.step"))
bb = conjunto.bounding_box()
print(f"  montagem  {bb.size.X:.1f} x {bb.size.Y:.1f} x {bb.size.Z:.1f} mm")


def _add_arestas(svg, arestas, camada):
    """Adiciona aresta por aresta, pulando as degeneradas (arcos de elipse com início = fim fazem o exportador
    do build123d 0.13 falhar numa asserção do svgpathtools)."""
    puladas = 0
    for a in arestas:
        try:
            if a.length < 1e-3:
                puladas += 1
                continue
            svg.add_shape(a, layer=camada)
        except Exception:
            puladas += 1
    if puladas:
        print(f"  ({camada}: {puladas} arestas degeneradas puladas)")


def previa(nome, shape, direcao, escala=2.0):
    svg = ExportSVG(scale=escala, line_weight=0.4)
    svg.add_layer("visivel", line_color="black")
    svg.add_layer("oculto", line_type=LineType.ISO_DASH, line_color="gray", line_weight=0.2)
    cima = (0, 1, 0) if abs(direcao[2]) > 0.99 else (0, 0, 1)  # vista de topo: "cima" não pode ser paralelo à direção
    vis, hid = shape.project_to_viewport(viewport_origin=tuple(c * 800 for c in direcao), viewport_up=cima)
    _add_arestas(svg, vis, "visivel")
    _add_arestas(svg, hid, "oculto")
    caminho = os.path.join(PREV, f"{nome}.svg")
    svg.write(caminho)
    try:
        import cairosvg
        cairosvg.svg2png(url=caminho, write_to=caminho.replace(".svg", ".png"), background_color="white", output_width=1400)
    except Exception as e:
        print("  (PNG não gerado:", e, ")")


for nome, direcao in {"frente": (0, -1, 0), "lado": (1, 0, 0), "iso": (1, -1, 0.7), "topo": (0.001, 0, 1)}.items():
    previa(f"montagem_{nome}", conjunto, direcao)
conj_carga = Compound(children=[s for _, s in pecas.montagem(carga_lb=pecas.P.ESCALA_LB_MAX)])
previa("montagem_frente_22lb", conj_carga, (0, -1, 0))
previa("base_topo", pecas.base(), (0.001, 0, 1), escala=4)  # 0.001: vista exatamente axial sai vazia no build123d 0.13
previa("copo_lado", pecas.copo(), (0, -1, 0), escala=4)
previa("ponte_com_copo", Compound(children=[pecas.ponte(), Pos(0, 0, P.PONTE_CUBO_ESP - P.PONTE_REBAIXO_PROF - (P.COPO_CORPO_L + P.COPO_OMBRO_L + P.COPO_PESCOCO_L)) * pecas.copo()]), (1, -0.6, 0.5), escala=4)
previa("copo_com_manga", Compound(children=[pecas.copo(), Pos(0, 0, -(pecas.P.MANGA_L - pecas.P.MANGA_SOBRE_COPO)) * pecas.manga_montada(pecas.P.MANGA_FOTO_D, pecas.P.COPO_FOTO_D_EXT)]), (0, -1, 0), escala=4)
print("Prévias em", PREV)
