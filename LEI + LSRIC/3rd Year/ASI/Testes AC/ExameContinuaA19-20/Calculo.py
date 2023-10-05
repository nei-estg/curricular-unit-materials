import json

import LerFicheiro
import re


def DespesasMes(dicionario):
    # DespesasMes -> { Mes: total }
    # Despesas -> { MesRelativo: { NomeDespesa: { ValorPagar: ,DataPagamento: } } }
    despesasMes = {}
    datepattern = re.compile(
        r'(0[0-9]|1[0-9]|2[0-9]|3|[0-9])\/([0-1]|[3-9]|1[0-2])\/([1-2][0|9][0|1|7|8|9][0-9])|([0-9]|1[0-9]|2[0-8])\/([2])\/([1-2][0|9][0|1|7|8|9][0-9])')
    #pricepattern=re.compile(r'^\d*.\d*$')
    for mes in dicionario.keys():
        for despesa in dicionario[mes].keys():
            for preco in dicionario[mes][despesa].keys():
                if not datepattern.match(preco) and preco != "":
                    if mes in despesasMes.keys():
                        despesasMes[mes] += float(preco)
                    else:
                        despesasMes[mes] = float(preco)
    return despesasMes


#DespesasMes(LerFicheiro.ler('despesas2019.csv'))


def DespesasTipo(dicionario):
    # DespesasTipo -> { TipoDespesa: total }
    despesasMes = {}
    datepattern = re.compile(
        r'(0[0-9]|1[0-9]|2[0-9]|3|[0-9])\/([0-1]|[3-9]|1[0-2])\/([1-2][0|9][0|1|7|8|9][0-9])|([0-9]|1[0-9]|2[0-8])\/([2])\/([1-2][0|9][0|1|7|8|9][0-9])')
    for mes in dicionario.keys():
        for despesa in dicionario[mes].keys():
            for preco in dicionario[mes][despesa].keys():
                if not datepattern.match(preco) and preco != "":
                    if despesa in despesasMes.keys():
                        despesasMes[despesa] += float(preco)
                    else:
                        despesasMes[despesa] = float(preco)
    return despesasMes


# print(json.dumps(DespesasTipo(LerFicheiro.ler('despesas2019.csv')), ensure_ascii=False, indent=2))


def DespesasPagar(dicionario):
    despesasList = []
    for mes in dicionario.keys():
        for despesa in dicionario[mes].keys():
            for preco in dicionario[mes][despesa].keys():
                if preco == "":
                    if despesa not in despesasList:
                        despesasList.append(despesa)
    return despesasList

# DespesasPagar(LerFicheiro.ler('despesas2019.csv'))
