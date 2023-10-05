import csv
import json


def ler(filename):
    with open(filename, encoding="utf-8") as fp:
        fpreader = csv.reader(fp, delimiter=';')
        # Despesas -> { MesRelativo: { NomeDespesa: { ValorPagar: ,DataPagamento: } } }
        despesas = {}
        row = 0
        for csvLine in fpreader:
            row += 1
            if row != 1:
                line = csvLine[0].split(';')
                MESRELATIVO, NOMEDESPESA, VALORPAGAR, DATAPAGAMENTO = 0, 1, 2, 3
                if line[MESRELATIVO] in despesas.keys():
                    if line[NOMEDESPESA] in despesas[line[MESRELATIVO]].keys():
                        despesas[line[MESRELATIVO]][line[NOMEDESPESA]].update(
                            {line[VALORPAGAR]: "Valor a pagar em €", line[DATAPAGAMENTO]: "DataPagamento"})
                    else:
                        despesas[line[MESRELATIVO]][line[NOMEDESPESA]] = {line[VALORPAGAR]: "Valor a pagar em €",
                                                                          line[DATAPAGAMENTO]: "Data Pagamento"}
                else:
                    despesas[line[MESRELATIVO]] = {
                        line[NOMEDESPESA]: {line[VALORPAGAR]: "Valor a pagar em €",
                                            line[DATAPAGAMENTO]: "Data Pagamento"}}
    return despesas

