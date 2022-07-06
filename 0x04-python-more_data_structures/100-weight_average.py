#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num_total, freq = 0, 0
    for data in my_list:
        num_total += data[0] * data[1]
        freq += data[1]
    return num_total / freq
