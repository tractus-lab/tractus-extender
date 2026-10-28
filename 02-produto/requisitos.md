# Requisitos do produto (PRD)

## Visão
Uma frase sobre o que o produto é e para quem.

## Objetivos
O que o produto precisa alcançar para ser considerado sucesso? (ex.: "reduzir o tempo de X de 10 para 2 minutos")

## Fora de escopo
O que o produto NÃO vai fazer na primeira versão. Tão importante quanto o que vai.

## Requisitos funcionais
O que o produto faz. Numere para poder referenciar.

| ID | Requisito | Prioridade (Essencial / Importante / Desejável) | Origem (entrevista, norma, hipótese) |
|---|---|---|---|
| RF-01 | | | |

## Requisitos não funcionais
Como o produto é: tamanho, peso, durabilidade, autonomia, materiais, resistência à água, temperatura de operação, vida útil, ruído.

| ID | Requisito | Valor alvo | Como medir |
|---|---|---|---|
| RNF-01 | Nenhuma aresta ou ponta viva em peça que o usuário toque: todas as arestas externas arredondadas | raio ≥ 2 mm nas peças grandes, ≥ 1 mm nas pequenas | inspeção visual e ao toque; no CAD, `RAIO_ARESTA` em `parametros.py` |
| RNF-02 | Face da base que encosta na virilha em material elastomérico firme e confortável (como no Epic: metade de baixo da ferradura em borracha) | dureza a definir (referência Shore A 60–80); sem cheiro; lavável | comparação com o Epic; teste de uso |
| RNF-03 | Manga de vedação em silicone macio e elástico: veste o copo com ~44% de alongamento sem rasgar | alongamento de ruptura ≥ 400%; dureza a definir (referência Shore A 20–30) | ficha técnica do silicone; teste de montagem repetida |
| RNF-04 | Peças de plástico com acabamento de qualidade: sem rebarba, sem marca de injeção visível na face externa | igual ou melhor que o Epic | inspeção visual |

## Requisitos regulatórios
Vindos de `01-pesquisa/normas-e-certificacoes.md`.

## Requisitos de custo
- Custo unitário alvo de fabricação: R$
- Preço de venda alvo: R$
- Margem mínima aceitável: %

## Experiência do usuário
Como é abrir a caixa, usar pela primeira vez, usar no dia a dia, limpar, guardar, descartar?

## Perguntas em aberto
