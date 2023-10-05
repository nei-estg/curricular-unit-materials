import json

def ler(file):
    with open(file) as fp:
        # VENDAS -> {ISBN : {data: [Titulo, Editora, Preco, Desconto]}}
        ISBN, TITULO, EDITORA, PRECO, DESCONTO, DATA = 0,1,2,3,4,5
        vendas = {}
        for line in fp:
            line=line.strip().split(';')
            if line[ISBN] in vendas.keys():
                if line[DATA] not in vendas[line[ISBN]].keys():
                    vendas[line[ISBN]].update({line[DATA]: [line[TITULO], line[EDITORA], line[PRECO], line[DESCONTO]]})
                else:
                    vendas[line[ISBN]][line[DATA]].append([line[TITULO],line[EDITORA],line[PRECO],line[DESCONTO]])
            else:
                vendas[line[ISBN]] = {line[DATA]: [line[TITULO], line[EDITORA], line[PRECO], line[DESCONTO]]}
    return vendas