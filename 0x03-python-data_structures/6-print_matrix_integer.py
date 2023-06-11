#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in matrix:
        print(' '.join("{:d}".format(b) for b in c))
