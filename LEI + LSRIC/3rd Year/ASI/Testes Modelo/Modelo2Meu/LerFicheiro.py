import json
#Alunos -> {numero: {uc:nota}}
#NomeAluno -> {numero: nome}

def ler(file):
    with open(file, encoding='utf-8') as fp:
        UC, NUMERO, NOME, NOTA = 0,1,2,3
        alunos={}
        nomes={}
        for line in fp:
            line=line.strip().split(';')
            if line[NUMERO] not in nomes.keys():
                nomes[line[NUMERO]] = line[NOME]
            if line[NUMERO] in alunos.keys():
                alunos[line[NUMERO]].update({line[UC]: line[NOTA]})
            else:
                alunos[line[NUMERO]]={line[UC]: line[NOTA]}
    return alunos, nomes

