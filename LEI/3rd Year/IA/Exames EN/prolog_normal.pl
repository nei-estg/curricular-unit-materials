
%1
%viajar(origem, destino, pcr, vacina, recuperado)
viajar(_, portugal, 0, 0, 0).
viajar(portugal, espanha, 1, 0, 0).
viajar(portugal, reinounido, 1, 1, 0).
viajar(portugal, franca, 1, 1, 1).

%2
%pode_entrar(origem, destino, pcr, vacina, recuperado)
pode_entrar(O,D,1,_,_):-viajar(O,D,1,_,_), !.
pode_entrar(O,D,_,1,_):-viajar(O,D,_,1,_), !.
pode_entrar(O,D,_,_,1):-viajar(O,D,_,_,1), !.
pode_entrar(O,D,_,_,_):-viajar(O,D,0,0,0).

%multa(pais,valor)
multa(espanha,500).
multa(franca,750).
multa(reino_unido,1250).

%entrou(id,pais,legalmente)
entrou(1,espanha,sim).
entrou(2,espanha,nao).
entrou(3,espanha,nao).
entrou(4,espanha,nao).
entrou(5,reino_unido,sim).
entrou(6,reino_unido,nao).

lucro_multas(Pais,X):-findall(X,entrou(_,Pais,nao),L),
    length(L,N),
    multa(Pais, M),
    X is N*M, !.
lucro_multas(_,0).