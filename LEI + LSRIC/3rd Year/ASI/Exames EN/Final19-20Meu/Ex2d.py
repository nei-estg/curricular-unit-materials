import ReadLogFile, Stats, json

cartao=ReadLogFile.read('clientes.txt')
top=Stats.topCliente(cartao)
print(json.dumps(top, ensure_ascii=False, indent=2))