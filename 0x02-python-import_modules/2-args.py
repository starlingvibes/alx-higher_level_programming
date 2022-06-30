#!/usr/bin/python3
import sys


arglength = len(sys.argv) - 1
if arglength <= 0:
    print(f"{arglength} arguments.")
elif arglength >= 1:
    if arglength == 1:
        print(f"{arglength} argument:")
        print(f"{arglength}: {sys.argv[1]}")
    else:
        print(f"{arglength} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
