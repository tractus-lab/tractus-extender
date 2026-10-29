# Requisitos do produto (PRD)

## Visão
Uma frase sobre o que o produto é e para quem.

## Objetivos
O que o produto precisa alcançar para ser considerado sucesso? (ex.: "reduzir o tempo de X de 10 para 2 minutos")

## Fora de escopo
O que o produto NÃO vai fazer na primeira versão. Tão importante quanto o que vai.

- Tração acima de 5 kg e curso para mais de ~20 cm esticado: o Epic faz, nós não (fundador, 2026-10-29). Não é limitação, é escolha de segurança e de público.
- Olhais para tração alternativa por elástico ou cordão.

## Requisitos funcionais
O que o produto faz. Numere para poder referenciar.

| ID | Requisito | Prioridade (Essencial / Importante / Desejável) | Origem (entrevista, norma, hipótese) |
|---|---|---|---|
| RF-01 | Força de tração regulável e legível numa escala em kg, com **máximo de 5 kg** (o Epic vai a 10 kg; fundador considera acima de 5 kg inseguro) | Essencial | fundador, 2026-10-29; literatura de tração usa 0,6 a 1,5 kg por sessão, então 5 kg já é folga grande |
| RF-02 | Curso de comprimento dimensionado para o público real, não para 25 cm ou mais como o Epic: comprimento máximo esticado alvo de **~20 cm** (a confirmar com dados antropométricos e entrevistas) | Essencial | fundador, 2026-10-29; hipótese de valor a validar |
| RF-03 | Batente mecânico que impede ultrapassar a força máxima (a mola chega ao fim do curso antes de passar de 5 kg) | Importante | decorrente de RF-01 |

## Requisitos não funcionais
Como o produto é: tamanho, peso, durabilidade, autonomia, materiais, resistência à água, temperatura de operação, vida útil, ruído.

| ID | Requisito | Valor alvo | Como medir |
|---|---|---|---|
| RNF-01 | Nenhuma aresta ou ponta viva em peça que o usuário toque: todas as arestas externas arredondadas | raio ≥ 2 mm nas peças grandes, ≥ 1 mm nas pequenas | inspeção visual e ao toque; no CAD, `RAIO_ARESTA` em `parametros.py` |
| RNF-02 | Face da base que encosta na virilha em material elastomérico firme e confortável (como no Epic: metade de baixo da ferradura em borracha) | dureza a definir (referência Shore A 60–80); sem cheiro; lavável | comparação com o Epic; teste de uso |
| RNF-03 | Manga de vedação em silicone macio e elástico: veste o copo com ~44% de alongamento sem rasgar | alongamento de ruptura ≥ 400%; dureza a definir (referência Shore A 20–30) | ficha técnica do silicone; teste de montagem repetida |
| RNF-04 | Peças de plástico com acabamento de qualidade: sem rebarba, sem marca de injeção visível na face externa | igual ou melhor que o Epic | inspeção visual |
| RNF-05 | Mola dimensionada para 5 kg no fim do curso, com escala legível: k ≈ 1,25 N/mm em 40 mm de curso (metade do Epic), ou 2,5 N/mm em 20 mm | erro da escala ≤ 10 % em 1, 3 e 5 kg | pesos pendurados no copo, como no P00 |
| RNF-06 | Hastes mais curtas que as do Epic (280 mm), na medida do curso de RF-02; aparelho mais discreto e barato | comprimento a definir no CAD do nosso produto | medir o curso útil na montagem |

## Requisitos regulatórios
Vindos de `01-pesquisa/normas-e-certificacoes.md`.

## Requisitos de custo
- Custo unitário alvo de fabricação: R$
- Preço de venda alvo: R$
- Margem mínima aceitável: %

## Experiência do usuário
Como é abrir a caixa, usar pela primeira vez, usar no dia a dia, limpar, guardar, descartar?

## Perguntas em aberto
