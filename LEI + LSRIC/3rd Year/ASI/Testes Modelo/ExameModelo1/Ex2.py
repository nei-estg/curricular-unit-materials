# Faça  um  programa  em PYTHONque  valide,  através  de  uma  expressão  regular,  se  umadata  ehora introduzida no
# formato AAAA/MM/DD HH:MM:SS é válida.
import re

pattern = re.compile(
    r'^\d\d\d\d\/(0?[1-9]|1[0-2])\/(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$')

str1 = "2016/05/15 23:43:01"

if pattern.match(str1):
    print("válido")
else:
    print("inválido")

str2 = "2016/05/15 24:00:59"

if pattern.match(str2):
    print("válido")
else:
    print("inválido")

str3 = "2015/13/21 12:00:01"

if pattern.match(str3):
    print("válido")
else:
    print("inválido")