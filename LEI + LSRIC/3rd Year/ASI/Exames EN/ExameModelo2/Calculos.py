import json, statistics

import LerFicheiro

NomeAlunos, Alunos = LerFicheiro.ler('alunos.txt')


# print(json.dumps(Alunos, ensure_ascii=False, indent=2))


def media(dictionary):
    # notasUC -> {UC : [notas]}
    notasUC = {}
    mediaUCs = {}
    for studentNumb in dictionary.keys():
        for uc in dictionary[studentNumb].keys():
            if uc not in notasUC.keys():
                notasUC[uc] = [int(dictionary[studentNumb][uc])]
            else:
                notasUC[uc].append(int(dictionary[studentNumb][uc]))

    for uc in notasUC.keys():
        arr = notasUC[uc]
        mediaUC = statistics.mean(arr)
        mediaUCs[uc] = str(mediaUC)

    # print(json.dumps(notasUC, ensure_ascii=False, indent=2))
    # print(json.dumps(mediaUCs, ensure_ascii=False, indent=2))
    return mediaUCs

