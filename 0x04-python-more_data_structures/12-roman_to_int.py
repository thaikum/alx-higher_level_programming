#!/usr/bin/python3
def roman_to_int(roman_string):
    try:
        roman_string = roman_string.upper()
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        decimal = 0

        for ind, char in enumerate(roman_string):
            if (ind < len(roman_string) - 1):
                if (romans[roman_string[ind + 1]] > romans[char]):
                    decimal -= romans[char]
                    continue
            decimal += romans[char]

        return decimal
    except Exception as e:
        return None
