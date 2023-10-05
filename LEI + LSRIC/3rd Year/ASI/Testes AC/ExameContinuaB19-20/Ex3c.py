import json, LerFicheiro, Calculo

print("Sócios com valores em atraso: ")
print(json.dumps(Calculo.ModalidadesPagar(LerFicheiro.ler('socios.csv')), ensure_ascii=False, indent=2))
