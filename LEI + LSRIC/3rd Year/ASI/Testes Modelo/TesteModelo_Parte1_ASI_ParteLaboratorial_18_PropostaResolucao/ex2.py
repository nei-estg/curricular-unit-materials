import re
str="2016/02/28 23:43:12"
dias = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}

print (dias['01'])

pattern = re.compile(r'^(?P<ano>\d{4})\/(?P<mes>\d{2})\/(?P<dia>\d{2})\s(?P<hora>\d{2}):(?P<minutos>\d{2}):(?P<segundos>\d{2})$')
res = pattern.match(str)

if res:
	if int(res.group('ano')) > 1900 and int(res.group('ano')) < 2019 and int(res.group('mes')) > 0 and int(res.group('mes')) < 13 and int(res.group('dia')) <= dias[res.group('mes')] and int(res.group('hora')) < 24 and int(res.group('minutos')) < 60 and int(res.group('segundos')) < 60:
		print ("OK")
	else:
		print ("NOT OK")
else:
	print ("DOES NOT MATCH")
