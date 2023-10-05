import re

str1 = "joaomail@gmail.com,BrinCar2017,23/10/2019"
str2 = "joaomail@gmail.com,BrinCar2017,23/13/2019"
str3 = "joaomail@gmail.com,1234567,23/13/2019"
pattern = re.compile(r'(?P<utilizador>[a-zA-Z0-9-_!?.]*\@\D*\.com|pt|eu|info),'
                     r'(?P<password>[a-zA-Z0-9.-_?!]*),'
                     r'(?P<data>(0[0-9]|1[0-9]|2[0-9]|3[0-1])\/(0[1]|0[3-9]|1[0-2])\/([1][9][7|8|9][0-9]|[2][0][0|1][0-9])|(0[0-9]|1[0-9]|2[0-8])\/(0[2])\/([1-2][0|9][0|1|7|8|9][0-9]))')

if pattern.match(str1):
    print("Válido")
else:
    print("Inválido")

if pattern.match(str2):
    print("Válido")
else:
    print("Inválido")

if pattern.match(str3):
    print("Válido")
else:
    print("Inválido")
