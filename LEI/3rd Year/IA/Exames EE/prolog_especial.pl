%nota(uc, ano, aluno, ects, nota)
nota('Sistemas de Informação', 3, joao, 16, 16).
nota('Sistemas de Informação', 3, carlos, 6, 12).
nota('Inteligência Artificial', 3, maria, 5, 12).
nota('Sistemas Operativos', 2, joao, 5, 13).
nota('Sistemas Operativos', 2, maria, 15, 10).
nota('Bases de Dados', 2, joao, 13, 12).

%ano(ects, ano)
ano(E, 1):-E >= 0, E =< 39, !.
ano(E, 2):-E > 39, E =< 99, !.
ano(E, 3):-E >= 100, E =< 180, !.
ano(_, -1).

primeiraUC(Estudante, Ano, UC):-nota(UC, Ano, Estudante,_,_), !.

completou(Estudante, Ano):-findall(_, nota(_, Ano, Estudante,_,_), Lista),
    length(Lista, 12).