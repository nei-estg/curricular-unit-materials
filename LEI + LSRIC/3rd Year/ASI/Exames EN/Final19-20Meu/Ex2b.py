import json, ReadLogFile

cartao=ReadLogFile.read('clientes.txt')
print(json.dumps(cartao, ensure_ascii=False, indent=2))