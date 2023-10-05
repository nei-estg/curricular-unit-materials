import re

ip="192.168.1.0/24"

pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\/(\d{1,2})$')
g = pattern.match(ip)

if int(g.group(1)) < 255 and int(g.group(2)) < 255 and int(g.group(3)) < 255 and int(g.group(4)) < 255 and int(g.group(5)) > 7 and int(g.group(5)) < 33:
	print ("IP VALIDO")
else:
	print ("IP INVALIDO")
