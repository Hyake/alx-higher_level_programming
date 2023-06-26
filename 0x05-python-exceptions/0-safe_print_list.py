#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    my_list_len = 0
    try:
        for c in my_list:
            my_list_len += 1
        for d in range(0, x):
            print("{}".format(my_list[d]), end='')
            count += 1
        print()
        return (count)
    except IndexError:
        print("")
        return my_list_len
