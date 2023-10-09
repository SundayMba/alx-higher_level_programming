#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for item in row:
            print("{:d}".format(item), end="")
            count += 1
            if count != len(row):
                print(end=" ")
        print("")
