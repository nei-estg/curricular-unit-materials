import json
import Modelo1Meu.Leitura


condutores, veiculos = Leitura.ler('dados.txt')
print(json.dumps(condutores, ensure_ascii=False, indent=2))
print(json.dumps(veiculos, ensure_ascii=False, indent=2))