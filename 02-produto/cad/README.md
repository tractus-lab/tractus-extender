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
.venv/bin/pip install build123d bd_warehouse cairosvg
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
Versão 0.9 (2026-10-28): hastes com o fio de rosca ISO M6 × 1,0 modelado de verdade (`bd_warehouse.thread.IsoThread`), núcleo e fio como duas formas do mesmo conjunto (sem fusão booleana, que custa ~36 s por haste). Interruptor `ROSCA_COM_FIO` em `parametros.py` para voltar ao cilindro liso. Malha grossa no visualizador (~36 mil triângulos por haste). Versão 0.8.4 (2026-10-28): entre-eixos das hastes medido: 75,7 mm (81,6 externo − 5,9), contra 83 da foto; garfos do pivô passam a caber dentro dos 96 mm da ferradura (sobra 2,75 mm por lado); comprimento da ponte acompanha. Versão 0.8.3 (2026-10-28): tampa redonda do pino também na face interna de cada garfo (usuário): duas tampas por pivô. Versão 0.8.2 (2026-10-28): pivô remodelado como garfo (clevis) com as medidas do usuário: 14,8 mm no sentido do pino (duas bochechas de 4,2 + vão de 6,4), 17,6 mm no sentido da rotação; ponta do tambor rebaixada numa lingueta de 5,6 mm com ponta arredondada, que entra no vão com 0,4 mm de folga por lado. Substitui o rasgo de 13 mm onde o tambor inteiro entrava. Versão 0.8.1 (2026-10-28): ferradura medida: largura externa 96 mm, altura 18 mm, faixa do arco 20,2 mm de largura radial (raio interno 27,8); divisão plástico/borracha ainda estimada em 9 + 9. Posição da manga sobre o copo marcada como arbitrária (não é medida). Versão 0.8: ponte medida (chapa 4,5 mm, furo 12, rebaixo 20 × 1,5) com cubos de 13 mm nas hastes (foto, a confirmar); encaixe copo–ponte tipo fechadura, copo mostrado assentado no rebaixo como em uso. Versão 0.7.2: visualizador com caixa por peça (botão "peças" em cada grupo de material); o manifesto traz a faixa de triângulos de cada peça. Versão 0.7.1: copo com domo abaulado (spline, formato de glande) no lugar do ombro cônico, e seção levemente oval (`COPO_OVAL` 0,93, chute); altura do domo chutada em 14 mm dentro dos 43,6 medidos. Versão 0.7: arestas externas arredondadas (`RAIO_ARESTA` 2 mm, `RAIO_ARESTA_PEQ` 1 mm) na base, caixas do pivô, ponte, punho, barra, tampas e boca do copo; ferradura dividida em `base_plastico` (cima, com as caixas do pivô) e `base_borracha` (baixo, contato com a virilha); grupo "borracha" no visualizador. Versão 0.6.1: manga modelada como na foto 09, esticada só sobre os anéis do copo e no diâmetro de repouso abaixo (prévia `copo_com_manga`). Versão 0.6: o pivô fica em cima do lobo da ferradura, numa caixa de articulação com 17,6 mm de largura (medida), pino transversal e tampa plástica; o rasgo não entra na base. Versão 0.5.1: alça de arame do copo removida do modelo (pertence a outro sistema de tração, fora do projeto). Versão 0.5 (2026-10-27, noite): a peça que segura o copo é uma **ponte** única entre as hastes, com rebaixo circular aberto de um lado onde o pescoço do copo encaixa (descrição do usuário). Substitui os dois porta-copos da v0.3. Versão 0.4 (2026-10-27, noite): mecanismo confirmado pelo usuário. Haste roscada única por lado, fixa nas pontas; punho é a castanha, com furo liso em cima; mola de compressão passa por dentro do punho e do tubo da escala e apoia no porta-copo; o tubo entra no punho sob tração. Parâmetro `CARGA_LB` mostra a montagem em repouso ou carregada (prévia `montagem_frente_22lb`). Mola estimada: 2,45 N/mm, curso 40 mm. Versão 0.3 (2026-10-27, noite): com a foto 08 (kit montado com o copo) ficou claro que não há guia central: cada haste tem um **porta-copo** com braço curvo, e a alça de arame do copo engancha nos dois braços. O copo fica entre as hastes, válvula para a barra e boca para a base. Comprimentos do punho e das roscas expostas atualizados pela foto 08. Versão 0.2 (mesmo dia): arquitetura observada nas fotos do P00 (base em ferradura com pivôs, hastes com punho e tubo de mola, barra superior com olhais, copo em sino com válvula e alça). Dimensões marcadas **FOTO** (±2 mm) em `parametros.py`. Não serve para fabricar. Faltam: medidas de paquímetro, rosca real, mola, interior da válvula, membrana, mangas, bomba, arredondamentos.

## Ver o modelo 3D
Três jeitos, do mais fácil ao mais completo:
1. **Página publicada** (link no README principal): gira no navegador, sem instalar nada. Gerada por `gerar_visualizador.py` a partir de `visualizador.html` + STLs em `saida/visualizador/`. Precisa ser republicada a cada versão.
2. **https://3dviewer.net/**: arraste qualquer `.stl` de `saida/stl/` ou de `saida/visualizador/`.
3. **FreeCAD**: Arquivo → Importar → `saida/step/montagem.step`. É o jeito de medir, cortar e editar.
