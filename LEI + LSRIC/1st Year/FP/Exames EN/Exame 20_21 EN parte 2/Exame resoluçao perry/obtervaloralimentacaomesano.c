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
#include "input.h"

void ObterValorAlimentacaoMesAno(NUMERO_TRANSACOES *transacoes){
    
    float valor_total = 0;
    int ano,mes,calculados = 0;
    int n;
    TIPO_TRANSACAO tipo = ALIMENTACAO;
    
    if (transacoes->cont > 0) {
        
        ano=obterInt(1900,2021,"Insira o ano da transação!:","ERRO\n");
        mes=obterInt(1,12,"Insira o ano da transação!:","ERRO\n");
        
        for(int i=0;i<31;i++){
            n = procurardia(*transacoes, mes, ano, i, tipo);
            if(n!=-1){
                calculados++;
                valor_total+=transacoes->transacao[n].valor_transacao;
            }
        }
        if(calculados>0){
            
        printf("Valor de Alimentação do %d/%d:%.1f",mes,ano,valor_total);
        }
        else{
        printf("Nao existe informação do mês %d do %d!\n",mes,ano,valor_total);
        }
    }
    else {
        printf("Não existem transações na memória!\n");
    }
    fclose(fp);
}