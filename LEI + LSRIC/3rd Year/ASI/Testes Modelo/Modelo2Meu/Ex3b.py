import json, LerFicheiro, Calculos

alunos, nomes = LerFicheiro.ler('alunos.txt')

medias=Calculos.media(alunos)
print(json.dumps(medias, ensure_ascii=False, indent=2))