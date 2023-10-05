/*
 * File:   main.c
 * Author: ESTG
 */

#include <stdio.h>

#include "salas.h"
#include "input.h"

#define SALAS_DB_FILE  "salas.bin"

/*
 * Teste modelo parte 2
 */
int main() {
    int opcao;
    Salas salas;

    carregarSalas(&salas, SALAS_DB_FILE);

    do {
        printf("\nSalas------------------------------------------------------");
        printf("\n1 - Inserir");
        printf("\n2 - Procurar");
        printf("\n3 - Remover");
        printf("\n4 - Listar");
        printf("\n5 - Marcar Presença");
        printf("\n6 - Guardar");
        printf("\n0 - Sair");
        printf("\n------------------------------------------------------------");
        printf("\nSalas: %d/%d", salas.contador, salas.tamanho);

        opcao = obterInt(0, 6, "\nOpção: ");

        switch (opcao) {
            case 0:
                break;
            case 1:
                inserirSalas(&salas);
                break;
            case 2:
                procurarSalas(salas);
                break;
            case 3:
                removerSalas(&salas);
                break;
            case 4:
                listarSalas(salas);
                break;
            case 5:
                marcarPresencas(&salas);
                break;
            case 6:
                guardarSalas(&salas, SALAS_DB_FILE);
                break;
            default:
                printf("\nOpcão invalida!");
        }

    } while (opcao != 0);

    libertarSalas(&salas);

    return 0;
}
