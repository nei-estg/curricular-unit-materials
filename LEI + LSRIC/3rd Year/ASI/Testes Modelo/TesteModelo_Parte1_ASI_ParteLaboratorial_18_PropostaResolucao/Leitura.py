
def ler(nome_ficheiro):
	Condutores = {}
	Veiculos = {}
	with open(nome_ficheiro) as fp:
		for linha in fp:
			linha = linha.strip().split(";")
			if linha[0] in Condutores.keys():
				Condutores[linha[0]].append(linha[1])
			else:
				matriculas = [linha[1]]
				Condutores[linha[0]] = matriculas

			if linha[1] in Veiculos.keys():
				Veiculos[linha[1]][linha[2]]=[linha[3],linha[4],linha[5]]	
			else:
				contra_ordenacoes = {}
				contra_ordenacoes[linha[2]]=[linha[3],linha[4],linha[5]]
				Veiculos[linha[1]] = contra_ordenacoes
				
	fp.close()
	return Condutores,Veiculos
