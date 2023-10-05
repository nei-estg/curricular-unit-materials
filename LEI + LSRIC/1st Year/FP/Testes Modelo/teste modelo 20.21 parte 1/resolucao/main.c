#include <stdio.h>
#include <stdlib.h>

#define NUM_CIDADES 6
#define TAM_TRAJETO 6

void printMatriz(int cidade[NUM_CIDADES][NUM_CIDADES]) {
    int i, j;
    for (i = 0; i < NUM_CIDADES; i++) {
        puts("");
        for (j = 0; j < NUM_CIDADES; j++) {
            printf("%3d", cidade[i][j]);
        }
    }
}

int verificaSimetria(int cidade[NUM_CIDADES][NUM_CIDADES]) {
    int i, j;
    for (i = 0; i < NUM_CIDADES - 1; i++) {
        for (j = i + 1; j < NUM_CIDADES; j++) {
            if (cidade[i][j] != cidade[j][i]) {
                return 0;
            }
        }
    }
    return 1;
}

int obtemConexaoEntreCidades(int cidade1, int cidade2) {
    int op;
    do {
        printf("Insira um valor para %d %d:", cidade1, cidade2);
        scanf("%d", &op);
    } while (op != 0 || op != 1);
    return op;
}

int validaTrajeto(int trajeto[]) {
    int i, j;

    for (i = 0; i < TAM_TRAJETO - 1; i++) {
        for (j = i + 1; j < TAM_TRAJETO; j++) {
            if (trajeto[i] == trajeto[j]) {
                return 0;
            }
        }

    }

    for (i = 0; i < TAM_TRAJETO; i++) {
        if (trajeto[i] < 0 || trajeto[i] >= NUM_CIDADES) {
            return 0;
        }
    }

    return 1;
}

int verificaTrajeto(int trajeto[TAM_TRAJETO], int cidade[NUM_CIDADES][NUM_CIDADES]) {
    int i;
    for (i = 0; i < TAM_TRAJETO - 1; i++) {
        if (cidade[trajeto[i]][trajeto[i + 1]] == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int i, j;

    int trajeto[TAM_TRAJETO] = {0, 2, 1, 3, 4, 5};
    int trajeto2[TAM_TRAJETO] = {0, 1, 2, 3, 4, 5};

    int cidades[NUM_CIDADES][NUM_CIDADES] = {
        {1, 0, 1, 0, 0, 1},
        {0, 1, 1, 1, 0, 1},
        {1, 1, 1, 0, 1, 1},
        {0, 1, 0, 1, 1, 0},
        {0, 0, 1, 1, 1, 1},
        {1, 1, 1, 0, 1, 1}
    };
    int cidades2[NUM_CIDADES][NUM_CIDADES];

    // 1
    printf("\n%d", verificaTrajeto(trajeto, cidades));
    printf("\n%d", verificaTrajeto(trajeto2, cidades));

    // 2
    for (i = 0; i < NUM_CIDADES - 1; i++) {
        cidades2[i][i] = 1;
        for (j = i + 1; j < NUM_CIDADES; j++) {
            cidades2[i][j] = cidades2[j][i] = obtemConexaoEntreCidades(i, j);
        }
    }
    /*
    printMatriz(cidades2);

    // 3
    //cidades[1][0] = !cidades[1][0];
    printf("\n%d", verificaSimetria(cidades));
    printf("\n%d", verificaSimetria(cidades2));

    // 4
    printf("\n%d", validaTrajeto(trajeto));
    printf("\n%d", validaTrajeto(trajeto2));

*/
    return 0;
}

