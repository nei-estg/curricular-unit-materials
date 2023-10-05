import json

import Leitura, Apurar

condutores, veiculos = Leitura.ler('dados.txt')

Apurar.acumulado(condutores, veiculos)
