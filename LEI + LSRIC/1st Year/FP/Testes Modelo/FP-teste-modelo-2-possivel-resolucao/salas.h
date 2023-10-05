#ifndef SALAS_H
#define SALAS_H

#define SALAS_TAM_INICIAL 1
#define SALA_NOME_MAX 51

typedef struct {
    int capacidade; // capacidade máxima de alunos na sala
    int ocupacao; // número de alunos presentes na sala
    char nome[SALA_NOME_MAX]; // nome da sala, deve ser único
    int *presencas;
} Sala;

typedef struct {
    int contador, tamanho;
    Sala *salas;
} Salas;

void carregarSalas(Salas *salas, char *ficheiro);
void inserirSalas(Salas *salas);
void procurarSalas(Salas salas);
void removerSalas(Salas *salas);
void listarSalas(Salas salas);
void libertarSalas(Salas *salas);
void marcarPresencas(Salas *salas);
void guardarSalas(Salas *salas, char *ficheiro);

#endif /* SALAS_H */

