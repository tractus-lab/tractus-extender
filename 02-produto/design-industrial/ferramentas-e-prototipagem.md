# Ferramentas de CAD e caminho de prototipagem

Para quem é de computação e nunca fez produto físico. Atualizado em 2026-10-25.

## Software de CAD: qual usar

Para este produto (peças pequenas, geometria simples: anéis, tubos, copos, diafragmas) qualquer CAD paramétrico serve. A escolha é sobre custo de licença para uso comercial e curva de aprendizado.

| Opção | Custo | Prós | Contras | Recomendação |
|---|---|---|---|---|
| **FreeCAD 1.x** | Grátis, código aberto | Sem restrição comercial; comunidade grande; roda em Linux | Interface menos polida; curva inicial de 1–2 semanas | **Principal.** Sem risco de licença quando a empresa crescer. |
| **Onshape (plano Free)** | Grátis | Roda no navegador; muito bom de usar; colaboração | Documentos no plano gratuito são públicos. Plano comercial ~US$ 1.500/ano. | Bom para aprender; não para desenhos que queremos manter em sigilo. |
| **Fusion 360 (Personal)** | Grátis para uso pessoal | Excelente; muito tutorial no YouTube | Licença pessoal **proíbe uso comercial**. Comercial ~US$ 680/ano. | Só se aceitar pagar depois. |
| **OpenSCAD / CadQuery / build123d** | Grátis | CAD por código (Python no CadQuery e build123d). Natural para programador; parametrização trivial; versionável no git | Difícil para formas orgânicas e ergonômicas; sem desenho técnico 2D fácil | **Complemento forte.** Ideal para os copos (variar diâmetro é mudar um número) e para gerar as 5 variações automaticamente. |
| SolidWorks, Inventor, Rhino | Milhares de reais/ano | Padrão da indústria; o fabricante vai usar | Caro para começar | Não agora. Qualquer um exporta STEP, que o fabricante lê. |

**Plano sugerido:** build123d (Python) para as peças paramétricas (copos, mangas, moldes) e FreeCAD para montagem, visualização e desenhos 2D com cotas para enviar a fornecedores. Formato de troca: **STEP**. Formato para impressão 3D: **STL ou 3MF**.

## Como aprender (ordem)
1. 2 a 3 dias: tutorial básico de FreeCAD (sketch → pad/pocket → fillet). Fazer um anel e um tubo.
2. 1 dia: build123d, reproduzir o anel por código.
3. Modelar o copo de vácuo em um diâmetro. Imprimir em 3D. Testar vedação com uma membrana cortada de luva de silicone ou balão.
4. Iterar.

## Impressão 3D: a ferramenta de prototipagem

| Tecnologia | Para quê aqui | Custo da máquina (Brasil, 2026, aprox.) |
|---|---|---|
| FDM (filamento) | Base, suportes, moldes para silicone, gabaritos | R$ 1.500 a 3.500 (Bambu Lab A1, Creality K1, Elegoo Neptune) |
| Resina (SLA/MSLA) | Copos transparentes, peças com acabamento liso | R$ 1.200 a 3.000 (Elegoo Mars/Saturn, Anycubic Photon) + resina transparente + lavagem/cura |

Alternativa sem comprar máquina: serviços de impressão sob demanda no Brasil (buscar "impressão 3D sob demanda" na sua cidade, ou plataformas como 3D Hubs/Craftcloud internacionais). Para um projeto que vai iterar muito, comprar uma FDM barata se paga em um mês.

## Silicone: protótipo em casa
- Imprimir molde em 3D (duas partes, com canal de entrada e saída de ar).
- Silicone de cura por platina (RTV-2). Fornecedores nacionais: Redelease, Siquiplás, Silaex, Ecopox. Dureza 10–30 Shore A para mangas e membranas.
- Vácuo ou vibração para tirar bolhas (câmara de vácuo de cozinha serve no começo).
- Para produção: moldagem por compressão em ferramentaria de borracha, ou injeção de LSR (silicone líquido) na China.

## Peças metálicas: protótipo
- Tubo de inox 304 e molas: lojas de materiais industriais (Mercado Livre tem). Molas sob medida: fabricantes de molas em SP (buscar "molas sob medida").
- Usinagem pequena: tornearia de bairro faz peças simples por preço baixo. Para séries, "usinagem CNC sob demanda" com upload de STEP.

## Acrílico/policarbonato (copos e, futuramente, cilindros da bomba)
- Protótipo: resina 3D transparente, polida com lixa fina e verniz; ou usinar tarugo de acrílico em tornearia.
- Produção: tubo de acrílico extrudado cortado e polido (é exatamente como a LA Pump faz os cilindros) para a bomba; injeção de PC ou PMMA para os copos, molde de aço ~R$ 15 a 40 mil por cavidade no Brasil, menos na China.

## Caminho completo até o primeiro protótipo funcional
1. Comprar 1 Epic Extender (ou Penimaster) + 1 genérico chinês com copo de vácuo. Desmontar, medir, fotografar, pesar. Documentar em `02-produto/prototipos/P00-desmontagem/`.
2. Modelar cada peça em CAD a partir das medidas, ajustando o que achamos ruim.
3. Imprimir base e copos. Moldar membranas e mangas. Comprar hastes/molas prontas.
4. Montar P01 (funcional, feio). Testar vedação, tensão, conforto.
5. Iterar até P03. Só então pensar em ferramental.

Custo estimado da fase de protótipo: R$ 4.000 a 8.000 (produtos de referência, impressora, materiais, usinagem).
