/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   transacoes.h
 * Author: ricardosilva
 *
 * Created on 12 de fevereiro de 2021, 10:14
 */

#ifndef TRANSACOES_H
#define TRANSACOES_H

#ifdef __cplusplus
extern "C" {
#endif

    typedef enum{ //enumeracao para tipo de transacao
        ALIMENTACAO = 1, COMBUSTIVEL, OUTROS
    }TIPO_TRANSACAO;
    
    typedef struct data_transacao{ //estrutura para a data de transacao
    int ano, mes, dia;
    }DATA;
    
    typedef struct transacoes_empresa{ //estruturta para as transacoes
        DATA data;
        int numero_cartao;
        char descricao_transacao[120];
        TIPO_TRANSACAO tipo_transacao;
        int valor_transacao;
        char nome_colaborador[50];
    }TRANSACOES_EMPRESA;
    
    typedef struct numero_transacoes{ //estrutura para o numero de transacoes
        TRANSACOES_EMPRESA *transacao;
        int cont,tam;
    }NUMERO_TRANSACOES;

    void iniciarTransacoes(NUMERO_TRANSACOES *transacoes); //funcao iniciar transacoes
    void inserirNovaTransacao(NUMERO_TRANSACOES *transacoes); //funcao inserer novas transacoes
    void ObterValorAlimentacaoMesAno(NUMERO_TRANSACOES *transacoes); //funcao obter valor alimentacao
    
#ifdef __cplusplus

#endif

#endif /* TRANSACOES_H */

