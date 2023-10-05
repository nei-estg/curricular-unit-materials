import json, LerFicheiro

vendas=LerFicheiro.ler('dados.txt')
print(json.dumps(vendas, ensure_ascii=False, indent=2))
