import re

with open('clientes.txt') as fp:
    pattern = re.compile(r'(?P<nCliente>\d{6});(?P<mes>Jan|Fev|Mar|Abr|Mai|Jun|Jul|Ago|Set|Out|Nov|Dez);'
                         r'(?P<valorGasto>\d+);(?P<valorAcumulado>\d+)')
    for line in fp:
        if pattern.match(line):
            print(pattern.sub("\g<nCliente>;\g<mes>;\g<valorGasto>€;\g<valorAcumulado>€", line))
