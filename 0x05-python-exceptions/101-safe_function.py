#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=stderr)
        result = None
    finally:
        return result
