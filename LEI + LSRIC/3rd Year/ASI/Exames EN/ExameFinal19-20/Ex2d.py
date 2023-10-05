import json, Stats, ReadLogFile

print("Meses em que o cliente teve o valor gasto superior ao valor acumulado: ")
print(json.dumps(Stats.TopCliente(ReadLogFile.Read('clientes.txt')), ensure_ascii=False, indent=2))