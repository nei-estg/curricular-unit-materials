import re

str="Jose Maria Almeida;00351 962341234;1997-12-19"

pattern = re.compile(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)+;00351 \d{9};(\d{4})\-\d{2}\-\d{2}$')
g = pattern.match(str)

if g:
	idade = (2018-int(g.group(2)))
	print ("Nome, numero de telemovel e data valida, em 2018 tera", idade, "anos")
else:
	print ("NOT OK")
