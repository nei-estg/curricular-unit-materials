# Crie  um  programa  em PYTHONdado  um  IP  em  formato  CIDR  valide  se  o  mesmo  esta  bem  formado.
# (exemplo ip: 192.168.1.0/24; 10.10.10.0/16)
import re

ip1 = "92.168.1.0/24"
ip2 = "10.255.10.0/16"

pattern = re.compile(
    r'^((\d{1}|\d{2}|[0|1][0-9][0-9]|[2][0-5][0-5])\.){3}(\d{1}|\d{2}|[0|1][0-9][0-9]|[2][0-5][0-5])\/(\d{1}|1[0-9]|2[0-9]|3[0-2])$')

if pattern.match(ip1):
    print(ip1+" válido")
else:
    print(ip1+" inválido")

if pattern.match(ip2):
    print(ip2+" válido")
else:
    print(ip2+" inválido")
