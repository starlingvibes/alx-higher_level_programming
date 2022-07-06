#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1:
        set_1 = set()
    if not set_2:
        set_2 = set()
    return set_1.intersection(set_2)
