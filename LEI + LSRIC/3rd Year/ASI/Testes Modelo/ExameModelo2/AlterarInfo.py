import re


def adicionaDados(filename):
    with open(filename) as fp:
        pattern = re.compile(r'(?P<uc>\D{1,3});(?P<numA>\d{7});(?P<nomeA>\D*);(?P<nota>\d{1,2})')
        for line in fp:
            nota = float(pattern.match(line).group('nota'))
            notas_dec = pattern.sub(r"\g<uc>;\g<numA>;\g<nomeA>;" + str(nota), line)
            print(notas_dec)
