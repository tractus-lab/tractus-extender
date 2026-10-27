# 003 — Rosca das hastes: M6 x 1,0

**Data:** 2026-10-27
**Status:** decidido

## Contexto
No Epic Extender, 10 voltas do punho deslocam 9,3 mm (medido com régua). Isso é compatível tanto com M6 x 1,0 (10 mm) quanto com 1/4"-28 UNF (9,1 mm). Não medimos o diâmetro com paquímetro.

## Decisão
Usar **M6 x 1,0, inox 304** nas hastes, no punho (castanha), nos tambores do pivô e nas contraporcas. Não importa qual é a rosca do Epic: a nossa é uma escolha de projeto.

## Motivos
- Padrão métrico brasileiro: barra roscada, porca, inserto e ferramenta M6 em qualquer loja.
- 1/4"-28 é padrão americano, difícil de achar no Brasil e sem vantagem funcional.
- Passo de 1 mm por volta dá ajuste fino e confortável de comprimento.

## Consequências
- `ROSCA_D = 6.0` e `ROSCA_PASSO = 1.0` em `02-produto/cad/parametros.py` passam a status DEF.
- Se o diâmetro medido do Epic der 6,35 mm, não muda nada aqui.
