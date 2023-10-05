


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: ricardosilva
 *
 * Created on 10 de fevereiro de 2021, 18:13
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "transacoes.h"
#include "input.h"

/*

 * 
 */
int main(int argc, char** argv) {

    int selecao;
    NUMERO_TRANSACOES transacoes;
    
    iniciarTransacoes(&transacoes);

    do {
        printf("************ Transações Empresa ************\n");
        printf("1 - Inserir Lista de Transações.\n");
        printf("2 - Calcular Valor de Pagamentos Alimentação.\n");
        printf("0 - Sair.\n\n");

        puts("Escolha uma das seleções: ");
        scanf("%d", &selecao);

        switch (selecao){
            case 0:
                break;
            case 1:
                inserirNovaTransacao(&transacoes);
                break;
            case 2:
                ObterValorAlimentacaoMesAno(&transacoes);
                break;
            default:
                printf("\nA seleção escolhida não existe!\n\n");
        }
    }
    while(selecao != 0);
    
    return (EXIT_SUCCESS);
}







