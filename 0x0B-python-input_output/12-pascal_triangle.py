#!/usr/bin/python3

"""
pascal triangle
"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    def f(x):
        y = 1;
        for k in range(1, x + 1):
            y *= k

        return y

    if n <= 0:
        return []

    triangle = []
    for r in range(n):
        row = []
        for each in range(r + 1):
            row.append(int(f(r) / (f(each) * f(r - each))))
        triangle.append(row)

    return triangle
