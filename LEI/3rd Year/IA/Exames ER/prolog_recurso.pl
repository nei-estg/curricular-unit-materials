
%1
%estado(dia,concelho,incidencia,rt)
estado(49, braga, 123, 0.97).
estado(50, braga, 180, 1.02).
estado(51, braga, 198, 1.01).
estado(49, lisboa, 170, 1.24).
estado(50, lisboa, 220, 1.04).
estado(51, lisboa, 60, 0.97).
estado(49, porto, 97, 0.9).
estado(50, porto, 120, 1.05).
estado(51, porto, 170, 1.0).


risco(D,C,1):-estado(D,C,I,R),I<120,R<1.
risco(D,C,2):-estado(D,C,I,R),I<120,R>=1.
risco(D,C,3):-estado(D,C,I,R),I>=120,R<1.
risco(D,C,4):-estado(D,C,I,R),I>=120,R>=1.

lista_concelhos(D, Risco, L):-findall(X, (risco(D,X,R), R >= Risco), L).

variacao(C, D1, D2, melhorou):-risco(D1,C,R1), risco(D2,C,R2),R1 > R2, !.
variacao(C, D1, D2, piorou):-risco(D1,C,R1), risco(D2,C,R2),R1 < R2, !.
variacao(_, _, _, manteve).