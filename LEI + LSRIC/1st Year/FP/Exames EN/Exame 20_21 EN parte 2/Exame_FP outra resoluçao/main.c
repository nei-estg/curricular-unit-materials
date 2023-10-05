#include <stdio.h>
#include <stdlib.h>
#include "transacoes.h"


int main() {

    int opcao;
    TRANSACOES transacoes;
    
     iniciarTransacoes(&transacoes);

    do {
        printf("\nTransaçoes------------------------------------------------------");
        printf("\n1 - Inserir Transaçao");
        printf("\n2 - Obter valor do mes e ano");
        printf("\n0 - Sair");
        printf("\n------------------------------------------------------------");

        puts("\nOpção:");
        scanf("%d", &opcao);

        switch (opcao) {
            case 0:
                break;
            case 1:
                inserirNovaTransacao(&transacoes);
                break;
            case 2:
                ObterValorAlimentacaoMesAno(&transacoes);
                break;
            default:
                printf("\nOpcão invalida!");
        }

    } while (opcao != 0);

    
    
    return 0;

}

