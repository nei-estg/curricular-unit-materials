import json

import LerFicheiro

print(json.dumps(LerFicheiro.ler('despesas2019.csv'), ensure_ascii=False, indent=2))

