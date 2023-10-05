import json

def ler(filename):
    with open(filename, encoding='utf-8') as fp:
        #Condutores -> {NCarta: [matriculas]}
        #Veiculos -> {Matricula: {Data: [cont,coima,data]}}
        NCARTA, MATRICULA, DATA, CONTRAORD, COIMA, DATAPAG = 0,1,2,3,4,5
        condutores={}
        veiculos={}
        contraords={}
        for line in fp:
            line=line.strip().split(';')
            if line[NCARTA] in condutores.keys():
                if line[MATRICULA] not in condutores[line[NCARTA]]:
                    condutores[line[NCARTA]].append(line[MATRICULA])
            else:
                condutores[line[NCARTA]]=[line[MATRICULA]]
            if line[MATRICULA] in veiculos.keys():
                if line[DATA] in veiculos[line[MATRICULA]].keys():
                    veiculos[line[MATRICULA]][line[DATA]].append([line[CONTRAORD,line[COIMA],line[DATAPAG]]])
                else:
                    veiculos[line[MATRICULA]].update(
                        {line[DATA]: [[line[CONTRAORD], line[COIMA], line[DATAPAG]]]})
            else:
                contraords={line[DATA]: [[line[CONTRAORD],line[COIMA],line[DATAPAG]]]}
                veiculos[line[MATRICULA]]=contraords;

    return condutores, veiculos