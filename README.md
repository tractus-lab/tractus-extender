# Projeto: extensor de tração (nome provisório)

Repositório de trabalho para o desenvolvimento de um extensor peniano de tração com fixação a vácuo, de qualidade equivalente aos importados premium (Epic Extender, Penimaster), vendido no Brasil por cerca de R$ 500, e para a criação da empresa que vai fabricá-lo e vendê-lo. Produto futuro: bomba a vácuo com cilindros de acrílico (referência: LA Pump).

## Como navegar

As pastas seguem a ordem natural do projeto. Nada impede trabalhar em paralelo, mas cada etapa alimenta a seguinte.

| Pasta | O que guarda | Pergunta que responde |
|---|---|---|
| `00-ideia/` | A ideia, o problema e o público | O que estamos fazendo e para quem? |
| `01-pesquisa/` | Mercado, concorrentes, entrevistas, normas | Vale a pena? O que já existe? O que a lei exige? |
| `02-produto/` | Requisitos, especificação, design, engenharia, protótipos | Como o produto é e como funciona? |
| `03-negocio/` | Modelo de negócio, custos, preço, plano | Como isso dá dinheiro? |
| `04-empresa/` | Abertura da empresa, marca, impostos | Como formalizar no Brasil? |
| `05-fabricacao/` | Fornecedores, produção, logística | Quem fabrica e como chega ao cliente? |
| `06-lancamento/` | Marketing, canais de venda, lançamento | Como as pessoas vão conhecer e comprar? |
| `decisoes/` | Registro de decisões importantes | Por que escolhemos isso e não aquilo? |

## Arquivos na raiz

- `roadmap.md` — fases do projeto, marcos e o que está em andamento.
- `glossario.md` — termos técnicos e siglas usadas no projeto.

## Convenções

- Idioma: português do Brasil.
- Datas no formato AAAA-MM-DD.
- Toda decisão relevante vira um arquivo em `decisoes/` (copie `decisoes/000-modelo.md`).
- Arquivos binários (CAD, imagens, planilhas) ficam na subpasta do tema. Documentos de texto em Markdown.

## Estado atual

- **Fase:** P00 em andamento (Epic Extender em mãos, fotografado, CAD v0.2 pela foto)
- **Última atualização:** 2026-10-27
- **Próximos passos:** (1) fotografar o resto do kit e medir com paquímetro, preenchendo `02-produto/engenharia/mecanica/levantamento-dimensional.md`; (2) trocar valores FOTO por MED em `02-produto/cad/parametros.py`; (3) confirmar o mecanismo da mola; (4) busca de patentes no INPI; (5) preços no Mercado Livre e Shopee.
