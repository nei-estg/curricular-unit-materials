import json, statistics

import LerFicheiro

NomeAlunos, Alunos = LerFicheiro.ler('alunos.txt')
print(json.dumps(Alunos, ensure_ascii=False, indent=2))


def listagem(dictionary):
    alunosApproved = []
    for studentNumb in dictionary.keys():
        if "ASI" in dictionary[studentNumb].keys():
            if float(dictionary[studentNumb]["ASI"]) >= 9.5:
                alunosApproved.append(NomeAlunos[studentNumb])
    return alunosApproved


print(listagem(Alunos))
