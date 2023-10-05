#include <stdio.h>
#include <stdlib.h>

#include "tools.h"

int *alloc_int_array(int size) {
    return (int*) calloc(size, sizeof (int));
}

double *alloc_double_array(int size) {
    return (double*) malloc(size * sizeof (double));
}

int **alloc_int_matrix(int nrows, int ncolumns) {
    int i = 0, **temp = (int**) malloc(nrows * sizeof (int*));
    for (; i < nrows; ++i) {
        temp[i] = alloc_int_array(ncolumns);
    }
    return temp;
}

double **alloc_double_matrix(int nrows, int ncolumns) {
    int i = 0;
    double **temp = (double**) malloc(nrows * sizeof (double*));
    for (; i < nrows; ++i) {
        temp[i] = alloc_double_array(ncolumns);
    }
    return temp;
}

void free_int_matrix(int **matrix, int nrows) {
    int i = 0;
    for (; i < nrows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

void free_double_matrix(double **matrix, unsigned int nrows) {
    int i = 0;
    for (; i < nrows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

void print_int_array(const int *values, int max, const char *s) {
    int i = 0;
    printf("\n%s: ", s);
    for (; i < max; ++i) {
        printf("|%d", values[i]);
    }
}

void print_double_array(const double *values, int max, const char *s) {
    int i = 0;
    printf("\n%s: ", s);
    for (; i < max; ++i) {
        printf("|%.3f", values[i]);
    }
}

void print_int_matrix(int **values, int rows, int columns, const char *s) {
    int i = 0, j;
    printf("\n%s: ", s);
    for (; i < rows; ++i) {
        printf("\n");
        for (j = 0; j < columns; ++j) {
            printf("|%d", values[i][j]);
        }
    }
}

void print_double_matrix(double **values, int rows, int columns, const char *s) {
    int i = 0, j;
    printf("\n%s: ", s);
    for (; i < rows; ++i) {
        printf("\n");
        for (j = 0; j < columns; ++j) {
            printf("|%.2f", values[i][j]);
        }
    }
}