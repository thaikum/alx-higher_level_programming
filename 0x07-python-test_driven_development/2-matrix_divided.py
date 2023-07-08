#!/usr/bin/python3
"""
This module contains a function
that divides a matrix
"""


def matrix_divided(matrix, div):
    """
    This method divides a matrix by div
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/float"
    size_error = "Each row of the matrix must have the same size"

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)

    new_matrix: list = []
    isFirst = True
    length = 0

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_error)

        if (isFirst):
            length = len(row)
            isFirst = False
        else:
            if (len(row) != length):
                raise TypeError(size_error)
        new_row = []

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(matrix_error)

            new_row.append(round(elem / div, 2))

        new_matrix.append(new_row)

    return new_matrix
