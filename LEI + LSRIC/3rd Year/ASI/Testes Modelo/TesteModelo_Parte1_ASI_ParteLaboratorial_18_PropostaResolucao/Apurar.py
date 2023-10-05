
def acumulado(Condutores, Veiculos):
	Acumulado = {}
	for condutor in Condutores.keys():
		valor = 0
		for matricula in set(Condutores[condutor]):
			for data in Veiculos[matricula].keys():	
				valor =  valor + float(Veiculos[matricula][data][1])
		Acumulado[condutor] = valor	
	return Acumulado
