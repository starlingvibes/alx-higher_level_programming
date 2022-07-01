#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()
    tupa = tuple_a + (0, 0)
    tupb = tuple_b + (0, 0)
    sum_tuple = tupa[0] + tupb[0], tupa[1] + tupb[1]
    return sum_tuple
