# Automação de etiquetas de ordens de produção

Script em Python que automatiza a geração de etiquetas de ordens de produção (OP).

## Por que eu fiz

Trabalho no PCP e percebi um gasto grande de etiquetas: pelo menos 2 caixas por mês (R$ 285,60 cada), porque pedidos pequenos usavam quase uma folha inteira. Além disso, a digitação manual gerava erros de código e de OP, o que causava retrabalho, pois era preciso procurar a OP de novo no sistema.

Com o script, os erros de digitação praticamente deixaram de existir (cerca de 99%). Ainda pode acontecer da produção perder etiquetas, mas isso foi raro: só 2 vezes nos últimos 3 meses.

## O problema

A impressão das etiquetas era feita uma OP por vez, de forma manual, e levava de 30 a 50 minutos. Também gerava desperdício: com dois pedidos de 28 etiquetas cada, eram usadas 2 folhas, quando 1 folha seria suficiente.

## A solução

O script lê o PDF com as ordens de produção, junta várias OPs e calcula as etiquetas necessárias. Depois separa por marca e gera um arquivo CSV para cada uma, pronto para importar no software de impressão de etiquetas (MasterPrint).

**Resultado:** o processo que levava de 30 a 50 minutos agora é concluído em cerca de 6 cliques, com menos desperdício de etiqueta.

## Como funciona

1. O PDF das ordens de produção é colocado na pasta do script.
2. O script lê o PDF e identifica as OPs.
3. As etiquetas são calculadas e separadas por marca.
4. Os CSVs são gerados na pasta `saidas`.
5. No MasterPrint, os CSVs são importados

## Extra
Trabalho no PCP e percebi um gasto grande de etiquetas: eram usadas de 2 a 3 caixas a cada 2 meses, porque pedidos pequenos usavam quase uma folha inteira. Além disso, a digitação manual gerava erros de código e de OP, o que causava retrabalho, pois era preciso procurar a OP de novo no sistema.

Com o script, o consumo caiu para cerca de 1 caixa a cada 2-3 meses (mais da metade de redução) e os erros de digitação praticamente deixaram de existir (cerca de 99%). Ainda pode acontecer da produção perder etiquetas, mas isso foi raro: só 2 vezes nos últimos 3 meses.
