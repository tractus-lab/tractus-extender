# Mola de tração do extensor: o que se sabe e a estimativa da geometria

Atualizado em 2026-10-29.

## Medido (P00, 2026-10-27)

| Grandeza | Valor | Como |
|---|---|---|
| Constante da mola | 0,255 kgf/mm = **2,5 N/mm** | 2 kg → 8,0 mm e 4 kg → 15,4 mm, régua; linear nos dois pontos |
| Fundo de escala | 22 lb = 10 kg = 98 N | escala impressa no tubo |
| Curso no fundo de escala | ~39 mm | 98 N ÷ 2,5 N/mm |
| Diâmetro externo do tubo da escala | 15,6 mm | paquímetro |

## Espaço disponível (do CAD)

- Por dentro passa a haste M6: diâmetro interno da mola ≥ 7,5 mm para não raspar.
- Por fora, o furo do tubo: ~13,6 mm (parede do tubo estimada em 1,0 mm). Diâmetro externo da mola ≤ 13 mm.
- Comprimento em repouso ~105 mm (do fundo do furo do punho à ponte, estimado). A 22 lb fica com ~66 mm, e nessa altura as espiras ainda não podem encostar umas nas outras.

## Cálculo

Mola helicoidal de compressão: k = G·d⁴ / (8·D³·n), com G o módulo de cisalhamento do arame, d o diâmetro do arame,
D o diâmetro médio (externo − d) e n as espiras ativas. Tensão na espira a 22 lb: τ = Kw·8·F·D / (π·d³), com o
fator de Wahl Kw. Limite estático adotado: 45 % da resistência à tração do arame (Shigley: inox 302 A = 1867 MPa·mm^m,
m = 0,146; arame de piano ASTM A228 A = 2211, m = 0,145).

Varredura de arame 1,2 a 1,8 mm e diâmetro externo 11 a 13 mm. Critérios: cabe na haste e no tubo, não dá bloco antes
dos 22 lb (comprimento de bloco ≤ 61 mm) e tensão abaixo do limite.

| Arame | D ext | Espiras ativas (inox / aço mola) | Bloco | Tensão a 22 lb | Veredito |
|---|---|---|---|---|---|
| 1,2 a 1,4 mm | qualquer | 5 a 17 | curto | 1 060 a 1 950 MPa | **não aguenta**: arame fino demais para 98 N |
| 1,5 mm | 11 | 20 / 23 | 34 a 38 mm | 870 MPa | só em aço mola, no limite |
| **1,6 mm** | **12** | **20 / 23** | **35 a 40 mm** | **780 MPa** | **melhor candidata**: cabe com folga, bloco longe dos 66 mm, tensão no limite para inox e folgada para aço mola |
| 1,6 mm | 13 | 15 / 18 | 28 a 31 mm | 840 MPa | só em aço mola |
| 1,8 mm | 12,5 a 13 | 26 a 30 / 30 a 34 | 50 a 57 mm | 575 a 595 MPa | aguenta sobrando, mas o bloco chega perto dos 66 mm e o diâmetro interno (8,9) fica justo |

## Estimativa adotada no CAD

- Arame **1,6 mm**, diâmetro externo **12 mm** (interno 8,8), **20 espiras ativas** em inox 302 (22 com as pontas fechadas) ou 23 em aço mola.
- Comprimento livre ~105 mm, passo ~5 mm, comprimento de bloco ~35 mm.
- Pontas fechadas e esmerilhadas (apoio plano no punho e na ponte).

A tensão a 22 lb fica no limite para inox; na prática molas assim recebem "pré-assentamento" (set) e aguentam. Se o
fabricante reclamar, a alternativa é arame 1,8 mm com 13 mm de externo, ou aço mola com acabamento zincado (não precisa
ser inox: a mola fica dentro do tubo, sem contato com a pele).

## Como confirmar

1. Tirar a mola do punho (soltar a contraporca de cima e a barra, puxar o tubo) e medir arame, diâmetro externo, espiras e comprimento livre com paquímetro.
2. Ou, sem desmontar: enfiar o paquímetro de profundidade no tubo pela ponte e ler até o fim da mola.
3. Pedir ao fabricante de molas (termos no glossário: compression spring / 压缩弹簧) com k = 2,5 N/mm ± 10 %, D ext 12, L livre 105, curso útil 45 mm, e conferir a força com pesos como no P00.

## Mola do nosso produto (não do Epic)

Requisito RF-01: máximo 5 kg (49 N). Duas opções com o mesmo espaço:

| Opção | k | Curso a 5 kg | Arame | Externo | Espiras ativas (inox) | Comentário |
|---|---|---|---|---|---|---|
| A | 1,25 N/mm | 39 mm | 1,3 mm | 12 mm | ~16 | mesma escala de 40 mm do Epic, mas 1 kg = 8 mm: duas vezes mais legível; tensão a 5 kg ~650 MPa, folgada |
| B | 2,5 N/mm (a mesma do Epic) | 20 mm | 1,6 mm | 12 mm | ~20 | aproveita a mesma mola; curso curto, escala apertada |

Recomendação: **opção A**. O batente de fim de curso (RF-03) fica em 40 mm, onde a mola marca 5 kg.
