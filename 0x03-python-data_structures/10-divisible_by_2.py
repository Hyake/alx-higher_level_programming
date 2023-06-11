#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = [c % 2 == 0 for c in my_list]
    return even
