#ifndef TOOLS_H
#define TOOLS_H

int *alloc_int_array(int size);
double *alloc_double_array(int size);

int **alloc_int_matrix(int nrows, int ncolumns);
double **alloc_double_matrix(int nrows, int ncolumns);

void free_int_matrix(int **matrix, int nrows);
void free_double_matrix(double **matrix, unsigned int nrows);

void print_int_array(const int *values, int max, const char *s);
void print_double_array(const double *values, int max, const char *s);
void print_int_matrix(int **values, int rows, int columns, const char *s);
void print_double_matrix(double **values, int rows, int columns, const char *s);

#endif /* TOOLS_H */

