#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        mul = list((map(lambda t: t[0] * t[1],  my_list)))
        sumofmul = sum(mul)
        weight = list(map(lambda t: t[1], my_list))
        sumofweight = sum(weight)
        Average = sumofmul / sumofweight
        return Average
