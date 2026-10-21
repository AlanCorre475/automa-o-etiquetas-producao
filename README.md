##Automação de etiquetas de ordens de produção
Script em Python que automatiza a geração de etiquetas de ordens de produção (OP).

##Por que eu fiz
Trabalho no PCP e percebi um gasto grande de etiquetas: pelo menos 2 caixas por mês (R$ 285,60 cada), porque pedidos pequenos usavam quase uma folha inteira. Além disso, a digitação manual gerava erros de código e de OP, o que causava retrabalho, pois era preciso procurar a OP de novo no sistema.

Com o script, os erros de digitação praticamente deixaram de existir (cerca de 99%). Ainda pode acontecer da produção perder etiquetas, mas isso foi raro: só 2 vezes nos últimos 3 meses.

##O problema
A impressão das etiquetas era feita uma OP por vez, de forma manual, e levava de 30 a 50 minutos. Também gerava desperdício: com dois pedidos de 28 etiquetas cada, eram usadas 2 folhas, quando 1 folha seria suficiente.

##A solução
O script lê o PDF com as ordens de produção, junta várias OPs e calcula as etiquetas necessárias. Depois separa por marca e gera um arquivo CSV para cada uma, pronto para importar no software de impressão de etiquetas (MasterPrint).

Resultado: o processo que levava de 30 a 50 minutos agora é concluído em cerca de 6 cliques, com menos desperdício de etiqueta.

##Como funciona
O PDF das ordens de produção é colocado na pasta do script.
O script lê o PDF e identifica as OPs.
As etiquetas são calculadas e separadas por marca.
Os CSVs são gerados na pasta saidas.
No MasterPrint, os CSVs são importados no template de cada marca.
##Como rodar
Instale o Python (3.8 ou mais novo)
Instale a biblioteca: pip install pdfplumber
Coloque o PDF das ordens de produção na pasta do script
Rode: python extrair_etiquetas.py entrada.pdf
Os arquivos CSV vão aparecer na pasta saidas
##Exemplo de saída
Trecho de um CSV gerado (dados fictícios). Cada OP vira várias etiquetas, e as sobras completam a linha de 8 etiquetas:

100001;PROD-A;28;Cadeira exemplo A;OP 01
100001;PROD-A;28;Cadeira exemplo A;OP 01
...
.;.;0;Sobra da OP 01 (PROD-A) - a proxima OP comeca na linha de baixo;OP 01 - SOBRA
O que eu aprendi
A maior lição que levo para a vida é entender o processo antes de qualquer coisa, com cada nuance, para executar da melhor maneira. Também aprendi que o que eu achava certo mudou várias vezes no caminho, e que isso exige paciência. Por fim, aprendi a importância da comunicação: tratei a produção como meu "cliente" e ajustei a solução para ficar boa para os dois lados.

Programas utilizados
Python
CSV
MasterPrint
Observação
Projeto criado para uso interno. Os códigos e nomes de marcas do script são exemplos fictícios, e nenhum dado real foi incluído.
