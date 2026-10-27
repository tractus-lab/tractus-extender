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
Versão 0.5.1: alça de arame do copo removida do modelo (pertence a outro sistema de tração, fora do projeto). Versão 0.5 (2026-10-27, noite): a peça que segura o copo é uma **ponte** única entre as hastes, com rebaixo circular aberto de um lado onde o pescoço do copo encaixa (descrição do usuário). Substitui os dois porta-copos da v0.3. Versão 0.4 (2026-10-27, noite): mecanismo confirmado pelo usuário. Haste roscada única por lado, fixa nas pontas; punho é a castanha, com furo liso em cima; mola de compressão passa por dentro do punho e do tubo da escala e apoia no porta-copo; o tubo entra no punho sob tração. Parâmetro `CARGA_LB` mostra a montagem em repouso ou carregada (prévia `montagem_frente_22lb`). Mola estimada: 2,45 N/mm, curso 40 mm. Versão 0.3 (2026-10-27, noite): com a foto 08 (kit montado com o copo) ficou claro que não há guia central: cada haste tem um **porta-copo** com braço curvo, e a alça de arame do copo engancha nos dois braços. O copo fica entre as hastes, válvula para a barra e boca para a base. Comprimentos do punho e das roscas expostas atualizados pela foto 08. Versão 0.2 (mesmo dia): arquitetura observada nas fotos do P00 (base em ferradura com pivôs, hastes com punho e tubo de mola, barra superior com olhais, copo em sino com válvula e alça). Dimensões marcadas **FOTO** (±2 mm) em `parametros.py`. Não serve para fabricar. Faltam: medidas de paquímetro, rosca real, mola, interior da válvula, membrana, mangas, bomba, arredondamentos.

## Ver o modelo 3D
Três jeitos, do mais fácil ao mais completo:
1. **Página publicada** (link no README principal): gira no navegador, sem instalar nada. Gerada por `gerar_visualizador.py` a partir de `visualizador.html` + STLs em `saida/visualizador/`. Precisa ser republicada a cada versão.
2. **https://3dviewer.net/**: arraste qualquer `.stl` de `saida/stl/` ou de `saida/visualizador/`.
3. **FreeCAD**: Arquivo → Importar → `saida/step/montagem.step`. É o jeito de medir, cortar e editar.
