#!/usr/bin/python3
"""
A class inheriting from the list class
"""


class MyList(list):
    """
    Class MyList inherits from list
    """
    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
