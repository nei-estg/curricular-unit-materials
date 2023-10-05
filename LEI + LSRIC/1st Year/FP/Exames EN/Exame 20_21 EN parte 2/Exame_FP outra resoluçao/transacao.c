#include <stdio.h>
#include <stdlib.h>
#include "transacoes.h"

void cleanInputBuffer() {
    char ch;
    while ((ch = getchar()) != '\n' && ch != EOF);
}

void iniciarTransacoes(TRANSACOES *transacoes) {
    FILE *fp;
    TRANSACOES *temp;
    int sucesso = 0;
    fp = fopen("transacoes.bin", "rb");
    if (fp != NULL) {
        fread(&transacoes->cont, sizeof (int), 1, fp);
        transacoes->tam = transacoes->cont;
        if (transacoes->cont > 0) {
            temp = (TRANSACOES *) malloc(sizeof (TRANSACOES) * transacoes->cont);
            if (temp != NULL) {
                transacoes->transacao = temp;
                fread(transacoes->transacao, sizeof (TRANSACOES), transacoes->cont, fp);
                sucesso = 1;
            }
        } else {
            printf("Ficheiro nao contem transaçoes!\n");
        }
    } else {
        printf("Ficheiro nao abriu!\n");
    }
    if (!sucesso) {
        temp = (TRANSACOES *) malloc(sizeof (TRANSACOES)*5);
        if (temp != NULL) {
            transacoes->transacao = temp;
            transacoes->cont = 0;
            transacoes->tam += 5;
        }
    }
}

void addtransacao(TRANSACOES *transacoes) {
    TRANSACAO *temp = (TRANSACAO *) realloc((transacoes->transacao), sizeof (TRANSACAO)* (transacoes->cont + 2));
    if (temp != NULL) {
        transacoes->tam += 2;
        transacoes->transacao = temp;
    }
}

int VerificaDia() {

    int a;

    do {
        scanf(" %d", &a);

    } while (a <= 0 || a > 31);

    return a;
}

int VerificaMes() {

    int a;

    do {
        scanf(" %d", &a);

    } while (a <= 0 || a > 12);

    return a;
}

int VerificaAno() {

    int a;

    do {
        scanf(" %d", &a);

    } while (a < 1900 || a > 2021);

    return a;
}

float obterFloat(float minValor, float maxValor, char *msg) {
    float valor;
    printf(msg);
    while (scanf("%f", &valor) != 1 || valor < minValor || valor > maxValor) {
        printf("Erro");
        cleanInputBuffer();
        printf(msg);
    }
    cleanInputBuffer();
    return valor;
}

int obterInt(int minValor, int maxValor, char *msg) {
    int valor;
    printf(msg);
    while (scanf("%d", &valor) != 1 || valor < minValor || valor > maxValor) {
        printf("Erro");
        cleanInputBuffer();
        printf(msg);
    }
    cleanInputBuffer();
    return valor;
}

void lerString(char *string, unsigned int tamanho, char *msg) {
    printf(msg);
    if (fgets(string, tamanho, stdin) != NULL) {
        unsigned int len = strlen(string) - 1;
        if (string[len] == '\n') {
            string[len] = '\0';
        } else {
            cleanInputBuffer();
        }
    }
}

void inserirNovaTransacao(TRANSACOES *transacoes) {

    if (transacoes->cont == transacoes->tam) {
        addtransacao(transacoes);

    }
    transacoes->transacao[transacoes->cont].cod_transacao += 1;
    printf("\ntransacao nº:%d", transacoes->transacao[transacoes->cont].cod_transacao);
    printf("\nDia:");
    transacoes->transacao[transacoes->cont].data.dia = VerificaDia();
    printf("\nMes:");
    transacoes->transacao[transacoes->cont].data.mes = VerificaMes();
    printf("\nAno:");
    transacoes->transacao[transacoes->cont].data.ano = VerificaAno();
    transacoes->transacao[transacoes->cont].num_cartao = obterFloat(999999999999999, 9999999999999999, "numero do cartao(16 digitos): ");
    //printf("%.f", transacoes->transacao[transacoes->cont].num_cartao);
    lerString(transacoes->transacao[transacoes->cont].descricao, 120, "Descrição da transação: ");
    transacoes->transacao[transacoes->cont].valor = obterFloat(0, 9999999999999999, "Valor transacao: ");
    transacoes->transacao[transacoes->cont].tipo = obterInt(0, 4, "tipo de transação:ALIMENTACAO =1 | COMBUSTIVEL=2 | OUTROS=3: ");
    lerString(transacoes->transacao[transacoes->cont].nome, 50, "nome do funcionario responsavel pela transação: ");

    FILE *fp;
    fp = fopen("transacoes.bin", "rb+");

    if (fp == NULL) {
        fclose(fp);
        fp= fopen("transacoes.bin","wb");
        fwrite(&transacoes->cont, sizeof (transacoes->cont), 1, fp);
        fwrite(transacoes->transacao, sizeof (TRANSACAO), transacoes->cont, fp);
        fclose(fp);
        transacoes->cont++;
        
        
    } else {
        fp = fopen("transacoes.bin", "wb+");
        fread(&transacoes->cont, sizeof (transacoes->cont), 1, fp);
        fread(transacoes->transacao, sizeof (TRANSACAO), transacoes->cont, fp);
        fwrite(&transacoes->cont, sizeof (transacoes->cont), 1, fp);
        fwrite(transacoes->transacao, sizeof (TRANSACAO), transacoes->cont, fp);

        fclose(fp);
        transacoes->cont++;
    }


}

void ObterValorAlimentacaoMesAno(TRANSACOES *transacoes) {
    int a;
    float total;
    printf("\nAno:");
    scanf("%d", &a);
    total = 0;

    printf("Gastos ano %d", a);
    for (int i = 0; i < transacoes->cont; i++) {
        if (transacoes->transacao[i].data.ano == a && transacoes->transacao[i].tipo == 1) {
            printf("numero de transaçao: %d     valor: %f", transacoes->transacao[i].cod_transacao, transacoes->transacao[i].valor);
            total += transacoes->transacao[i].valor;
        }
    }
        
    
    printf("Total = %f", total);
}



