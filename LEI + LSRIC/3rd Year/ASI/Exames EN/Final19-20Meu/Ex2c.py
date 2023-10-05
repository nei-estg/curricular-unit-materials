import ReadLogFile, Stats, json

cartao=ReadLogFile.read('clientes.txt')
totais=Stats.totais(cartao)
print(json.dumps(totais, ensure_ascii=False, indent=2))