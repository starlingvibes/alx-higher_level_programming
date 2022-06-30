#!/usr/bin/python3
import sys


sumint = 0
for i in range(1, len(sys.argv)):
    sumint += int(sys.argv[i])
print(f"{sumint}")
