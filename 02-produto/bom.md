# Lista de materiais (BOM)

Versão: 0.2 (estimativa de custos, sem cotação)
Data: 2026-10-29

Custos em R$ por kit (1 extensor completo). Duas colunas: **1 unidade** (protótipo, comprando no varejo e mandando
fazer peça a peça) e **1.000 unidades** (lote, com fornecedor e, onde indicado, molde). Tudo é estimativa a partir de
preços públicos de 2026 e de experiência com peças parecidas; nada foi cotado. Dólar a R$ 5,80. Peças importadas
chegam com ~90 % em cima do preço FOB (imposto de importação 60 % + ICMS + frete + despachante), já incluído onde diz
"China, posto no Brasil". Os números servem para decidir o que fazer onde, não para fechar preço.

## 1. Peças compradas prontas (commodities)

| # | Peça | Qtd/kit | Especificação | 1 un. (R$) | 1.000 un. (R$/kit) | De onde | Observações |
|---|---|---|---|---|---|---|---|
| 1 | Haste roscada | 2 | M6 × 1,0 inox 304, ~280 mm, pontas chanfradas | 16 | 10 | barra de 1 m nacional cortada (3 hastes por barra) | China cortada no tamanho: ~R$ 3/haste FOB. Referência: barra 1 m inox no exterior ~R$ 25 |
| 2 | Contraporca sextavada | 2 | M6 inox 304 (ou aço com zinco preto) | 1 | 0,40 | ferragem | Epic tem 4; a proposta de montagem usa 2 |
| 3 | Porca de cima da barra | 2 | porca cega M6 inox (no lugar da Allen embutida) | 3 | 1 | ferragem | Allen cilíndrica embutida custaria R$ 4 a 8 cada no varejo e exige rebaixo usinado; porca cega é padrão e faz o mesmo papel |
| 4 | Mola de compressão | 2 | arame 1,6, ext. 12, ~20 espiras, livre ~105, k = 2,5 N/mm, inox 302 ou aço mola zincado | 40 | 6 | fabricante de molas (SP/RS); China ~R$ 1,50 FOB | Pequena quantidade sob medida sai R$ 15 a 30 cada; em 2.000 molas cai para R$ 2 a 4 |
| 5 | Pino do pivô | 2 | inox 4 × 20 mm | 2 | 0,40 | ferragem | Pino elástico (roll pin) dispensa as tampas |
| 6 | Tubo da escala | 2 | alumínio 6063 16 × 1 mm, ~62 mm, anodizado preto, escala gravada a laser | 26 | 10 | serralheria + anodizador + gravação | 1 un.: tubo de 1 m anodizado (~R$ 40) + gravação avulsa. Padrão é 16 mm; os 15,6 do Epic são irrelevantes |
| 7 | Copo de vácuo com válvula | 1 | transparente, boca ~44 mm, válvula de retenção + alívio | 90 | 45 | China, posto no Brasil (kit do mesmo fabricante dos genéricos) | FOB US$ 2,5 a 4 em lote; sozinho só vem dentro do kit (US$ 8 a 15) |
| 8 | Mangas de silicone | 3 | 21 / 26 / 32 mm, parede 2,5, altura 83 | 25 | 15 | China, posto no Brasil | FOB US$ 0,5 a 1 cada; molde de compressão nacional (R$ 12 a 20 mil) só compensa acima de 3.000 kits |
| 9 | Bomba manual | 1 | pera ou pistão com mangueira | 50 | 35 | China, posto no Brasil | Anúncio público: US$ 3,15 acima de 1.000 peças (US$ 4,50 avulso) |
| 10 | Embalagem + manual | 1 | caixa, berço, manual em português | 30 | 15 | gráfica nacional | |
| | **Subtotal compradas** | | | **283** | **138** | | |

## 2. Peças feitas sob projeto (precisam de molde, usinagem ou impressão 3D)

Para 1.000 unidades há duas rotas. **Rota A**: impressão 3D industrial (MJF/SLS em nylon PA12) e corte a laser, sem
molde. **Rota B**: molde de injeção nacional, com o molde diluído nos 1.000 kits. O custo do molde é o que decide.

| # | Peça | Qtd/kit | Material | 1 un. (R$) | 1.000 un., rota A (R$/kit) | 1.000 un., rota B (R$/kit) | Molde (R$) | Observações |
|---|---|---|---|---|---|---|---|---|
| 11 | Ferradura, metade plástica com os garfos do pivô | 1 | nylon PA12 (MJF) ou PA6/ABS injetado | 200 | 80 | 8 + 40 de molde = 48 | 35 a 50 mil | ~40 cm³; MJF cobra por volume (R$ 1,5 a 3/cm³ em lote) |
| 12 | Ferradura, face de borracha | 1 | TPE sobremoldado ou silicone 30 Shore A colada | 30 | 20 (silicone em molde de compressão simples) | 5 + 20 de molde = 25 | 15 a 25 mil (2º tiro ou molde próprio) | 1 un.: silicone vazado num molde impresso em 3D |
| 13 | Punho recartilhado | 2 | nylon MJF ou ABS injetado, com porca M6 cativa | 80 | 70 | 5 + 25 de molde = 30 | 20 a 30 mil (2 cavidades) | Porca sextavada presa num alojamento: nada de rosca no plástico nem inserto quente |
| 14 | Tambor do pivô | 2 | inox 303/304 torneado, rosca M6 interna, lingueta fresada | 120 | 25 | 25 | — | Torno CNC em lote: R$ 8 a 15 cada. China: US$ 1 a 2 |
| 15 | Ponte | 1 | chapa de alumínio 4,5 mm cortada a laser, furos e rasgo no corte, anodizada | 120 (CNC) | 10 | 10 | — | Sem molde: corte a laser + rebaixo de 1,5 mm por fresa simples ou por gravação |
| 16 | Barra superior | 1 | chapa de alumínio 4 mm cortada a laser e dobrada em "[", 2 furos | 150 (CNC) | 8 | 8 | — | Os cilindros de 16 mm do Epic viram só a chapa; a porca cega faz o acabamento de cima |
| 17 | Tampas do pino | 4 | — | 0 | 0 | 0 | — | Eliminadas pelo pino elástico (ver montagem) |
| | **Subtotal sob projeto** | | | **700** | **213** | **146 (+ R$ 70 a 105 mil de molde antes do 1º kit)** | | |

## 3. Montagem e teste

| Item | 1 un. | 1.000 un. (R$/kit) | Observações |
|---|---|---|---|
| Montagem (sequência de 8 passos, ver `montagem-facil.md`) | seu tempo | 12 | ~20 min por kit a R$ 35/h com encargos |
| Teste de força (pesos ou dinamômetro, 2 pontos) | seu tempo | 3 | 5 min |
| Perdas e refugo (4 %) | — | 15 | |
| **Subtotal** | — | **30** | |

## 4. Resumo

| | 1 unidade | 1.000 un., rota A (sem molde) | 1.000 un., rota B (molde nacional) |
|---|---|---|---|
| Compradas | 283 | 138 | 138 |
| Sob projeto | 700 | 213 | 146 |
| Montagem e teste | — | 30 | 30 |
| **Custo por kit** | **~R$ 980** | **~R$ 380** | **~R$ 315 + molde R$ 70 a 105 mil** |

Para comparar: kit genérico chinês completo, OEM com a sua marca, sai por US$ 6 a 12 FOB, ou R$ 65 a 130 posto no
Brasil. É o piso do mercado e o que o Epic provavelmente paga pelas peças de vácuo.

### O que isso diz

- **A R$ 500 de venda, 1.000 unidades não fecham com molde nacional.** Do preço saem Simples (~8 %), taxa do
  marketplace (12 a 17 %), anúncios (~10 %) e frete grátis: sobram R$ 300 a 340. A rota A custa 380 e a rota B custa
  315 sem contar o molde. O negócio só fica positivo em 3.000 a 5.000 kits (molde diluído a R$ 15 a 25) ou com preço
  de R$ 600 a 700.
- **Os três maiores custos são copo + bomba + mangas importados (R$ 95), as peças plásticas (R$ 100 a 150) e os
  tambores (R$ 25).** Não é a ferragem: hastes, porcas, molas e pinos juntos dão R$ 18.
- **Onde cortar:** (1) comprar o conjunto de vácuo direto do fabricante chinês do Epic, com volume, baixa para R$ 60 a
  70; (2) trocar os tambores torneados por um pivô de plástico com porca cativa (R$ 5 o par) se o teste de carga
  permitir; (3) fazer ponte e barra em chapa cortada a laser, como já está acima, em vez de usinar.
- **Para o protótipo (1 unidade), R$ 1.000** é o custo de fazer tudo sob medida. Mais barato: comprar um kit genérico
  chinês (R$ 120 a 150 no varejo) e aproveitar copo, bomba, mangas e até hastes, fazendo só ferradura, punhos, ponte e
  barra. Sai por R$ 500 a 600 e já serve para testar o projeto.

## 5. Itens críticos

- **Copo e válvula**: fornecedor único (China), é o coração do produto e o que define a qualidade percebida. Pedir
  amostras de 2 ou 3 fabricantes antes de qualquer lote.
- **Mola**: precisa de teste de força em 100 % das peças no começo (a constante define a escala impressa no tubo).
- **Molde da ferradura**: maior investimento; só encomendar depois de validar a forma em MJF com usuários.

## Histórico de versões
| Versão | Data | O que mudou |
|---|---|---|
| 0.1 | 2026-10-25 | Criação do arquivo |
| 0.2 | 2026-10-29 | Estimativa de custos por peça em 1 e 1.000 unidades, duas rotas para as peças de projeto, resumo e leitura do resultado |
