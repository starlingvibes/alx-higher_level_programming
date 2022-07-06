#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return dict()
    return {key: a_dictionary[key]*2 for index, key in enumerate(a_dictionary)}
