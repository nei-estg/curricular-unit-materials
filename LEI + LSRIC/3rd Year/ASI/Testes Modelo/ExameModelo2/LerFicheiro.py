import json


def ler(filename):
    with open(filename) as fp:
        # Alunos -> { NAluno: { UC: Nota } }
        # NomeAluno -> { NAluno: Nome }
        UC, NUMALUNO, NOME, NOTA = 0, 1, 2, 3
        Alunos = {}
        NomeAlunos = {}
        ucDict = {}
        for student in fp:
            student = student.strip().split(';')
            if student[NUMALUNO] not in NomeAlunos:
                NomeAlunos[student[NUMALUNO]] = student[NOME]
            if student[NUMALUNO] not in Alunos:
                ucDict = {student[UC]: student[NOTA]}
                Alunos[student[NUMALUNO]] = ucDict
            else:
                ucDict = {student[UC]: student[NOTA]}
                Alunos[student[NUMALUNO]].update(ucDict)
    return NomeAlunos, Alunos
    # print(json.dumps(NomeAlunos, ensure_ascii=False, indent=2))
    # print(json.dumps(Alunos, ensure_ascii=False, indent=2))


ler('../Modelo2Meu/alunos.txt')
