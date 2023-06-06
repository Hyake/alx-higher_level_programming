#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
