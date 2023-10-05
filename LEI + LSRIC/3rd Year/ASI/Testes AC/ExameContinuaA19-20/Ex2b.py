import json

import Calculo, LerFicheiro

print(json.dumps(Calculo.DespesasMes(LerFicheiro.ler('despesas2019.csv')), ensure_ascii=False, indent=2))
