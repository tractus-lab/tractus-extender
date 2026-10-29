# Melhorias sobre o Epic Extender

O Epic é a referência. Este arquivo lista onde ele falha e o que fazemos diferente. Cada melhoria vira requisito em `requisitos.md` quando for confirmada.

## Como preencher
Para cada ideia: qual o problema no Epic, qual a nossa solução, como vamos provar que é melhor, e quanto custa a mais. Ideias sem prova viram hipótese a testar no protótipo.

## Ideias do fundador
> Registrar aqui as ideias já existentes, uma por bloco.

### M-01 — Força máxima de 5 kg, não 10
- **Problema no Epic:** escala até 10 kg (22 lb). Exagerado e, na visão do fundador, inseguro acima de 5 kg. Protocolos de tração usam 0,6 a 1,5 kg por horas; ninguém precisa de 10.
- **Nossa solução:** mola e escala dimensionadas para 5 kg no fim do curso, com batente mecânico. Mola de metade da constante (≈ 1,25 N/mm) no mesmo curso de 40 mm, o que dobra a resolução da escala.
- **Como provar que é melhor:** escala mais legível (1 kg = 8 mm em vez de 4) e teste de uso mostrando que 5 kg já é mais do que qualquer protocolo pede. Argumento de venda: "limitado por projeto".
- **Custo ou complexidade adicional:** nenhum; a mola fica mais leve (arame ~1,3 mm) e mais barata.
- **Status:** confirmada pelo fundador (2026-10-29)

### M-02 — Curso dimensionado para gente real
- **Problema no Epic:** hastes de 280 mm que acomodam 25 cm ou mais. Deixa o aparelho comprido, pesado, caro e difícil de esconder sob a roupa, para servir a um caso que não existe.
- **Nossa solução:** curso para ~20 cm esticado (valor a confirmar com dados antropométricos e entrevistas), com hastes uns 5 cm mais curtas. Se houver demanda, versão longa como variante, não como padrão.
- **Como provar que é melhor:** dados de comprimento esticado da população (percentil 95 fica bem abaixo de 20 cm); teste de discrição sob a roupa.
- **Custo ou complexidade adicional:** negativa: menos haste, menos tubo, menos embalagem.
- **Status:** confirmada pelo fundador (2026-10-29); valor exato em aberto

### M-03 — Variante longa como edição especial
- **Problema no Epic:** um tamanho só, dimensionado para o caso extremo, que encarece e alonga o aparelho de todo mundo.
- **Nossa solução:** versão padrão (~20 cm esticado) e uma edição longa, mais cara, com hastes 5 a 8 cm maiores e, se preciso, copo e mangas de boca maior do mesmo fornecedor. Mesmos moldes, mesma mola, mesmo limite de 5 kg; só muda o que é cortado no comprimento e a caixa.
- **Como provar que é melhor:** custo extra de R$ 10 a 20 por kit contra preço 30 a 50 % maior; medir quantos clientes pedem a longa antes de estocar.
- **Custo ou complexidade adicional:** segunda SKU (estoque, fotos, anúncios, dúvidas). Começar sob encomenda; só estocar com demanda comprovada.
- **Status:** ideia (fundador, 2026-10-29)

## Pontos de atenção levantados na pesquisa (a confirmar desmontando)
Observações genéricas sobre extensores de vácuo que podem ou não valer para o Epic:

- **Membrana:** nos genéricos, a membrana de silicone é o primeiro item a rasgar e é vendida em kits de reposição. Oportunidade: material e espessura melhores, troca sem ferramenta, reposição inclusa.
- **Perda de vácuo:** copos genéricos perdem vácuo em minutos e exigem bombar de novo. Oportunidade: válvula de melhor qualidade, vedação entre copo e membrana projetada com tolerância.
- **Escala de tensão:** o Epic anuncia até 10 kg, mas não está claro se a escala é precisa. Oportunidade: calibrar e dizer isso.
- **Base:** almofada que absorve suor e não lava bem é reclamação comum. Oportunidade: capa de silicone removível.
- **Articulação copo-haste:** quando é rígida, o ângulo incomoda ao sentar. Oportunidade: junta esférica.
- **Discrição ao vestir:** hastes longas marcam a roupa. Oportunidade: perfil mais baixo, ou versão com cinto (como Phallosan) para uso sob a roupa.
- **Instruções:** material em inglês, vídeos genéricos. Oportunidade: manual ilustrado em português e app próprio.

## Montagem
As simplificações de montagem (porca cega no lugar da Allen embutida, pino elástico sem tampas, porca cativa no punho, ponte e barra em chapa cortada a laser) estão em `montagem-facil.md`.

## Regra
Melhorar não é adicionar. Cada peça a mais é um ponto de falha e um custo. Prefira fazer a mesma função com menos peças e melhor material.
