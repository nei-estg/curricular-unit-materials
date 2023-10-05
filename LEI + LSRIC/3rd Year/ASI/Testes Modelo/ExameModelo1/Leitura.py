import json

def ler(filename):
    with open(filename, encoding='utf-8') as fp:
        # Condutores -> { NCarta: [matriculas]}
        # Veiculos -> { Matricula: { Data: [ContraOrd,Coima,DataPagCoima]} }
        NCARTA, MATRICULA, DATA, CONTRAORD, COIMA, DATAPAGCOIMA = 0, 1, 2, 3, 4, 5
        condutores = {}
        veiculos = {}
        contraOrds = {}
        for line in fp:
            line = line.strip().split(';')
            if line[NCARTA] in condutores.keys():
                if line[MATRICULA] not in condutores[line[NCARTA]]:
                    condutores[line[NCARTA]].append(line[MATRICULA])
            else:
                condutores[line[NCARTA]] = [line[MATRICULA]]
            if line[MATRICULA] in veiculos.keys():
                if line[DATA] in veiculos[line[MATRICULA]].keys():
                    veiculos[line[MATRICULA]][line[DATA]].append([line[CONTRAORD], line[COIMA], line[DATAPAGCOIMA]])
                else:
                    veiculos[line[MATRICULA]].update(
                        {line[DATA]: [[line[CONTRAORD], line[COIMA], line[DATAPAGCOIMA]]]})
            else:
                contraOrds = {line[DATA]: [[line[CONTRAORD], line[COIMA], line[DATAPAGCOIMA]]]}
                veiculos[line[MATRICULA]] = contraOrds
        # print(json.dumps(condutores, ensure_ascii=False, indent=2))
        # print(json.dumps(veiculos, ensure_ascii=False, indent=2))

    return condutores, veiculos
