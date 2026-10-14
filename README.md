## automacao-etiquetas-producao
Script em Python que automatiza a geração de etiquetas de ordens de produção

## Automação de etiquetas de ordens de produção

Script em Python que automatiza a geração de etiquetas de ordens de produção (OP).

## O problema

A impressão das etiquetas era feita uma OP por vez, de forma manual, levando de 30 a 50 minutos e gerava desperdício de etiquetas, já que por exemplo, se tinha dois pedido, 28 cada um, seria usada 2 folha ao invés de 1, tirando o desperdício total de 56 etiquetas. Além disso tinha o erro de código e ou OP, fazendo um retrabalho gigante pois tinha que procura a OP de novo no sistema. 

## A solução
O script lê o PDF com as ordens de produção, junta várias OPs e calcula as etiquetas necessárias. Depois separa por marca e gera um arquivo CSV para cada uma, prontos para importar no software de impressão de etiquetas (MasterPrint).

Resultado: o processo que levava de 30 a 50 minutos agora é concluído em cerca de 6 cliques, com menos desperdício de etiqueta.

## Como funciona

1. O PDF das ordens de produção é colocado na pasta do script.
2. O script lê o PDF e identifica as OPs.
3. As etiquetas são calculadas e separadas por marca.
4. Os CSVs são gerados na pasta "saidas".
5. No MasterPrint, os CSVs são importados no template de cada marca.

## Programas utilizados

- Python
- CSV
- MasterPrint


## Observação

Projeto criado para uso interno. Os códigos e nomes de marcas do script são exemplos fictícios, e nenhum dado real foi incluído
