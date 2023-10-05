import json, Stats, ReadLogFile

print("Total Gasto e Acumulado por Cliente: ")
print(json.dumps(Stats.Totais(ReadLogFile.Read('clientes.txt')), ensure_ascii=False, indent=2))
