#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num = len(argv)
    result = 0
    if num > 1:
        for i in range(1, num):
            result += int(argv[i])
    print("{:d}".format(result))
