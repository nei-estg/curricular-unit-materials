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
#include "procurardia.c"

void ExpandirTrans(NUMERO_TRANSACOES *transacao){
    TRANSACOES_EMPRESA *temp= (TRANSACOES_EMPRESA *) realloc(transacao->transacao, sizeof (TRANSACOES_EMPRESA)*(transacao->cont+5));
    
    if(temp != NULL){
        transacao->tam += 5;
        transacao->transacao = temp;
    }
}

void inserirNovaTransacao(NUMERO_TRANSACOES *transacao) {
    if(transacao->cont == transacao->tam){
        ExpandirTrans(transacao);
    }
    TIPO_TRANSACAO tipo;
    
    int dia,mes,ano;
    
    dia = obterInt(0, 32, "Dia transação: ");
    mes = obterInt(0, 32, "Mes transação: ");
    ano = obterInt(0, 32, "Ano da transação: ");
    tipo = obterInt(1,3, "Tipo de transação:\n- ALIMENTACAO = 1\n- COMBUSTIVEL = 2\n- OUTROS = 3");
    
    if(procurardia(*transacao,mes, ano , dia, tipo) == -1){
        
    transacao->transacao[transacao->cont].data.dia = dia;
    transacao->transacao[transacao->cont].data.mes = mes;
    transacao->transacao[transacao->cont].data.ano = ano;
    transacao->transacao[transacao->cont].tipo_transacao = tipo;
    transacao->transacao[transacao->cont].numero_cartao = obterInt(999999999999999, 9999999999999999, "numero do cartao(16 digitos):");
    lerString(transacao->transacao[transacao->cont].descricao_transacao, 120, "descrição da transacao:");
    lerString(transacao->transacao[transacao->cont].nome_colaborador, 120, "nome do colaborador da transacao:");
    transacao->cont++;
    }
    else{
        printf("Transação existente na memória!");
    }
}