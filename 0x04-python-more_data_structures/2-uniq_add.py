#!/usr/bin/python3
def uniq_add(my_list=[]):
    ak = set(my_list)
    j = 0
    for num in ak:
        j += num
    return j
