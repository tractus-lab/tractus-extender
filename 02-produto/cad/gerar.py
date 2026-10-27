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
salvar("porta_copo_dir", pecas.porta_copo(1))
salvar("barra_superior", pecas.barra_superior())
salvar("copo_foto", pecas.copo())
salvar("membrana_foto", pecas.membrana())
for d in P.MANGA_TAMANHOS:
    salvar(f"manga_{d}", pecas.manga(d))

print("Montagem:")
partes = pecas.montagem()
conjunto = Compound(children=[s for _, s in partes])
export_step(conjunto, os.path.join(STEP, "montagem.step"))
bb = conjunto.bounding_box()
print(f"  montagem  {bb.size.X:.1f} x {bb.size.Y:.1f} x {bb.size.Z:.1f} mm")


def previa(nome, shape, direcao, escala=2.0):
    svg = ExportSVG(scale=escala, line_weight=0.4)
    svg.add_layer("visivel", line_color="black")
    svg.add_layer("oculto", line_type=LineType.ISO_DASH, line_color="gray", line_weight=0.2)
    cima = (0, 1, 0) if abs(direcao[2]) > 0.99 else (0, 0, 1)  # vista de topo: "cima" não pode ser paralelo à direção
    vis, hid = shape.project_to_viewport(viewport_origin=tuple(c * 800 for c in direcao), viewport_up=cima)
    svg.add_shape(vis, layer="visivel")
    svg.add_shape(hid, layer="oculto")
    caminho = os.path.join(PREV, f"{nome}.svg")
    svg.write(caminho)
    try:
        import cairosvg
        cairosvg.svg2png(url=caminho, write_to=caminho.replace(".svg", ".png"), background_color="white", output_width=1400)
    except Exception as e:
        print("  (PNG não gerado:", e, ")")


for nome, direcao in {"frente": (0, -1, 0), "lado": (1, 0, 0), "iso": (1, -1, 0.7), "topo": (0.001, 0, 1)}.items():
    previa(f"montagem_{nome}", conjunto, direcao)
previa("base_topo", pecas.base(), (0.001, 0, 1), escala=4)  # 0.001: vista exatamente axial sai vazia no build123d 0.13
previa("copo_lado", pecas.copo(), (0, -1, 0), escala=4)
print("Prévias em", PREV)
