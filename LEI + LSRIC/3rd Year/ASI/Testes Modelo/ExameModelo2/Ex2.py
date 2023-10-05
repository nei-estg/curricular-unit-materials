# Crie um programa em PYTHONque dado um nome na forma “Luis Corte-Real Sousa”, retire as iniciais l.c.r.s seguidas de pontoe em minúsculas. Deverá utilizar uma única expressão regular
import re

nome = "Luis Corte-Real Sousa"
pattern = re.compile(r'[A-Z]')
# str2 = pattern.sub('.', str)
# print(str2)
totalStr = ""
for match in re.finditer(pattern, nome):
    s = match.start()
    e = match.end()
    totalStr += nome[s:e].lower() + "."
print(totalStr)
