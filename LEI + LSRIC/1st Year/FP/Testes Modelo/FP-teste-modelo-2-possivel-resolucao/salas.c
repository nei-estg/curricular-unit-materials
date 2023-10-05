#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "salas.h"
#include "input.h"
#include "tools.h"

void imprimirSala(Sala sala) {
    int i;
    printf("\nNome: %s Capacidade: %3d Ocupação: %3d Presenças: ", sala.nome, sala.capacidade, sala.ocupacao);
    for (i = 0; i < sala.ocupacao; i++) {
        printf("%d - ", sala.presencas[i]);
    }
}

void apagarDadosSala(Sala *sala) {
    sala->capacidade = 0;
    sala->ocupacao = 0;
    strcpy(sala->nome, "");
    sala->presencas = NULL;
}

void carregarSalas(Salas *salas, char *ficheiro) {
    int i, sucesso = 0;

    FILE *fp = fopen(ficheiro, "rb");
    if (fp != NULL) {

        fread(&salas->contador, sizeof (int), 1, fp);

        if (salas->contador > 0) {
            salas->tamanho = salas->contador;
            salas->salas = (Sala*) malloc(salas->contador * sizeof (Sala));
            for (i = 0; i < salas->contador; i++) {
                fread(&salas->salas[i], sizeof (Sala), 1, fp);

                salas->salas[i].presencas = alloc_int_array(salas->salas[i].capacidade);
                fread(salas->salas[i].presencas, sizeof (int), salas->salas[i].capacidade, fp);
            }
            sucesso = 1;
        }

        fclose(fp);
    }

    if (!sucesso) {
        fp = fopen(ficheiro, "wb");
        if (fp != NULL) {

            salas->salas = (Sala*) malloc(SALAS_TAM_INICIAL * sizeof (Sala));
            salas->contador = 0;
            salas->tamanho = SALAS_TAM_INICIAL;

            fclose(fp);
        }
    }

}

void guardarSalas(Salas *salas, char *ficheiro) {
    int i;

    FILE *fp = fopen(ficheiro, "wb");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    fwrite(&salas->contador, sizeof (int), 1, fp);

    for (i = 0; i < salas->contador; i++) {
        fwrite(&salas->salas[i], sizeof (Sala), 1, fp);
        fwrite(salas->salas[i].presencas, sizeof (int), salas->salas[i].capacidade, fp);
    }

    fclose(fp);
}

int procurarSala(Salas salas, char* nome) {
    int i;
    for (i = 0; i < salas.contador; i++) {
        if (strcmp(salas.salas[i].nome, nome) == 0) {
            return i;
        }
    }

    return -1;
}

void libertarSalas(Salas *salas) {
    if (salas->salas) {
        free(salas->salas);
        salas->salas = NULL;
    }

    salas = NULL;
}

int inserirSala(Salas *salas) {
    char nome[SALA_NOME_MAX];

    lerString(nome, SALA_NOME_MAX, "\nNome sala: ");

    if (procurarSala(*salas, nome) == -1) {

        strcpy(salas->salas[salas->contador].nome, nome);

        salas->salas[salas->contador].capacidade = obterInt(0, 50, "Capacidade: ");
        salas->salas[salas->contador].ocupacao = 0;
        salas->salas[salas->contador].presencas = alloc_int_array(salas->salas[salas->contador].capacidade);

        return salas->contador++;
    }

    return -1;
}

void expandirSalas(Salas *salas) {
    int tam = (salas->tamanho) == 0 ? SALAS_TAM_INICIAL : salas->tamanho * 2;
    Sala *temp = (Sala*) realloc(salas->salas, sizeof (Sala) * (tam));
    if (temp != NULL) {
        salas->tamanho = tam;
        salas->salas = temp;
    }
}

void inserirSalas(Salas *salas) {
    if (salas->contador == salas->tamanho) {
        expandirSalas(salas);
    }

    if (salas->contador < salas->tamanho) {
        if (inserirSala(salas) == -1) {
            puts("Sala já existe.");
        }
    } else {
        puts("Não é possível inserir uma nova sala.");
    }
}

void procurarSalas(Salas salas) {
    int sala;

    char nome[SALA_NOME_MAX];
    lerString(nome, SALA_NOME_MAX, "\nNome sala: ");

    if (procurarSala(salas, nome) != -1) {
        imprimirSala(salas.salas[sala]);
    } else {
        puts("A sala não existe.");
    }
}

void removerSalas(Salas *salas) {
    int i, sala;

    char nome[SALA_NOME_MAX];
    lerString(nome, SALA_NOME_MAX, "\nNome sala: ");

    sala = procurarSala(*salas, nome);

    if (sala != -1) {

        free(salas->salas[sala].presencas);

        for (i = sala; i < salas->contador - 1; i++) {
            salas->salas[i] = salas->salas[i + 1];
        }

        apagarDadosSala(&salas->salas[i]);
        salas->contador--;

    } else {
        puts("A sala não existe.");
    }
}

void listarSalas(Salas salas) {
    int i;

    if (salas.contador > 0) {
        for (i = 0; i < salas.contador; i++) {
            imprimirSala(salas.salas[i]);
        }
    } else {
        puts("Lista vazia");
    }
}

void marcarPresencas(Salas *salas) {
    int i, existe = 0, sala, numero;

    char nome[SALA_NOME_MAX];
    lerString(nome, SALA_NOME_MAX, "\nNome sala: ");

    sala = procurarSala(*salas, nome);

    if (sala != -1) {

        if (salas->salas[sala].ocupacao < salas->salas[sala].capacidade) {

            numero = obterInt(0, 1000, "\nNumero aluno: ");

            for (i = 0; i < salas->salas[sala].ocupacao; i++) {
                if (numero == salas->salas[sala].presencas[i]) {
                    existe = 1;
                }
            }

            if (!existe) {
                salas->salas[sala].presencas[salas->salas[sala].ocupacao] = numero;
                salas->salas[sala].ocupacao++;
            } else {
                puts("\nO aluno já existe.");
            }

        } else {
            puts("\nA sala está cheia.");
        }

    } else {
        puts("A sala não existe.");
    }
}

