import json, ReadLogFile

print("Conteúdo Clientes.txt: ")
print(json.dumps(ReadLogFile.Read('clientes.txt'), ensure_ascii=False, indent=2))
