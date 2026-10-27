# 003 — Rosca das hastes: M6 x 1,0

**Data:** 2026-10-27
**Status:** decidido

## Contexto
No Epic Extender, 10 voltas do punho deslocam 9,3 mm (régua) e o diâmetro da haste mede 5,9 mm (paquímetro). Barra roscada M6 comercial mede 5,8 a 5,95 mm, então o Epic usa M6 x 1,0; os 9,3 mm foram erro de leitura da régua.

## Decisão
Usar **M6 x 1,0, inox 304** nas hastes, no punho (castanha), nos tambores do pivô e nas contraporcas. Não importa qual é a rosca do Epic: a nossa é uma escolha de projeto.

## Motivos
- Padrão métrico brasileiro: barra roscada, porca, inserto e ferramenta M6 em qualquer loja.
- 1/4"-28 é padrão americano, difícil de achar no Brasil e sem vantagem funcional.
- Passo de 1 mm por volta dá ajuste fino e confortável de comprimento.

## Consequências
- `ROSCA_D = 6.0` e `ROSCA_PASSO = 1.0` em `02-produto/cad/parametros.py` passam a status DEF.
- O Epic também é M6, então a nossa haste é intercambiável com a dele.
