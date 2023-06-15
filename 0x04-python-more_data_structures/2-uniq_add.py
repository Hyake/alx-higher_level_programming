#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_one = list(set(my_list))
    total = 0
    for c in new_one:
        total += c
    return total
