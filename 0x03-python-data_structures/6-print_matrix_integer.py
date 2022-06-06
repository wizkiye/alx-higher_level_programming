#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for int_list in matrix:
        for num in int_list:
                print("{:d}".format(num), end="")
                print(" ", end="")

        print()
