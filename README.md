# Automação de etiquetas de ordens de produção

Script em Python que automatiza a geração de etiquetas de ordens de produção (OP).

## Por que eu fiz

Trabalho no PCP e percebi um gasto elevado de etiquetas, pois muitos pedidos pequenos utilizavam quase uma folha inteira. Antes da implantação do script, o consumo era de pelo menos 2 caixas de etiquetas por mês, com custo de R$ 285,60 por caixa, além da ocorrência frequente de erros de digitação de códigos e números de OP, que geravam retrabalho devido à necessidade de localizar novamente as ordens no sistema.

Com a implementação do script, houve uma redução significativa no consumo de etiquetas, que passou para aproximadamente 1 caixa a cada 2 ou 3 meses, representando uma economia superior a 80%. Além disso, os erros de digitação foram praticamente eliminados, com uma redução estimada em 99%, aumentando a confiabilidade e a agilidade do processo.

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
Ainda existe a possibilidade de perda de etiquetas pela produção, porém esse tipo de ocorrência tornou-se raro, sendo registrados apenas 2 casos nos últimos 3 meses. Dessa forma, a solução trouxe ganhos expressivos tanto na redução de custos quanto na diminuição de retrabalho e aumento da eficiência operacional
