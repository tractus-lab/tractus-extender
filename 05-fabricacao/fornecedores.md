# Fornecedores

## Estratégia
- **Fabricar internamente:** controle total, investimento alto, escala lenta.
- **Terceirizar montagem:** você projeta, uma fábrica monta. Comum para eletrônicos (EMS) e injeção plástica.
- **Importar pronto e marcar:** rápido, pouca diferenciação, risco de dependência.
- **Híbrido:** peças terceirizadas, montagem final interna.

Decisão em `decisoes/`.

## Onde procurar no Brasil
- Polos industriais: Santa Rita do Sapucaí (eletrônica), Joinville (metal-mecânica e plástico), Caxias do Sul (metal-mecânica), Manaus (eletrônicos com incentivo), Franca e Novo Hamburgo (couro e calçados), São Paulo e região (de tudo).
- Associações setoriais e feiras (Feiplastic, FIEE, Mecânica).
- Plataformas B2B e indicações de outros empreendedores.

## Quem pode fazer cada peça no Brasil (levantamento 2026-10-29)

Resposta curta: tudo que é estrutura (plástico injetado, borracha, chapa, usinado, mola, haste, tubo) tem fábrica no
Brasil, e várias. O que **não** tem fabricante nacional especializado é o conjunto de vácuo (copo com válvula, bomba
manual e mangas): dá para fazer aqui com injeção transparente + moldagem de silicone + válvula comprada, mas ninguém
faz isso pronto, e o custo da ferramenta é alto para o volume inicial. Os nomes abaixo vieram de busca na web, sem
contato e sem cotação; servem como ponto de partida, não como recomendação.

| Peça (BOM) | Processo | Tipo de fábrica | Onde há muitas | Exemplos achados | Observação |
|---|---|---|---|---|---|
| 11 Ferradura (plástico), 13 punhos | injeção de termoplástico (PA6/ABS) | "injetora" de peças técnicas + ferramentaria para o molde | Joinville/SC, Caxias do Sul/RS, ABC paulista, Vale do Paraíba | MASA Molds & Plastics, Würch Matrizes & Plásticos (desde 1981), Voktep (terceirização de injeção), CDR Plastic (SP) | Molde de aço nacional R$ 20 a 50 mil por peça; para lotes de centenas, molde em alumínio ou com insertos impressos em 3D (estudos UFU/UFSC/UFMG) |
| 11/13 em baixo volume | impressão 3D industrial (MJF/SLS em PA12) | bureau de impressão 3D | São Paulo, Curitiba, Porto Alegre | SKA é a revendedora HP no Brasil (seus clientes são os bureaus); nenhum bureau confirmado na busca | Pedir cotação por volume (cm³) a 2 ou 3 bureaus; alternativa é JLC3DP/China com importação |
| 12 Face de borracha da ferradura, 8 mangas de silicone | moldagem de silicone (LSR injetado ou HTV por compressão) | fábrica de artefatos de silicone | Jundiaí, São Paulo, Joinville | Silikonbrasil (Jundiaí, LSR, projeta o molde), Pro Rubber (SP, peças sob desenho, ventosas) | Pedir silicone platina com laudo de contato com pele (ISO 10993-5/-10 ou grau alimentício) |
| 7 Copo de vácuo | injeção de PC ou PETG transparente | injetora que trabalha com transparentes (óptica, embalagem cosmética, eletrodoméstico) | SP, SC | nenhum achado específico | Molde polido (espelhado) é mais caro; protótipo pode ser torneado em tarugo de acrílico |
| 7 Válvula de retenção/alívio, 9 bomba | — | não há fabricante nacional de bomba peniana; as "nacionais" são de ABS + silicone de origem importada | — | só a seringa de reposição "Pérola" aparece como nacional | Importar da China (mesma fábrica dos genéricos) ou projetar válvula própria com O-ring e mola |
| 4 Molas | conformação de arame | fábrica de molas | ABC paulista, Caxias, Joinville | Darvig Molas (Santo André, desde 1984, sob medida), Isomol (inox, arame a partir de 0,15 mm), Líder Molas (S. B. do Campo) | Pequena quantidade sob desenho: R$ 15 a 30 cada; 2.000 un.: R$ 2 a 4 |
| 1 Hastes roscadas, 2/3 porcas, 5 pinos | fixadores | fabricante ou distribuidor de fixadores | Joinville, Indaial/SC, SP | Ciser (Joinville), Metalúrgica Fey (Indaial), distribuidores de inox em qualquer capital | Barra roscada M6 inox 304 é item de prateleira; só cortar e chanfrar |
| 14 Tambor do pivô | torno CNC | tornearia de precisão | SP, Indaiatuba, Joinville, Caxias | Rio da Prata (SP, peças por amostra ou desenho), Speed-Tec (Indaiatuba, tornos automáticos ROMI) | Em lote de 2.000, R$ 8 a 15 cada |
| 15 Ponte, 16 barra superior | corte a laser + dobra em alumínio | serralheria com laser de fibra | Mogi das Cruzes, Curitiba, SP, SC | SBM Laser Corte e Dobra (Mogi, até 9,5 mm inox), Engecorte (Curitiba, laser + dobra) | Mandar DXF; peça de 4 mm em 6063/5052 sai barata, anodizar à parte |
| 6 Tubo da escala | corte de tubo + anodização + gravação a laser | serralheria + anodizador + gravadora | SP, Caxias | anodizadores em toda região industrial (pedir "anodização preta tipo II") | Tubo 16 × 1 mm 6063 é extrusão padrão (Hydro, Alcoa e revendas) |
| 10 Embalagem | gráfica / cartonagem | gráfica | qualquer capital | — | — |

### O que isso muda no plano

- **Rota nacional é viável para a estrutura inteira.** Nenhuma peça estrutural depende da China. O gargalo é o custo
  do molde da ferradura e dos punhos, não a existência de fábrica.
- **O conjunto de vácuo decide.** Fazer copo + válvula + bomba + mangas no Brasil exige 3 moldes (copo transparente,
  mangas, face de borracha) e uma válvula projetada; só compensa acima de alguns milhares de kits. Até lá, importar
  o conjunto da mesma fábrica que abastece os genéricos (decisão 002, híbrido).
- **Próximo passo prático:** mandar o STEP/DXF do CAD para 2 injetoras, 1 fábrica de silicone, 1 de molas e 1 de corte
  a laser e pedir cotação para 50, 500 e 2.000 unidades. Preencher a tabela abaixo com as respostas.

## Lista de fornecedores
| Componente / serviço | Fornecedor | Cidade | Contato | Preço cotado | Prazo | Lote mínimo | Avaliação | Status |
|---|---|---|---|---|---|---|---|---|

## Critérios de avaliação
Preço, qualidade, prazo, lote mínimo, comunicação, capacidade de crescer com você, certificações (ISO 9001), disposição para fazer protótipo.

## Importação de componentes
Se algum componente vem de fora: fornecedor, NCM, custo com impostos e frete, prazo, risco cambial.

## Contratos
Sempre com NDA. Para moldes: quem é dono do molde? Deixe por escrito.
