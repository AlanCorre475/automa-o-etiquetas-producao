# 🏷️ Automação de etiquetas de ordens de produção

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![pdfplumber](https://img.shields.io/badge/pdfplumber-PDF-informational)
![Status](https://img.shields.io/badge/status-em%20uso%20na%20produção-brightgreen)

Script em Python que lê o PDF das ordens de produção (OP), junta várias OPs em uma única impressão e gera os arquivos CSV prontos para o software de etiquetas (MasterPrint).

> Projeto criado e usado no meu dia a dia no PCP (Planejamento e Controle de Produção).

---

## 📑 Sumário

- [Resultados](#-resultados)
- [Por que eu fiz](#-por-que-eu-fiz)
- [O problema](#-o-problema)
- [A solução](#-a-solução)
- [Como funciona](#️-como-funciona)
- [Tecnologias](#-tecnologias)
- [Como rodar](#-como-rodar)
- [Exemplo de saída](#-exemplo-de-saída)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Próximos passos](#-próximos-passos)
- [Autor](#-autor)

---

## 📊 Resultados

| Indicador | Antes | Depois |
|---|---|---|
| Tempo para imprimir as etiquetas | 30 a 50 minutos | cerca de 6 cliques |
| Consumo de etiquetas | 2 caixas por mês | 1 caixa a cada 2 ou 3 meses (**economia acima de 80%**) |
| Erros de digitação de código/OP | frequentes | redução estimada de **99%** |

## 💡 Por que eu fiz

Trabalho no PCP e percebi um gasto elevado de etiquetas, pois muitos pedidos pequenos usavam quase uma folha inteira. Antes do script, o consumo era de pelo menos 2 caixas de etiquetas por mês, com custo de R$ 285,60 por caixa. Também eram frequentes os erros de digitação de códigos e números de OP, que geravam retrabalho para localizar as ordens de novo no sistema.

## ❌ O problema

A impressão das etiquetas era feita uma OP por vez, de forma manual, e levava de 30 a 50 minutos. Também gerava desperdício: com dois pedidos de 28 etiquetas cada, eram usadas 2 folhas, quando 1 folha seria suficiente.

## ✅ A solução

O script lê o PDF com as ordens de produção, junta várias OPs e calcula as etiquetas necessárias. Depois separa por marca e gera um arquivo CSV para cada uma, pronto para importar no MasterPrint.

Para não misturar OPs na mesma linha da folha, o script completa a última linha de cada OP com etiquetas de "sobra". Assim a próxima OP sempre começa numa linha nova, fácil de destacar.

## ⚙️ Como funciona

```
PDF das OPs  ──►  lê e identifica cada OP  ──►  separa por marca  ──►  gera 1 CSV por marca  ──►  importa no MasterPrint
```

1. O script lê o PDF e encontra cada bloco que começa com **"Ordem de Produção"**.
2. De cada OP ele pega: número da OP, produto, centro de trabalho, quantidade e descrição.
3. Pula os produtos que não levam etiqueta (prefixos configurados no início do script).
4. Separa as OPs por marca (AAA, BBB e CCC).
5. Repete cada OP pela quantidade de etiquetas e completa a linha com sobras (8 etiquetas por linha).
6. Salva os CSVs na pasta `saidas/`.

## 🛠 Tecnologias

- **Python 3**
- **pdfplumber** – leitura do texto do PDF
- **re** (expressões regulares) – encontrar os campos de cada OP
- **csv** – gerar os arquivos para o MasterPrint

## ▶️ Como rodar

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Baixe o projeto:
   ```bash
   git clone https://github.com/AlanCorre475/automa-o-etiquetas-producao.git
   cd automa-o-etiquetas-producao
   ```
3. Instale a dependência:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode passando o PDF das ordens de produção:
   ```bash
   python extrair_etiquetas.py ordens.pdf
   ```
5. Os arquivos aparecem na pasta `saidas/`:
   ```
   3 ordem(ns) de producao lida(s) no total

   AAA: 1 ordem(ns) -> 16 etiqueta(s) em .../saidas/saida_aaa.csv
   BBB: 1 ordem(ns) -> 8 etiqueta(s) em .../saidas/saida_bbb.csv
   CCC: 1 ordem(ns) -> 8 etiqueta(s) em .../saidas/saida_ccc.csv
   ```
6. No MasterPrint, importe os CSVs e imprima.

## 📄 Exemplo de saída

Exemplo com **dados fictícios** (arquivo completo em [`exemplos/saida_aaa_exemplo.csv`](exemplos/saida_aaa_exemplo.csv)). Uma OP de 10 peças gera 10 etiquetas + 6 de sobra, para fechar 2 linhas de 8:

```
100001;SOF001;10;SOFA 3 LUGARES CINZA;OP 01
100001;SOF001;10;SOFA 3 LUGARES CINZA;OP 01
...
.;.;0;Sobra da OP 01 (SOF001) - a proxima OP comeca na linha de baixo;OP 01 - SOBRA
```

Colunas: `ordem ; produto ; quantidade ; descricao ; sequencia`

## 📁 Estrutura do projeto

```
automa-o-etiquetas-producao/
├── extrair_etiquetas.py   # script principal
├── requirements.txt       # dependências (pdfplumber)
├── exemplos/              # exemplo de CSV gerado (dados fictícios)
├── .gitignore             # evita subir PDFs reais e a pasta saidas/
└── README.md
```

> 🔒 Os nomes das marcas (AAA, BBB, CCC) e os prefixos de produto foram trocados por nomes genéricos para não expor dados da empresa. PDFs reais não são enviados ao repositório.

## 🚀 Próximos passos

- [ ] Ler as configurações (marcas, prefixos) de um arquivo separado, sem precisar mexer no código
- [ ] Criar um executável (.exe) para usar sem instalar o Python
- [ ] Adicionar testes automáticos com um PDF de exemplo

## 👤 Autor

**Alan Correa** – estudante de Análise e Desenvolvimento de Sistemas (Infnet) e Auxiliar de PCP.

[![GitHub](https://img.shields.io/badge/GitHub-AlanCorre475-181717?logo=github)](https://github.com/AlanCorre475)

## 📌 Observação

Ainda pode haver perda de etiquetas pela produção, mas isso ficou raro: apenas 2 casos nos últimos 3 meses. A solução trouxe ganhos tanto na redução de custos quanto na diminuição de retrabalho e no aumento da eficiência.
