import csv, json


def ler(filename):
    with open(filename) as fp:
        NUMSOCIO, MODALIDADE, VALORPAGAR, DATAPAGAMENTO = 0, 1, 2, 3
        # Modalidade -> { Modalidade: { NSocio: [(ValorPagar,DataPagamento ), (), ...] }}
        modalidade = {}
        fpreader = csv.reader(fp, delimiter=';')
        row = 0
        for line in fpreader:
            row += 1
            if row != 1:
                line = line[0].split(';')
                if line[MODALIDADE] in modalidade.keys():
                    if line[NUMSOCIO] in modalidade[line[MODALIDADE]].keys():
                        modalidade[line[MODALIDADE]][line[NUMSOCIO]].append((line[VALORPAGAR], line[DATAPAGAMENTO]))
                    else:
                        modalidade[line[MODALIDADE]][line[NUMSOCIO]] = [(line[VALORPAGAR], line[DATAPAGAMENTO])]
                else:
                    modalidade[line[MODALIDADE]] = {line[NUMSOCIO]: [(line[VALORPAGAR], line[DATAPAGAMENTO])]}
    return modalidade
