# Como fazer o blueprint do Epic Extender

"Blueprint" aqui significa: lista de peças, medidas de cada peça, materiais, como as peças se encaixam, e um modelo 3D paramétrico que reproduz tudo isso. É engenharia reversa. O processo tem cinco etapas.

## Verdade inconveniente primeiro
**Sem o produto na mão, o blueprint é chute.** Fotos de site não dão espessura de parede, dureza do silicone, passo de rosca, constante da mola. Dá para começar o modelo com dimensões estimadas (é o que vamos fazer em `02-produto/cad/`), mas a primeira coisa a fazer é comprar a unidade. Um Epic Extender Full Set custa US$ 259 mais frete e imposto. É o investimento mais barato e mais informativo do projeto inteiro.

Compre também um genérico chinês com copo de vácuo (R$ 150 a 300 na Shopee) para comparar: onde o Epic é melhor, e como.

## Ferramentas (total R$ 200 a 400)
| Ferramenta | Para quê | Preço aprox. |
|---|---|---|
| Paquímetro digital 150 mm | Toda medida externa, interna e de profundidade. É a ferramenta principal. | R$ 40 a 120 |
| Balança de cozinha 0,1 g | Peso de cada peça (ajuda a estimar material e volume) | R$ 30 a 60 |
| Dinamômetro / balança de gancho 10 kg | Medir a força real das hastes em cada posição da escala | R$ 30 a 80 |
| Papel milimetrado ou tapete de corte com grade | Fundo para fotos com escala | R$ 10 a 40 |
| Celular com boa câmera | Fotos ortogonais de cada peça | já tem |
| Durômetro Shore A (opcional) | Dureza do silicone. Sem ele, comparar ao toque com amostras de dureza conhecida do fornecedor | R$ 150 a 300 |
| Chaves pequenas, alicate de bico | Desmontar | já tem ou R$ 30 |

## Etapa 1 — Desembalar e documentar antes de tocar
Tudo em `02-produto/prototipos/P00-desmontagem/`.
1. Foto da caixa fechada, aberta, de cada camada da embalagem. Anote dimensões e peso da caixa. Isso é referência para a nossa embalagem.
2. Foto de tudo que veio dentro, lado a lado, sobre a grade. Conte as peças. Preencha a lista em `levantamento-dimensional.md`.
3. Fotografe manual, cartões, QR codes. Guarde o PDF do manual se houver.
4. Pese o kit completo montado.

## Etapa 2 — Fotos ortogonais de cada peça
Para cada peça, sobre o papel milimetrado, câmera o mais perpendicular possível, a pelo menos 40 cm (reduz distorção da lente), com zoom em vez de aproximar:
- Vista de cima, de frente, de lado. Para peças redondas, cima e lado bastam.
- Uma foto com o paquímetro aberto na medida principal, para calibrar escala.
- Nomeie: `P00-copo-32mm-topo.jpg`, `P00-copo-32mm-lado.jpg`.

Essas fotos vão virar fundo de referência no CAD: você importa a imagem, ajusta a escala pela grade e desenha por cima. No FreeCAD é a ferramenta "Image plane"; no build123d você usa as medidas direto.

## Etapa 3 — Medir
Regras:
- Mede duas vezes, anota uma. Anote na tabela de `levantamento-dimensional.md`.
- Externo com os bicos externos do paquímetro, interno com os bicos internos, profundidade com a haste traseira.
- Para diâmetros, meça em dois ângulos e anote os dois; se forem diferentes, a peça é oval ou está deformada.
- Para espessura de parede de peça oca: diâmetro externo menos interno, dividido por dois.
- Para roscas: diâmetro externo da rosca, e conte quantos fios em 10 mm (passo = 10 / fios). Ou compare com parafusos conhecidos (M6, M8).
- Para molas: diâmetro do arame, diâmetro externo, número de espiras, comprimento livre, e comprimento sob carga conhecida (pendure 1 kg e meça). Isso dá a constante da mola.
- Para silicone: espessura da membrana em 3 pontos, dureza (ou impressão: "mais mole que borracha de apagar, mais duro que chiclete").

### Medidas críticas, por subsistema
**Copos de vácuo (cada tamanho):** diâmetro interno da boca, diâmetro interno do corpo, altura total, espessura de parede, diâmetro e tipo do engate com a haste, diâmetro e rosca da válvula/conexão da bomba, como a membrana se fixa (encaixe, anel, cola).
**Membrana:** diâmetro total, diâmetro do furo central, espessura, perfil (plana, abaulada, com reforço na borda).
**Bomba manual:** tipo (seringa, pera, pistão), curso, volume, válvula de alívio.
**Hastes:** comprimento mínimo e máximo, diâmetro externo do tubo, diâmetro interno, passo de rosca, comprimento das extensões, como a mola está alojada, força em cada marca da escala (medir com o dinamômetro).
**Base:** diâmetro externo e interno do anel, espessura, distância entre os furos das hastes, formato e espessura da almofada, como a almofada se fixa.
**Mangas de silicone:** diâmetro interno em repouso, comprimento, espessura, como engatam na haste.

## Etapa 4 — Desmontar e entender
Desmonte tudo que desmonta sem quebrar. Fotografe cada estágio.
- Como o copo veda com a membrana? Pressão? Anel? Cola?
- Como a mola é presa dentro da haste? Tem pistão? Qual o curso?
- Que material parece ser cada peça? Pistas: acrílico é mais frágil e risca fácil, policarbonato é mais flexível; nylon é levemente translúcido e mais "ceroso", ABS é opaco e brilhante; inox não atrai ímã (ou atrai pouco), aço cromado atrai.
- Marcas de injeção (pontos de entrada do plástico, linhas de partição do molde) mostram como foi fabricado. Fotografe.
- Anote tudo que parece mal resolvido. Isso alimenta `02-produto/melhorias-sobre-o-epic.md`.

Se precisar cortar uma peça para ver a seção interna (ex.: haste), corte. O kit comprado é para isso. Compre dois se quiser manter um inteiro para comparar.

## Etapa 5 — Modelar
Com as medidas na tabela:
1. Atualizar `02-produto/cad/parametros.py` com as medidas reais, substituindo as estimadas.
2. Rodar os scripts; eles geram STEP (para fabricante e FreeCAD) e STL (para impressão 3D).
3. Abrir no FreeCAD, comparar visualmente com as fotos.
4. Imprimir uma peça em 3D e comparar fisicamente com a original. Se encaixa onde deve encaixar, o modelo está certo.

Alternativa para formas complexas (almofada, pegadores ergonômicos): fotogrametria com o Meshroom (grátis) ou um scanner 3D de celular. Gera uma malha que serve de referência visual, não de peça final. Para este produto, quase tudo é cilindro e anel; o paquímetro basta.

## Resultado esperado
Ao final da etapa 5 temos:
- `levantamento-dimensional.md` preenchido (o blueprint em texto).
- Pasta de fotos organizada.
- Modelo 3D paramétrico que reproduz o Epic.
- Lista do que está mal resolvido no Epic.

A partir daí, cada melhoria é mudar um parâmetro ou uma peça e imprimir de novo.
