#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda c: c**2, v)) for v in matrix]
