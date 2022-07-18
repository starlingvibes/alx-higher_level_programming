#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except BaseException:
        return False
    else:
        return True
