import json

import LerFicheiro, Calculos, Listagens, AlterarInfo

# ALÍNEA A)
# Ler para hashtables o conteúdo do ficheiro alunos.txt, invocando e executando para o efeito a função “ler” a criar no módulo
# “LerFicheiro.py”.OBS: A hashtable Alunosdeverá ter como chave o número do aluno e o valor será umhashtable cuja a chave é a UC
# e o valor é anota que o aluno obteve à UC. Para além das hashtables anteriores deverá criar uma hashtable NomeAlunosque terá
# como chave o número do aluno e como valor o nome do aluno.
NomeAlunos, Alunos = LerFicheiro.ler('alunos.txt')
print(json.dumps(Alunos, ensure_ascii=False, indent=2))
print(json.dumps(NomeAlunos, ensure_ascii=False, indent=2))

# ALÍNEA B)
# Percorrendo as hashtables criadas, diga invocando a função “media” a criar no módulo “Calculos.py”, qual é a média de notas por UC.
print("Médias por UC: ")
mediasUc = Calculos.media(Alunos)
print(json.dumps(mediasUc, ensure_ascii=False, indent=2))

# ALÍNEA C)
# Percorrendo  as  hashtables  criadas  liste,  invocando  a  função  “listagem”  a  criar  no  módulo “Listagens.py”,
# o nome dos alunos que tiveram aprovação à UC de ASI.
alunosAprovados = Listagens.listagem(Alunos)
print("Alunos Aprovados a ASI: ")
print(json.dumps(alunosAprovados, ensure_ascii=False, indent=2))

# ALÍNEA D)
# Através da invocação da função “adicionaDados” a criar no módulo “AlterarInfo.py” e da utilização de expressões
# regulares acrescente uma casa decimal à nota. O resultado deve apenas ser mostrado no ecrã.
print("Notas Decimais: ")
AlterarInfo.adicionaDados('alunos.txt')
