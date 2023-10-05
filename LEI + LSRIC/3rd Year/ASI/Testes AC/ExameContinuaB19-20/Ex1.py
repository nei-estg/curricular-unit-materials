import re

pattern = re.compile(r'(?P<data>(0[0-9]|1[0-9]|2|[0-9]|3[0-9])\/(0([1]|[3-9])|1[0-2])\/[1-2][0|9][0-9][0-9]);'
                     r'(?P<descricao>.*);(?P<montante>(-\d*.\d*)|(\d*.\d*))')

dateNow = "18/11/2019"

with open('transacoes.txt') as fp:
    totDebito = 0
    totCredito = 0
    print("Transações feitas na data " + dateNow + ":")
    for line in fp:
        if pattern.match(line):
            montante = float(pattern.match(line).group('montante'))
            if pattern.match(line).group('data') == dateNow:
                print(pattern.match(line).group('descricao'))
                if montante < 0:
                    totDebito += montante
                else:
                    totCredito += montante

    print("O total de débito na data " + dateNow + ": " + str(round(totDebito, 2)) + "€")
    print("O total de crébito na data " + dateNow + ": " + str(totCredito) + "€")
