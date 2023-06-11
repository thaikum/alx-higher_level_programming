#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        row_len = len(row)
        for column in row:
            print("{:d}".format(column), end="")
            if index != row_len - 1:
                print('', end=' ')
            else:
                print('')
            index += 1
