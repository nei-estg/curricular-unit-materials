import re

nome="Luis Corte-Real Sousa"
nomee=input("Introduza um nome: ")

pattern=re.compile(r'[A-Z]')
str=""

for match in re.finditer(pattern, nomee):
    s=match.start()
    str+= nomee[s].lower() + "."
print(str)

