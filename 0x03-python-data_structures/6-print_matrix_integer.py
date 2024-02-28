#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in range(len(row)):
            if item != len(row) - 1:
                print("{:d}".format(row[item]), end=" ")
            else:
                print("{:d}".format(row[item]), end="")
        print()
