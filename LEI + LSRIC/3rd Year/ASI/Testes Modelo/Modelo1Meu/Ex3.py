import re


str1="Jose Maria Almeida;00351 962341234;1997-12-19"
str2="Pedro Am Aaaaa Loool Ok Bro;00351 962341234;1997-12-19"
str4="Daniel;00351 912341234;6-12-19"
str3="Zaniel Zazo;00351 962341234;2020-12-19"



pattern=re.compile(
    r'(?P<nome>[A-Z][a-z]+( [A-Z][a-z]+)*);(?P<telefone>00351 9[1|2|3|6][0-9]{7});'
    r'(?P<anonasc>(\d{1}|\d{2}|\d{3}|0[0-9]{3}|1[0-9]{3}|20[0|1][0-9]|202[0|1]))-(?P<mesnasc>([1-9]|0[1-9]|1[0-2]))'
    r'-(?P<dianasc>([1-9]|0[1-9]|[1|2][0-9]|3[0|1]))'
)
nome=pattern.match(str1).group('nome')
telefone=pattern.match(str1).group('telefone')
anonasc=pattern.match(str1).group('anonasc')
mesnasc=pattern.match(str1).group('mesnasc')
dianasc=pattern.match(str1).group('dianasc')
age=2021-int(pattern.match(str1).group('anonasc'))

print(str(nome)+", "+str(telefone)+", "+str(anonasc)+"/"+str(mesnasc)+"/"+str(dianasc)+", em 2021 terá "+str(age)+" anos.")

nome1=pattern.match(str2).group('nome')
telefone1=pattern.match(str2).group('telefone')
anonasc1=pattern.match(str2).group('anonasc')
mesnasc1=pattern.match(str2).group('mesnasc')
dianasc1=pattern.match(str2).group('dianasc')
age1=2021-int(pattern.match(str2).group('anonasc'))

print(str(nome1)+", "+str(telefone1)+", "+str(anonasc1)+"/"+str(mesnasc1)+"/"+str(dianasc1)+", em 2021 terá "+str(age1)+" anos.")

nome=pattern.match(str3).group('nome')
telefone=pattern.match(str3).group('telefone')
anonasc=pattern.match(str3).group('anonasc')
mesnasc=pattern.match(str3).group('mesnasc')
dianasc=pattern.match(str3).group('dianasc')
age=2021-int(pattern.match(str3).group('anonasc'))

print(str(nome)+", "+str(telefone)+", "+str(anonasc)+"/"+str(mesnasc)+"/"+str(dianasc)+", em 2021 terá "+str(age)+" anos.")

nome=pattern.match(str4).group('nome')
telefone=pattern.match(str4).group('telefone')
anonasc=pattern.match(str4).group('anonasc')
mesnasc=pattern.match(str4).group('mesnasc')
dianasc=pattern.match(str4).group('dianasc')
age=2021-int(pattern.match(str4).group('anonasc'))

print(str(nome)+", "+str(telefone)+", "+str(anonasc)+"/"+str(mesnasc)+"/"+str(dianasc)+", em 2021 terá "+str(age)+" anos.")

