def uppercase(str):
    str_upper = ''
    for x in str:
        if ord(x) in range(98, 123):
            str_upper += f"{chr(ord(x) - 32)}"
        else:
            str_upper += x
    print(f"{str_upper}")
