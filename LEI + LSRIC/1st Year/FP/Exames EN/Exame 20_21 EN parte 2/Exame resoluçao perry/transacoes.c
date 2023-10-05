/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "transacoes.h"

void IniciarTransacoes(NUMERO_TRANSACOES *transacoes){
    
    FILE *fp;
    TRANSACOES_EMPRESA *temp;
    int sucesso = 0;
    
    fp= fopen("transacoes.bin", "rb");
    
    if(fp != NULL){
        fread(&transacoes->cont, sizeof(int), 1, fp);
        transacoes->tam = transacoes->cont;
        
        if(transacoes->cont>0){
        temp=(TRANSACOES_EMPRESA*)malloc(sizeof(TRANSACOES_EMPRESA)*transacoes->cont);
        
        if(temp != NULL){
        transacoes->transacao = temp;
        fread(transacoes->transacao,sizeof(TRANSACOES_EMPRESA), transacoes->cont, fp);
        sucesso = 1;
        }
        }
        else{
            printf("O FICHEIRO ESTÁ VAZIO!\n");
        }
    }
    else{
        printf("ERRO NA ABERTURA DO FICHEIRO!\n");
    }
    if(!sucesso){
        temp = (TRANSACOES_EMPRESA*) malloc(sizeof(TRANSACOES_EMPRESA)*10);
        
        if(temp != NULL){
            transacoes->transacao = temp;
            transacoes->cont = 0;
            transacoes->tam += 10;
        }
    }
}