#!/usr/bin/python3
# Francis Shoke Ngosianga

""" Defines a function that append a string at
    the end of a text file(UTF8).
"""


def append_write(filename="", text=""):
    """ appends to a file if it exits
        otherwise create the file and write to it.
        And return the number of characters added.
    """
    with open(filename, 'a') as f:
        num_of_chars = 0
        for r in text:
            num_of_chars += 1
            f.write(r)
    return num_of_chars
