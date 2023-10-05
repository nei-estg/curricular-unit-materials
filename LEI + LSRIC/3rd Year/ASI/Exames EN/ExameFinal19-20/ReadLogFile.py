def Read(filename):
    with open(filename) as fp:
        # Cartao -> { NCliente: { Mes: [ValorGasto, ValorAcumulado] } }
        cartao = {}
        NUMCLIENTE, MES, VALORGASTOCOMPRAS, VALORACUMULADOCARTAO = 0, 1, 2, 3
        for line in fp:
            line = line.strip().split(';')
            if line[NUMCLIENTE] in cartao.keys():
                if line[MES] in cartao[line[NUMCLIENTE]].keys():
                    cartao[line[NUMCLIENTE]][line[MES]].append(line[VALORGASTOCOMPRAS], line[VALORACUMULADOCARTAO])
                else:
                    cartao[line[NUMCLIENTE]][line[MES]] = [[line[VALORGASTOCOMPRAS], line[VALORACUMULADOCARTAO]]]
            else:
                cartao[line[NUMCLIENTE]] = {line[MES]: [[line[VALORGASTOCOMPRAS], line[VALORACUMULADOCARTAO]]]}
    return cartao
