import json, LerFicheiro, Listagens

alunos, nomes= LerFicheiro.ler('alunos.txt')

aprovacoes=Listagens.listagem(alunos,nomes)
print(json.dumps(aprovacoes, ensure_ascii=False, indent=2))