import json, Leitura

condutores, veiculos = Leitura.ler('dados.txt')


def acumulado(condutores, veiculos):
    # Condutores -> { NCarta: [matriculas]}
    # Veiculos -> { Matricula: { Data: [ContraOrd,Coima,DataPagCoima]} }
    # CoimaAcu -> { NCarta: ValorCoimaAcumulado }
    coimaAcu = {}
    for condutor in condutores.keys():
        for matriculaCond in condutores[condutor]:
            for dataCoima in veiculos[matriculaCond].keys():
                for valorCoima in veiculos[matriculaCond][dataCoima]:
                        if condutor in coimaAcu.keys():
                            coimaAcu[condutor] += float(valorCoima[1].strip('€'))
                        else:
                            coimaAcu[condutor] = float(valorCoima[1].strip('€'))
    print(json.dumps(coimaAcu, ensure_ascii=False, indent=2))
