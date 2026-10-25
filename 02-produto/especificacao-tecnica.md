# Especificação técnica

Versão 0.1 — 2026-10-25. Baseada na análise do Epic Extender e similares pela web. **Comprar uma unidade do Epic e uma de um genérico chinês e desmontar antes de fechar qualquer dimensão.**

## Arquitetura do produto

```
 [Copo de vácuo]----[Conector]----[Haste esq.]----+
       |                                          |--[Base / anel acolchoado]
 [Bomba manual]                 [Haste dir.]------+
       |
 [Membrana de silicone]        [Alternativa: manga de silicone no lugar do copo]
```

Cinco subsistemas:

| # | Subsistema | Função | Peças |
|---|---|---|---|
| 1 | Base | Apoia no púbis, ancora as hastes | Anel rígido (plástico de engenharia) + almofada (espuma com capa de silicone ou tecido) |
| 2 | Hastes de tração | Geram e permitem ajustar a força | 2 hastes telescópicas com mola interna calibrada, ou hastes rosqueadas com extensões; escala de medida |
| 3 | Fixação a vácuo | Segura a glande sem apertar | Copo transparente (PMMA ou PC) em 4–5 diâmetros (28 a 44 mm), membrana de silicone, válvula, bomba manual pequena |
| 4 | Fixação alternativa | Para quem prefere ou não se adapta ao vácuo | Mangas de silicone em 3 tamanhos (21, 26, 32 mm), fita coesiva |
| 5 | Embalagem e documentação | Discrição, instrução, confiança | Estojo rígido, manual em português, cartão de garantia, QR para vídeos e app |

## Mecânica

### Base
- Material: nylon PA6 ou ABS (injeção) para produção; impressão 3D (PETG/nylon) para protótipo.
- Furação para hastes com inserto metálico roscado.
- Almofada removível e lavável.

### Hastes
- **Decisão pendente:** mola interna (tensão constante, mais confortável, é o que os premium usam) ou rosca (mais simples, mais barata, é o que os genéricos usam). Hipótese: mola com escala em kg ou lb, como diferencial.
- Material: tubo de aço inox 304, 8 a 10 mm de diâmetro externo. Molas de aço inox ou aço mola com acabamento.
- Faixa de tensão alvo: 0,5 a 5 kg por haste (total 1 a 10 kg), legível em escala gravada.
- Comprimento ajustável com extensões: cobrir de ~8 a ~25 cm.

### Copo de vácuo
- Corpo: acrílico (PMMA) ou policarbonato (PC) transparente. Protótipo em resina transparente 3D. Produção: injeção ou usinagem.
- Membrana: silicone platinum 20–30 Shore A, espessura ~1 mm, formato de diafragma com furo central.
- Bomba: pistão manual tipo seringa ou bomba de borracha pequena com válvula de alívio. Pode ser comprada pronta.
- Tamanhos: 28, 32, 36, 40, 44 mm (confirmar após medir o Epic).
- Conexão com as hastes: engate rápido ou articulação esférica (permite ângulo).

### Mangas de silicone
- Silicone platinum 10–20 Shore A. Produção: moldagem por compressão ou injeção de LSR. Protótipo: molde impresso em 3D + silicone de cura por platina de fornecedor nacional.

## Elétrica / eletrônica
Nenhuma na versão 1. Ideia futura: célula de carga Bluetooth para medir tensão no app. (Exigiria ANATEL.)

## Software
- App web ou PWA de acompanhamento: registro de sessões, tempo, tensão, medidas, lembretes. Diferencial fácil para nós, caro para concorrente.
- Nenhum software no dispositivo.

## Interfaces com o usuário
- Escala de tensão visível nas hastes.
- Marcas de tamanho gravadas nos copos e mangas.
- Manual ilustrado + vídeos curtos.

## Embalagem
- Estojo rígido com espuma recortada (EVA) ou caixa de papelão rígida com berço.
- Externa: caixa de envio neutra, sem identificação do conteúdo.
- Obrigatórias: razão social, CNPJ, composição, advertências, lote.

## Acessórios e consumíveis
- Reposição: membranas (desgastam), mangas, almofada da base, fita coesiva. Receita recorrente.

## Tolerâncias e qualidade
- Copo: sem rebarba, vedação testada com vácuo por 60 s.
- Mola: tensão medida com dinamômetro em 3 pontos da escala; tolerância ±10%.
- Silicone: sem bolhas, sem rebarba na face de contato.
- Teste de montagem completa em 100% das unidades no início; amostragem depois.

## Perguntas em aberto
1. Mola ou rosca? (decisão 001)
2. Produzir no Brasil, na China ou híbrido? (decisão 002)
3. Dimensões reais do Epic Extender (desmontar).
4. Qual bomba manual pronta serve? (buscar no mercado de bombas de vácuo para alimentos / laboratório / cosmética)
