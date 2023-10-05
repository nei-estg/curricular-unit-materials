import LerFicheiro

def listagem(alunos, nomes):
    # Alunos -> {numero: {uc:nota}}
    # NomeAluno -> {numero: nome}
    # Aprovs -> {uc: [alunos]}
    aprovs={}
    for aluno in alunos.keys():
        for uc in alunos[aluno].keys():
            if uc == "ASI" and int(alunos[aluno][uc])>9:
                if uc in aprovs.keys():
                    aprovs[uc].append(nomes[aluno])
                else:
                    aprovs[uc]=[nomes[aluno]]
    return aprovs


