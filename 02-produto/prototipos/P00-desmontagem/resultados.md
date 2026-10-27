# P00 — Resultados parciais (fotos de 2026-10-27, antes de medir)

Sete fotos sobre papel milimetrado A3. Escala obtida por software a partir da grade: ~8,9 px/mm nos originais. Medidas abaixo são **FOTO** (±2 mm, mais para peças altas por paralaxe). Serão substituídas pelas do paquímetro.

## Arquitetura observada (muda tudo em relação ao modelo v0.1)

1. **Base em ferradura**, não anel fechado. Arco de ~106 mm de largura e ~99 mm de altura em planta, abertura interna ~60 mm, vão entre os lobos ~31 mm. Dois lobos arredondados nas pontas. Plástico preto fosco (provavelmente nylon ou ABS, talvez com revestimento macio: confirmar ao toque).
2. **Articulação nas hastes.** Cada haste rosqueia num tambor de inox (~12 × 31 mm) alojado num rasgo da base e preso por um pino transversal. Os dois pinos são colineares: formam uma dobradiça que deixa a estrutura inteira inclinar em relação à base, e dobrar totalmente para guardar (é assim que o kit está nas fotos: deitado, com as hastes dobradas sobre o arco).
3. **Hastes, de baixo para cima** (comprimentos ao longo do eixo):
   | Trecho | Comp. (mm) | Diâm. (mm) | Observação |
   |---|---|---|---|
   | Tambor do pivô (inox) | 31 | 12 | parte dentro da base |
   | Porca sextavada preta | 5 | 10 entre faces | rosca provável M6 |
   | Haste roscada inox exposta | 53 | 6 | |
   | Punho serrilhado preto | 65 | 26 | porca longa de ajuste |
   | Tubo da escala (preto, "LB 0–22") | 50 | 18 | abriga a mola |
   | Ponte | 13 | 112 | plataforma única; rebaixo circular aberto de um lado para o pescoço do copo |
   | Haste roscada inox exposta | 43 | 6 | varia com o ajuste |
   | Cilindro da barra superior | 38 | 16 | com porca por baixo |
   Entre eixos das hastes: ~83 mm.
4. **Barra superior "EPIC"**: alumínio anodizado preto. Dois cilindros (16 × 38 mm) unidos por uma tira plana de ~17 mm de altura; olhal (~11 mm, furo ~5 mm) na ponta de cada cilindro. Comprimento total ~117 mm.
5. **Copo de vácuo**: transparente (acrílico ou policarbonato), formato de sino. Corpo ~47 mm de diâmetro externo e ~44 mm de altura, três anéis externos junto à boca (passo ~9,5 mm, diâmetro ~49 mm nos anéis), ombro cônico, pescoço ~13 × 7 mm, corpo de válvula branco ~20 × 28 mm com marca vermelha, alça triangular de arame inox (~39 mm de comprimento, ~33 mm de largura, arame ~2 mm). Comprimento total com alça ~92 mm. **Tamanho nominal a confirmar** (provável 40 ou 44).

## Funcionamento (confirmado pelo usuário em 2026-10-27, à noite)

1. **Haste roscada única por lado**, de ponta a ponta: fixa no tambor do pivô embaixo e na barra "EPIC" em cima, com contraporca nas duas pontas. Não gira.
2. **Base em ferradura**: apoia o corpo; o pivô deixa mudar o ângulo entre a base e as hastes.
3. **Barra "EPIC"**: só proteção das pontas e batente. Sem função mecânica.
4. **Punho serrilhado** (castanha): gira guiado pela rosca e define o comprimento do aparelho. Esconde a mola.
5. **Tubo da escala** (mais fino, marcado em libras): preso ao punho por dentro, pela mola, e com a "ponte" no topo.
6. **Ponte** entre as duas hastes, no topo dos tubos: plataforma única com um rebaixo circular no meio, aberto de um lado, onde encaixa o pescoço cilíndrico do copo. Na foto 08 ela aparece de lado, e o entalhe visto de perfil é o que parecia "dois braços". A alça de arame não segura o copo na ponte.
7. **Uso**: o pênis puxa o copo, o copo puxa a ponte, a ponte empurra o tubo para dentro do punho, a mola comprime e a borda do punho aponta a força. Em repouso a borda está no 0 (foto 08).

### Consequências para o modelo (CAD v0.4)
- O punho precisa de rosca interna só num trecho curto (estimado 13 mm) e de um furo liso de ~18,5 mm para o tubo entrar.
- A ponte e o tubo deslizam na haste com furo liso; só o punho rosqueia.
- A mola não cabe só no punho: para um curso de 40 mm (distância entre o 0 e o 22 na foto 08) ela precisa passar por dentro do tubo e apoiar na ponte. Comprimento livre estimado ~105 mm, 65 mm a 22 lb.
- Constante da mola: 22 lb = 97,9 N em 40 mm → **~2,45 N/mm (0,25 kgf/mm)**. Esse é o número a confirmar com dinamômetro.

### A confirmar
1. Passo da rosca: girar o punho 10 voltas e medir a variação de comprimento (10 mm = M6 passo 1).
2. Curso real: puxar até o 22 e medir quanto o tubo entrou no punho (modelo usa 40 mm).
3. Força real: dinamômetro no copo, ler no 11 e no 22, comparar com a escala.
4. Diâmetro do rebaixo da ponte e para que lado ele abre (mesmo lado da abertura da ferradura?).

## Foto 08: kit montado com o copo (2026-10-27, noite)

O que a foto mostra, da barra para a base, ao longo de cada haste (medidas pela grade, ±2 mm):

| Trecho | Comp. (mm) | Observação |
|---|---|---|
| Cilindro da barra "EPIC" | 39 | porca sextavada preta entre o cilindro e a rosca |
| Rosca inox exposta (superior) | 40 | |
| Ponte | 13 | plataforma única entre as hastes, com entalhe em U para o pescoço do copo (vista de lado na foto) |
| Tubo da escala "LB" | 50 | marcas 22 20 18 15 13 11 9 7 4 2 0; o **22 fica junto ao porta-copo e o 0 junto ao punho** |
| Punho serrilhado | 68 | |
| Rosca inox exposta (inferior) | 64 | depende do ajuste do punho |
| Porca + tambor do pivô | 10 + 27 | porca preta encostada no tambor |
| Base (lobo até a borda externa) | 42 | |

Comprimento total neste ajuste: ~353 mm (borda externa da barra até a borda externa da base). Hastes a ~83 mm entre eixos.

**Copo**: fica entre as duas hastes, com a válvula voltada para a barra e a boca (com a manga preta de silicone montada) voltada para a base. O pescoço está encaixado no entalhe da ponte. A alça de arame em U que contorna o pescoço é de outro sistema de tração (cinta/elástico) e fica fora do projeto: não será modelada nem fabricada. A manga preta é a que estava montada; a membrana não aparece.

**Leitura da escala em repouso**: a borda do punho está exatamente no 0. Isso sugere que a borda do punho é a referência de leitura e que, sob tração, o tubo da escala desliza para dentro do punho (o punho tem 26 mm de diâmetro e o tubo 18). Teste 1 e 2 confirmam.

**Porcas**: há uma porca sextavada em cada extremidade das hastes (junto ao tambor e junto à barra). Isso indica que o trecho roscado inferior é fixo no tambor (porca trava) e o superior é fixo na barra (porca trava); o punho é a única "porca" que gira para ajustar. Se for assim, são **duas hastes roscadas por lado**, não uma: a inferior entra no punho e a superior termina dentro do tubo (pistão da mola). Teste 1 decide entre essa hipótese e a de haste única.

## Lista de peças vista até agora
| # | Peça | Qtd | Material aparente | Foto |
|---|---|---|---|---|
| 1 | Base ferradura | 1 | plástico preto | 07 |
| 2 | Tambor de pivô + pino | 2 | inox | 07 |
| 3 | Porca sextavada preta | 4 (2 no pivô, 2 na barra) | aço | 06, 07 |
| 4 | Haste roscada | 2 (ou 4, se a superior for separada) | inox | 01, 02 |
| 5 | Punho serrilhado | 2 | plástico ou alumínio preto | 01, 02 |
| 6 | Tubo da escala com mola interna | 2 | alumínio preto | 01, 02 |
| 7 | Ponte com entalhe para o copo | 1 | plástico preto | 01, 02, 08 |
| 8 | Barra superior "EPIC" | 1 | alumínio anodizado | 06 |
| 9 | Copo de vácuo com válvula e alça | 1 fotografado (de 5) | transparente + branco + inox | 03, 04, 05 |

Fotos: 01–02 kit dobrado, 03–05 copo solto, 06 barra, 07 base, 08 kit montado com copo.

Ainda não fotografados: demais copos, membranas, demais mangas de silicone, bomba, fita coesiva, extensões de haste (se houver), embalagem, manual.

## Qualidade percebida (primeira impressão pelas fotos)
- Acabamento muito bom: anodização uniforme, serrilhado limpo, inox polido.
- Muitas peças metálicas usinadas: isso é caro. A diferença de custo entre o Epic e o genérico chinês está aqui, não no plástico.
- O copo é a peça mais complexa (sino + anéis + pescoço + válvula + alça). Provavelmente é a mesma peça dos kits genéricos.

## Próximas medidas (paquímetro)
Ver `02-produto/engenharia/mecanica/levantamento-dimensional.md`. Prioridade: diâmetro e passo da rosca, diâmetro interno dos copos, espessura da base, dimensões do tambor e do pino, curso e força da mola.
