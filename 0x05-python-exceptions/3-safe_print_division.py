#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
