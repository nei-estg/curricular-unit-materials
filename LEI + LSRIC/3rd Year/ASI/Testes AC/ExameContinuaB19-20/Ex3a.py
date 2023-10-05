import json

import LerFicheiro

print("Conteúdo de socios.csv: ")
print(json.dumps(LerFicheiro.ler('socios.csv'), ensure_ascii=False, indent=2))
