#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    # new = [[item**2 for item in row] for row in matrix]
    # new = [list(map(lambda x: x**2, row)) for row in matrix]
    new = []
    for row in matrix:
        new.append([item**2 for item in row])
    return new
