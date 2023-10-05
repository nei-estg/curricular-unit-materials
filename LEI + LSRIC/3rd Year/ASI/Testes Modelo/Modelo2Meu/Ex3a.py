import json, LerFicheiro

alunos, nomes= LerFicheiro.ler('alunos.txt')
print(json.dumps(alunos, ensure_ascii=False, indent=2))
print(json.dumps(nomes, ensure_ascii=False, indent=2))