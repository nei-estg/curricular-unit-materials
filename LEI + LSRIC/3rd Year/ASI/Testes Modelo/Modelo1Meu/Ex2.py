import re

h1="2016/05/15 23:43:01"
h2="2016/05/15 24:00:59"
h3="2015/13/21 12:00:01"

pattern=re.compile(
    r'^[0-2]\d\d\d/(0\d|1[0-2])/(0/d|[1|2][0-9]|3[0|1]) ([0-1]\d|2[0-3]):[0-5]\d:[0-5]\d'
)

if pattern.match(h1):
    print(h1+" válido")
else:
    print(h1+" inválido")

if pattern.match(h2):
    print(h2+" válido")
else:
    print(h2+" inválido")
if pattern.match(h3):
    print(h3+" válido")
else:
    print(h3+" inválido")

for x in range(5):
    h4=input("Insira uma data: ")

    if pattern.match(h4):
        print("válido")
    else:
       print("inválido")