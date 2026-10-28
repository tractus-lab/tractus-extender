"""Exporta a montagem agrupada por material para o visualizador web: STL (para outros programas)
e JSON com os triângulos (o que a página publicada lê, porque STL não é servido).
Uso: .venv/bin/python gerar_visualizador.py  (depois de gerar.py)"""
import os, json
from build123d import *
import pecas

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, "saida", "visualizador")
os.makedirs(OUT, exist_ok=True)

GRUPOS = {
    "plastico": ("Plástico preto (base, punhos, ponte, tampas do pivô)", ["base", "punho_", "ponte", "pivo_tampa_"]),
    "inox": ("Inox (tambores, pinos, hastes, porcas, molas)", ["pivo_", "rosca_", "porca_", "mola_"]),
    "aluminio": ("Alumínio anodizado (tubos da escala, barra)", ["tubo_mola", "barra_superior"]),
    "copo": ("Copo de vácuo (transparente) com válvula e alça", ["copo"]),
}
partes = pecas.montagem()
manifest = []
for chave, (rotulo, prefixos) in GRUPOS.items():
    sols = [s for n, s in partes if any(n.startswith(p) for p in prefixos)]
    comp = Compound(children=sols)
    # triângulos em JSON: lista plana x,y,z por vértice, 9 valores por triângulo, 2 casas decimais
    tri = []
    for nome_sol, sol in [(n, s) for n, s in partes if any(n.startswith(p) for p in prefixos)]:
        tol = (0.3, 0.6) if nome_sol.startswith("mola_") else (0.05, 0.2)  # mola helicoidal: malha grossa
        verts, faces = sol.tessellate(*tol)
        for a, b, c in faces:
            for v in (verts[a], verts[b], verts[c]):
                tri.extend((round(v.X, 2), round(v.Y, 2), round(v.Z, 2)))
    # STL depois do JSON: a malha fica guardada na peça, e a exportação fina só refaz o que estiver mais grosso
    export_stl(comp, os.path.join(OUT, f"{chave}.stl"), tolerance=0.05, angular_tolerance=0.2)
    cj = os.path.join(OUT, f"{chave}.json")
    with open(cj, "w") as f:
        json.dump(tri, f, separators=(",", ":"))
    kb = os.path.getsize(cj) // 1024
    manifest.append({"arquivo": f"{chave}.json", "grupo": chave, "rotulo": rotulo, "pecas": len(sols), "triangulos": len(tri) // 9})
    print(f"  {chave:9s} {len(sols):2d} peças  {len(tri)//9:6d} triângulos  {kb} KB json")
bb = Compound(children=[s for _, s in partes]).bounding_box()
manifest_obj = {"versao": "0.6", "data": "2026-10-27", "grupos": manifest,
                "bbox_mm": [round(bb.size.X, 1), round(bb.size.Y, 1), round(bb.size.Z, 1)]}
json.dump(manifest_obj, open(os.path.join(OUT, "manifest.json"), "w"), ensure_ascii=False, indent=1)
print("Saída em", OUT)
