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

int procurardia(NUMERO_TRANSACOES transacoes, int dia, int mes, int ano, TIPO_TRANSACAO tipo){
    for (int i = 0; i < transacoes.cont; i++) {
        if (transacoes.transacao[i].tipo_transacao == tipo) {
            if (transacoes.transacao[i].data.ano == ano) {
                if (transacoes.transacao[i].data.mes == mes) {
                    if (transacoes.transacao[i].data.dia == dia) {
                        return i;
                    }
                }
            }
        }
    }
    return -1;
}