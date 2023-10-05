
def totais(vendas):
    # TOTVENDAS -> {ISBN : total}
    # VENDAS -> {ISBN : {data: [Titulo, Editora, Preco, Desconto]}}
    totvendas={}
    for serial in vendas.keys():
        for data in vendas[serial].keys():
            if serial in totvendas.keys():
                totvendas[serial] += float(vendas[serial][data][2].strip('â‚¬'))
            else:
                totvendas[serial]=float(vendas[serial][data][2].strip('â‚¬'))
    return totvendas


