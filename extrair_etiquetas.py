import csv
import os
import re
import sys

import pdfplumber

PREFIXOS_IGNORADOS = ("TSEC","TSHI","TSIM",)

def extrair_dados_pdf(caminho_pdf):

    texto_completo = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text() or ""
            texto_completo += texto_pagina + "\n"

    blocos = texto_completo.split("Ordem de Produção")[1:]

    linha_valores = re.compile(
        r"(\d{6,})\s+(\S+)\s+([\d.,]+)\s+\d{2}/\d{2}/\d{4}\s+\d{2}/\d{2}/\d{4}")
    registros = []
    ignorados = 0
    for bloco in blocos:
        valores_match = linha_valores.search(bloco)
        produto_match = re.search(r"Produto:\s*(\S+)", bloco)
        desc_match = re.search(r"Produto:\s*\S+\s*-\s*(.+)", bloco)

        if valores_match and produto_match:
            if produto_match.group(1).upper().startswith(PREFIXOS_IGNORADOS):
                ignorados += 1
                continue    
            qtd_float = float(valores_match.group(3).replace(",", "."))
            registros.append({
                    "ordem": valores_match.group(1),
                    "produto": produto_match.group(1),
                    "ctrab": valores_match.group(2),
                    "quantidade": int(round(qtd_float)),
                    "descricao": desc_match.group(1).strip() if desc_match else ""})
        else:
            print("[AVISO] bloco ignorado (nao achei todos os campos):")
            print(bloco[:200])
    if ignorados:
        print(f"[INFO] {ignorados} OP(s) sem etiqueta puladas ({', '.join(PREFIXOS_IGNORADOS)})")
    return registros


CTRAB_RLINE = "RLINE"
CTRAB_SEPARA_RIC = "710102"  

def separar_por_marca(registros):
    rhodes = []
    ricco = []
    rline = []
    for r in registros:
        ctrab = r["ctrab"].strip().upper()
        if ctrab == CTRAB_RLINE:
            rline.append(r)
        elif ctrab == CTRAB_SEPARA_RIC and r["produto"].upper().startswith("RIC"):
            ricco.append(r)
        else:
            rhodes.append(r)
    return rhodes, ricco, rline

ETIQUETAS_POR_LINHA = 8 

def expandir_por_quantidade(registros):
    
    expandido = []
    for numero_op, r in enumerate(registros, start=1):
        rotulo_op = f"OP {numero_op:02d}"

        qtd = max(1, r["quantidade"])
        for _ in range(qtd):
            etiqueta = dict(r)
            etiqueta["sequencia"] = rotulo_op 
            expandido.append(etiqueta)
        resto = (-qtd) % ETIQUETAS_POR_LINHA  
        for i in range(resto):
            expandido.append(
                {   "ordem": ".",
                    "produto": ".",
                    "quantidade": 0,
                    "descricao": (
                        f"Sobra da {rotulo_op} ({r['produto']}) - "
                        f"a proxima OP comeca na linha de baixo"),
                    "sequencia": f"{rotulo_op} - SOBRA"})
    return expandido

def salvar_csv(registros, caminho_saida):
    
    with open(caminho_saida, "w", newline="", encoding="cp1252", errors="replace") as f:
        writer = csv.DictWriter(f,
            fieldnames=["ordem", "produto", "quantidade", "descricao", "sequencia"],
            delimiter=";",
            extrasaction="ignore")
        writer.writerows(registros)  

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python extrair_etiquetas.py entrada.pdf")
        sys.exit(1)

    caminho_pdf = sys.argv[1]

    dados = extrair_dados_pdf(caminho_pdf)
    rhodes, ricco, rline = separar_por_marca(dados)

    pasta_saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saidas")
    os.makedirs(pasta_saida, exist_ok = True)
    saidas = [("RHODES", rhodes, os.path.join(pasta_saida, "saida_rhodes.csv")),
        ("RICCO ", ricco, os.path.join(pasta_saida, "saida_ricco.csv")),
        ("RLINE ", rline, os.path.join(pasta_saida, "saida_rline.csv"))]

    print(f"\n{len(dados)} ordem(ns) de producao lida(s) no total\n")
    for nome, grupo, arquivo in saidas:
        expandido = expandir_por_quantidade(grupo)
        salvar_csv(expandido, arquivo)
        print(f"{nome}: {len(grupo)} ordem(ns) -> {len(expandido)} etiqueta(s) em {arquivo}")
