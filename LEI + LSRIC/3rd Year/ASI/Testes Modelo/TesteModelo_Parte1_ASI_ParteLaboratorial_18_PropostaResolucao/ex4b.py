import Leitura
import Apurar

nome_ficheiro = "dados.txt"

Condutores,Veiculos = Leitura.ler(nome_ficheiro)
Acumulado = Apurar.acumulado(Condutores, Veiculos)

print (Acumulado)
