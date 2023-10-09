#!/usr/bin/python3

from calculator_1 import add, mul, div, sub
from sys import argv, exit

if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    size = len(argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
