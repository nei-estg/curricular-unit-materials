import re

def adicionaDados(file):
    with open(file) as fp:
        pattern=re.compile(r'(?P<uc>[A-Z]+);(?P<num>\d{7});(?P<nome>\D*);(?P<nota>([0-1][0-9]|20|\d{1}))')
        for line in fp:
            notaa=float(pattern.match(line).group('nota'))
            new = pattern.sub(r"\g<uc>;\g<num>;\g<nome>;" + str(notaa), line)
            print(new)


