import hashlib
import re

with open('clientes.txt') as fp:
    with open('clientesSHA256.txt', 'w') as new_fp:
        pattern = re.compile(r'(?P<nEstudante>8\d{5});(?P<mes>Jan|Fev|Mar|Abr|Mai|Jun|Jul|Ago|Set|Out|Nov|Dez);'
                             r'(?P<valorGasto>\d*);(?P<valorAcumulado>\d*)')
        NUMESTUDANTE, MES, VALORGASTOCOMPRAS, VALORACUMULADOCARTAO = 0, 1, 2, 3
        for line in fp:
            if pattern.match(line):
                noStudent = pattern.match(line).group('nEstudante')
                noStudentHashed = hashlib.sha256(noStudent.encode('utf-8')).hexdigest()
                new_line = pattern.sub(noStudentHashed + ";\g<mes>;\g<valorGasto>;\g<valorAcumulado>", line)
                new_fp.write(new_line)

fp.close()
new_fp.close()
