#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        i = '0' + str(i)
    if i == 99:
        print(i)
        break
    print(i, end=', ')
