#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return (sum([c * d for c, d in my_list])/sum(d for c, d in my_list))
    return 0
