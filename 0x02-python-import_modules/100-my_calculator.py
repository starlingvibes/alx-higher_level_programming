#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif operators.get(argv[2]) is not None:
        a = int(argv[1])
        b = int(argv[3])
        func = operators[argv[2]](a, b)  # brilliant lol
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], func))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
