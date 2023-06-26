#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for s in range(1, 3):
        try:
            if (s > a):
                raise Exception("Too far")
            else:
                result += (a ** b) / s
        except:
            result = b + a
            break
    return result
