import re

with open('clientes.txt') as fp:
   pattern = re.compile(r'(?P<numero>8\d{5});(?P<mes>Jan|Fev|Mar|Abr|Mai|Jun|Jul|Ago|Set|Out|Nov|Dez)'
                             r';(?P<valorgasto>\d+);(?P<valoracumulado>\d+)')
   for line in fp:
       if pattern.match(line):
           gasto=pattern.match(line).group('valorgasto')+"€"
           acumulado=pattern.match(line).group('valoracumulado')+"€"
           newline=pattern.sub("\g<numero>;\g<mes>;"+gasto+";"+acumulado, line)
           print(newline)
fp.close()