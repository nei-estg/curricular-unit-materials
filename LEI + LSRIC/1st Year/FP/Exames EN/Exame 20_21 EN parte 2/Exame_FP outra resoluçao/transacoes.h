

#ifndef TRANSACOES_H
#define TRANSACOES_H

#ifdef __cplusplus
extern "C" {
#endif

    typedef enum {
        ALIMENTACAO = 1, COMBUSTIVEL, OUTROS
    } TIPO;

    typedef struct {
        int dia, mes, ano;
    } DATA;

    typedef struct {
        int cod_transacao, tipo;
        float num_cartao, valor;
        char descricao[120], nome[50];
        DATA data;
    } TRANSACAO;

    typedef struct {
        TRANSACAO *transacao;
        int cont, tam;
    } TRANSACOES;

    void cleanInputBuffer();
    void iniciarTransacoes(TRANSACOES *transacoes);
    void addtransacao(TRANSACOES *transacoes);
    int VerificaDia();
    int VerificaMes();
    int VerificaAno();
    float obterFloat(float minValor, float maxValor, char *msg);
    int obterInt(int minValor, int maxValor, char *msg);
    void lerString(char *string, unsigned int tamanho, char *msg);
    void inserirNovaTransacao(TRANSACOES *transacoes);
#ifdef __cplusplus
}
#endif

#endif /* TRANSACOES_H */

