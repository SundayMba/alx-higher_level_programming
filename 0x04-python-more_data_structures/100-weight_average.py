#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    sum = 0
    weight_sum = 0
    average = 0
    for score, weight in my_list:
        sum += score * weight
        weight_sum += weight
    average = sum / weight_sum
    return average
