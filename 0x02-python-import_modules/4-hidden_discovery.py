#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    methods = dir(hidden_4)
    for method in methods:
        if (method[0]) != '_':
            print(method)
