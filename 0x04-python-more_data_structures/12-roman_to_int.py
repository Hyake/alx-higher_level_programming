#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        dictionary = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        number = 0
        for m, n in zip(roman_string, roman_string[1:]):
            if dictionary[m] < dictionary[n]:
                number -= dictionary[m]
            else:
                number += dictionary[m]
        number += dictionary[roman_string[-1]]
        return number
    else:
        return 0
