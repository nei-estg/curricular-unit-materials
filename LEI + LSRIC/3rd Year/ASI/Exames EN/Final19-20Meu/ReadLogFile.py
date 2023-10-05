def read(file):
    with open(file, encoding='utf-8') as fp:
        #CARTAO -> {numCli: {mes:[gasto, acumulado]}}
        NUM, MES, GASTO, ACUMULADO = 0,1,2,3
        cartao={}
        for line in fp:
            line=line.strip().split(';')
            if line[NUM] in cartao.keys():
                if line[MES] in cartao[line[NUM]].keys():
                    cartao[line[NUM]][line[MES]].append(line[GASTO],line[ACUMULADO])
                else:
                    cartao[line[NUM]][line[MES]]=[line[GASTO],line[ACUMULADO]]
            else:
                cartao[line[NUM]]={line[MES]:[line[GASTO],line[ACUMULADO]]}
    return cartao
    fp.close()