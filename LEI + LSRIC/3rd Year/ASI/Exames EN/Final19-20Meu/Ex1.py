import hashlib
import re

with open('clientes.txt') as fp:
    with open('clientesSHA256.txt','w') as fp_2:
        pattern =re.compile(r'(?P<numero>8\d{5});(?P<mes>Jan|Fev|Mar|Abr|Mai|Jun|Jul|Ago|Set|Out|Nov|Dez)'
                            r';(?P<valorgasto>\d+);(?P<valoracumulado>\d+)')
        for line in fp:
            if pattern.match(line):
                num=pattern.match(line).group('numero')
                numHash=hashlib.sha256(num.encode('utf-8')).hexdigest()
                newline=pattern.sub(numHash+";\g<mes>;\g<valorgasto>;\g<valoracumulado>", line)
                fp_2.write(newline)
fp.close()
fp_2.close()