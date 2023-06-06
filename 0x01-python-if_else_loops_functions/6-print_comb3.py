for x in range(10):
    for y in range(x + 1, 10):
        if f'{x}{y}' != "89":
            print(f'{x}{y}', end = ', ')
print("89")
