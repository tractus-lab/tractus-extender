# CAD paramétrico do extensor

Modelo 3D do produto escrito em Python com [build123d](https://build123d.readthedocs.io/). Toda dimensão vive em `parametros.py`; as peças em `pecas.py`; `gerar.py` exporta tudo.

## Por que CAD em código
- Mudar o diâmetro de um copo é mudar um número. Os cinco tamanhos saem do mesmo código.
- Versionável no git: dá para ver o que mudou entre versões do produto.
- Natural para quem programa. Sem curva de aprendizado de interface.
- Exporta STEP (o que fabricantes e o FreeCAD leem) e STL (o que a impressora 3D lê).

Formas orgânicas (almofada ergonômica, pegas) ficam melhores no FreeCAD. Os dois convivem: o STEP gerado aqui abre no FreeCAD.

## Instalação
```bash
cd 02-produto/cad
python3 -m venv .venv
.venv/bin/pip install build123d cairosvg
```

## Uso
```bash
.venv/bin/python gerar.py
```
Saída:
- `saida/step/` — um STEP por peça e `montagem.step` com o conjunto. Abrir no FreeCAD: Arquivo → Importar.
- `saida/stl/` — um STL por peça, pronto para o fatiador (Bambu Studio, Cura, PrusaSlicer).
- `preview/` — SVG e PNG da montagem em três vistas, para olhar sem abrir CAD.

`saida/` não vai para o git (é gerado). `preview/` vai, para acompanhar a evolução visual.

## Fluxo de trabalho
1. Medir o produto real (ver `../engenharia/mecanica/como-fazer-o-blueprint.md`).
2. Trocar os valores `EST` em `parametros.py` por `MED`.
3. Rodar `gerar.py`. Abrir a prévia. Comparar com as fotos.
4. Imprimir uma peça. Comparar com a original. Ajustar.
5. Commit a cada versão que faz sentido.

## Estado atual
Versão 0.2 (2026-10-27): arquitetura observada nas fotos do P00 (base em ferradura com pivôs, hastes com punho e tubo de mola, guia central, barra superior com olhais, copo em sino com válvula e alça). Dimensões marcadas **FOTO** (±2 mm) em `parametros.py`. Não serve para fabricar. Faltam: medidas de paquímetro, rosca real, mola, interior da válvula, membrana, mangas, bomba, arredondamentos.

## Visualizador rápido sem instalar nada
Arraste um `.stl` em https://3dviewer.net/ ou abra o STEP no FreeCAD.
