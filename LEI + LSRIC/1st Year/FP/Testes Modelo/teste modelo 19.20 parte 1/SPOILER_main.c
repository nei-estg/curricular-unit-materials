#include <stdio.h>
#include "myModule.h"

int main() {
    int x, y;
    int matrix[SIZE][SIZE] = {{-1, -1, -1},
                              {-1, -1, -1},
                              {-1, -1, -1}};

    imprimeMatriz(matrix);

    for (int i = 0; i < 9; i++) {
        int player = 0;

        if (i % 2 != 0) {
            player = 1;
        }

        printf("Player => %d\n", player);
        printf("Linha | Coluna =>\n");
        x = obtemCoord();
        y = obtemCoord();

        if (verificaPosicaoVazia(matrix, x, y) == 1) {
            matrix[x][y] = player;
        }

        puts("------------------------");
        imprimeMatriz(matrix);
        puts("------------------------");
        if (verificaVitoria(matrix, player) == 1) {
            break;
        }
    }


    return 0;
}

int obtemCoord() {
    int n;

    while (1) {
        scanf("%d", &n);
        if (n == 0 || n == 1 || n == 2) {
            break;
        }
    }

    return n;
}

void imprimeMatriz(int matrix[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int verificaPosicaoVazia(int matrix[SIZE][SIZE], int x, int y) {
    if (matrix[x][y] == -1) {
        return 1;
    }

    return 0;
}

int verificaVitoria(int matrix[SIZE][SIZE], int player) {

    if (matrix[0][0] == player && matrix[0][1] == player && matrix[0][2] == player ||
        matrix[1][0] == player && matrix[1][1] == player && matrix[1][2] == player ||
        matrix[2][0] == player && matrix[2][1] == player && matrix[2][2] == player) {
        printf("Vitoria em linha do player %d\n", player);
        return 1;
    }

    if (matrix[0][0] == player && matrix[1][0] == player && matrix[2][0] == player ||
        matrix[0][1] == player && matrix[1][1] == player && matrix[2][1] == player ||
        matrix[0][2] == player && matrix[1][2] == player && matrix[2][2] == player) {
        printf("Vitoria em coluna do player %d\n", player);
        return 1;
    }

    if (matrix[0][0] == player && matrix[1][1] == player && matrix[2][2] == player) {
        printf("Vitoria em diagonal do player %d\n", player);
        return 1;
    }
    return 0;
}
