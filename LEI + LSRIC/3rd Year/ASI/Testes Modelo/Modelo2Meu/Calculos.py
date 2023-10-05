import LerFicheiro, statistics

def media(alunos):
    # Alunos -> {numero: {uc:nota}}
    # Notas -> {uc: [notas]}
    # Media -> {uc: media}
    notas={}
    medias={}
    for aluno in alunos.keys():
        for uc in alunos[aluno].keys():
            if uc in notas.keys():
                notas[uc].append(int(alunos[aluno][uc]))
            else:
                notas[uc]= [int(alunos[aluno][uc])]

    for uc in notas.keys():
        arr=notas[uc]
        media = statistics.mean(arr)
        medias[uc]=str(media)

    return medias
