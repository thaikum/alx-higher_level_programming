#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_values: int = 0
    try:
        for y in range(0, x):
            print(my_list[y], end="")
            printed_values += 1
    except IndexError:
        raise
    finally:
        print('')
        return printed_values
