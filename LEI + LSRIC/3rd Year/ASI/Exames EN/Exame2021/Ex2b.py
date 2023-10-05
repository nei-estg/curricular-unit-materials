import Stats, json, LerFicheiro

vendas=LerFicheiro.ler('dados.txt')
totvendas=Stats.totais(vendas)
print(json.dumps(totvendas, ensure_ascii=False, indent=2))