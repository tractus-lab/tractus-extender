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
    print(f"  {nome:22s} {bb.size.X:6.1f} x {bb.size.Y:6.1f} x {bb.size.Z:6.1f} mm  vol {solido.volume/1000:7.2f} cm³")


print("Peças individuais:")
salvar("base", pecas.base())
salvar("almofada", pecas.almofada())
salvar("haste_externa", pecas.haste_externa())
salvar("haste_interna", pecas.haste_interna())
salvar("jugo", pecas.jugo())
for d in P.COPO_TAMANHOS:
    salvar(f"copo_{d}", pecas.copo(d))
    salvar(f"membrana_{d}", pecas.membrana(d))
for d in P.MANGA_TAMANHOS:
    salvar(f"manga_{d}", pecas.manga(d))

print("Montagem:")
partes = pecas.montagem(copo_d=36)
conjunto = Compound(children=[s for _, s in partes])
export_step(conjunto, os.path.join(STEP, "montagem.step"))
bb = conjunto.bounding_box()
print(f"  montagem  {bb.size.X:.1f} x {bb.size.Y:.1f} x {bb.size.Z:.1f} mm")

# Prévias em SVG (projeções ortográficas e isométrica)
vistas = {
    "frente": (0, -1, 0),
    "lado": (1, 0, 0),
    "iso": (1, -1, 0.8),
}
for nome, direcao in vistas.items():
    svg = ExportSVG(scale=2.5, line_weight=0.4)
    svg.add_layer("visivel", line_color=(20, 20, 20))
    svg.add_layer("oculto", line_type=LineType.ISO_DASH, line_color=(150, 150, 150), line_weight=0.2)
    vis, hid = conjunto.project_to_viewport(viewport_origin=tuple(c * 500 for c in direcao), viewport_up=(0, 0, 1))
    svg.add_shape(vis, layer="visivel")
    svg.add_shape(hid, layer="oculto")
    caminho = os.path.join(PREV, f"montagem_{nome}.svg")
    svg.write(caminho)
    try:
        import cairosvg
        cairosvg.svg2png(url=caminho, write_to=caminho.replace(".svg", ".png"), background_color="white", output_width=1400)
    except Exception as e:
        print("  (PNG não gerado:", e, ")")
print("Prévias em", PREV)
