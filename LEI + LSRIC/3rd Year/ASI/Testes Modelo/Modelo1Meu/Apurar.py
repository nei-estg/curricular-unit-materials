import json, Leitura

condutores, veiculos=Leitura.ler('dados.txt')


def acumulado(condutores, veiculos):
    # Condutores -> { NCarta: [matriculas]}
    # Veiculos -> { Matricula: { Data: [ContraOrd,Coima,DataPagCoima]} }
    # CoimaAcu -> { NCarta: ValorCoimaAcumulado }
    coimaacu={}
    for condutor in condutores.keys():
        for matricula in condutores[condutor]:
            for data in veiculos[matricula].keys():
                for valor in veiculos[matricula][data]:
                        if condutor in coimaacu.keys():
                         coimaacu[condutor] += float(valor[1].strip('€'))
                        else:
                         coimaacu[condutor] = float(valor[1].strip('€'))
    print(json.dumps(coimaacu, ensure_ascii=False, indent=2))