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
    "plastico": ("Plástico preto (base, punhos, ponte, tampas do pivô)", ["base_plastico", "punho_", "ponte", "pivo_tampa_"]),
    "inox": ("Inox (tambores, pinos, hastes, porcas, molas)", ["pivo_tambor_", "pivo_pino_", "rosca_", "porca_", "mola_"]),
    "aluminio": ("Alumínio anodizado (tubos da escala, barra)", ["tubo_mola", "barra_superior"]),
    "copo": ("Copo de vácuo (transparente) com válvula", ["copo"]),
    "silicone": ("Silicone (manga sobre o copo)", ["manga", "membrana"]),
    "borracha": ("Borracha firme (metade de baixo da ferradura)", ["base_borracha"]),
}
ROTULOS = {
    "base_plastico": "Ferradura, metade de cima", "base_borracha": "Ferradura, face de borracha",
    "pivo_tambor": "Tambor do pivô", "pivo_pino": "Pino do pivô", "pivo_tampa_ext": "Tampa do pivô, face externa", "pivo_tampa_int": "Tampa do pivô, face interna",
    "porca_pivo": "Contraporca do pivô", "porca_barra": "Contraporca da barra", "porca_cil_barra": "Porca cilíndrica Allen da barra", "rosca": "Haste roscada M6",
    "punho": "Punho (castanha)", "tubo_mola": "Tubo da escala", "mola": "Mola", "ponte": "Ponte",
    "barra_superior": "Barra superior", "copo": "Copo de vácuo", "manga": "Manga de silicone", "membrana": "Membrana",
}
LADOS = {"esq": "esq.", "dir": "dir."}


def rotulo_peca(nome):
    """'punho_esq' -> 'Punho (castanha), esquerdo'."""
    base, _, lado = nome.rpartition("_")
    if lado in LADOS and base in ROTULOS:
        return f"{ROTULOS[base]} ({LADOS[lado]})"
    return ROTULOS.get(nome, nome)


partes = pecas.montagem()
manifest = []
for chave, (rotulo, prefixos) in GRUPOS.items():
    sols = [s for n, s in partes if any(n.startswith(p) for p in prefixos)]
    comp = Compound(children=sols)
    # triângulos em JSON: lista plana x,y,z por vértice, 9 valores por triângulo, 2 casas decimais
    tri = []
    lista = []  # uma entrada por peça: nome, rótulo e faixa de triângulos dentro do arquivo do grupo
    for nome_sol, sol in [(n, s) for n, s in partes if any(n.startswith(p) for p in prefixos)]:
        tol = (0.3, 0.8) if nome_sol.startswith(("mola_", "rosca_")) else (0.05, 0.2)  # mola e rosca helicoidais: malha grossa
        verts, faces = sol.tessellate(*tol)
        inicio = len(tri) // 9
        for a, b, c in faces:
            for v in (verts[a], verts[b], verts[c]):
                tri.extend((round(v.X, 2), round(v.Y, 2), round(v.Z, 2)))
        lista.append({"nome": nome_sol, "rotulo": rotulo_peca(nome_sol), "inicio": inicio, "n": len(tri) // 9 - inicio})
    # STL depois do JSON: a malha fica guardada na peça, e a exportação fina só refaz o que estiver mais grosso
    export_stl(comp, os.path.join(OUT, f"{chave}.stl"), tolerance=0.05, angular_tolerance=0.2)
    cj = os.path.join(OUT, f"{chave}.json")
    with open(cj, "w") as f:
        json.dump(tri, f, separators=(",", ":"))
    kb = os.path.getsize(cj) // 1024
    manifest.append({"arquivo": f"{chave}.json", "grupo": chave, "rotulo": rotulo, "pecas": len(sols), "triangulos": len(tri) // 9, "lista": lista})
    print(f"  {chave:9s} {len(sols):2d} peças  {len(tri)//9:6d} triângulos  {kb} KB json")
bb = Compound(children=[s for _, s in partes]).bounding_box()
manifest_obj = {"versao": "0.9.7", "data": "2026-10-29", "grupos": manifest,
                "bbox_mm": [round(bb.size.X, 1), round(bb.size.Y, 1), round(bb.size.Z, 1)]}
json.dump(manifest_obj, open(os.path.join(OUT, "manifest.json"), "w"), ensure_ascii=False, indent=1)
print("Saída em", OUT)
