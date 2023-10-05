# Crie  um  programa  em PYTHONque  dada  uma stringcom  um  nome,  telefone(Portugal) e  data  de nascimento valide se
# os dados estão bem inseridos e indique quantos anos terá a pessoa no ano atual.
# Por exemplo:  “Jose  Maria  Almeida;00351  962341234;1997-12-19”  deverá  dar  como  output  “Nome,  Numero  de Telemóvel
# e Data Valida, em 2018 terá 21anos”. Recorra a expressão regulares para resolver o exercício.
import re

str1 = "Jose Maria Almeida;00351 962341234;1997-12-19"
pattern = re.compile(
    r'(?P<nome>[A-Z][a-z]+( [A-Z][a-z]+)*);(?P<telefone>00351 9[1|2|3|6][0-9]{7});(?P<anoNasc>[1|2][0|9][0-9][0-9])'
    r'-(?P<mesNasc>1[0-2]|0[0-9])-(?P<diaNasc>0[0-9]|1[0-9]|2[0-9]|3[0-1])')
nome = pattern.match(str1).group('nome')
telefone = pattern.match(str1).group('telefone')
diaNasc = pattern.match(str1).group('diaNasc')
mesNasc = pattern.match(str1).group('mesNasc')
anoNasc = pattern.match(str1).group('anoNasc')
age = 2018 - int(pattern.match(str1).group('anoNasc'))
# "Nome,  Numero  de Telemóvele Data Valida, em 2018terá 21 anos".
print(str(nome) + ", " + str(telefone) + ", " + str(anoNasc) + "/" + str(mesNasc) + "/"
      + str(diaNasc) + ", em 2018 terá " + str(age) + " anos")
