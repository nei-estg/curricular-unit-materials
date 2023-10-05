
def totais(cartao):
    # CARTAO -> {numCli: {mes:[gasto, acumulado]}}
    # TOTAL -> {numCli: [totgasto, totacumulado]}
    total={}
    for num in cartao.keys():
        totgasto=0
        totacum=0
        for mes in cartao[num].keys():
            totgasto+=int(cartao[num][mes][0])
            totacum+=int(cartao[num][mes][1])
        total[num]=["Valor gasto: "+str(totgasto),"Valor acumulado: "+str(totacum)]
    return total

def topCliente(cartao):
    # CARTAO -> {numCli: {mes:[gasto, acumulado]}}
    # MAIOR -> {numCli: mes}
    maior={}
    for num in cartao.keys():
        perc=0
        m=""
        for mes in cartao[num].keys():
            n=(float(cartao[num][mes][1])/float(cartao[num][mes][0]))
            if n > perc:
                perc=n
                m=mes
        if num in maior.keys():
            maior[num].update(m)
        else:
            maior[num]=m
    return maior