#!/usr/bin/python
import math
import sys
import time
import os


def get_first_derivative(x):
    ret = 4 * int(sys.argv[6]) * math.pow(x, 3) + 3 * int(sys.argv[5]) * math.pow(x, 2) + 2 * int(
        sys.argv[4]) * x + int(sys.argv[3])
    return ret


def my_function(x):
    ret = int(sys.argv[6]) * math.pow(x, 4) + int(sys.argv[5]) * math.pow(x, 3) + int(sys.argv[4]) * math.pow(x, 2) + \
          int(sys.argv[3]) * x + int(sys.argv[2])
    return ret


def check_interval():
    counter = 0
    if my_function(0) < 0:
        isNegative = True
    else:
        isNegative = False
    i = 0.0
    while (i <= 1.0):
        if my_function(i) > 0 and isNegative is True:
            counter += 1
            isNegative = False
        elif my_function(i) < 0 and isNegative is False:
            counter += 1
            isNegative = True
        i += 0.01
    if counter != 1:
        sys.exit(84)
    return 0


def newton():
    out = 1
    tmp_x = 0.5
    print("x = 0.5")
    x = tmp_x - my_function(tmp_x) / get_first_derivative(tmp_x)
    start_time = time.time()
    while (round(my_function(x), int(sys.argv[7])) != 0):
        if (1 >= x >= 0 and out == 1):
            out = 0
        elif ((1 < x or x < 0) and out == 0):
            sys.exit(84)
        print("x = %.{}f".format(sys.argv[7]) % x)
        tmp_x = x
        x = tmp_x - my_function(tmp_x) / get_first_derivative(tmp_x)
        if (float(time.time()) - float(start_time) > 9.0):
            os.system('clear')
            sys.exit(84)
    print("x = %.{}f".format(sys.argv[7]) % x)
    return tmp_x


def bisection():
    higher = 1
    middle = 0.0
    lower = 0
    i = 0
    start_time = time.time()
    while (abs(higher - lower) > math.pow(10, -int(sys.argv[7]))):
        res = my_function(middle)
        if (res < 0):
            lower = middle
        else:
            higher = middle
        middle = (lower + higher) / 2
        if (i < int(sys.argv[7])):
            print("x = %.{}g".format(sys.argv[7]) % middle)
        else:
            print("x = %.{}f".format(sys.argv[7]) % middle)
        i += 1
        if (float(time.time()) - float(start_time) > 9.0):
            os.system('clear')
            sys.exit(84)
    sys.exit(0)


def secant():
    left = 0
    right = 1
    x = 1
    first = True
    start_time = time.time()
    while(round(my_function(x), int(sys.argv[7]) - 1) != 0):
        x = right - (right - left) / (my_function(right) - my_function(left)) * my_function(right)
        left = right
        right = x
        if (float(time.time()) - float(start_time) > 9.0):
            os.system('clear')
            sys.exit(84)
        if (first):
            print("x = %.{}g".format(sys.argv[7]) % x)
        else:
            print("x = %.{}f".format(sys.argv[7]) % x)
        first = False
    sys.exit(0)


def get_which_algorithm():
    check_interval()
    if (sys.argv[1] == '1'):
        bisection()
    elif (sys.argv[1] == '2'):
        newton()
    elif (sys.argv[1] == '3'):
        secant()
    else:
        sys.exit(84)


def check_for_error():
    try:
        for i in range(1, 8):
            int(sys.argv[i])
        if (int(sys.argv[7]) < 0):
            sys.exit(84)
    except ValueError:
        sys.exit(84)


def my_input():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("USAGE")
        print("    ./105torus opt a0 a1 a2 a3 a4 n")
        print("\nDESCRIPTION")
        print("    opt       method option:")
        print("                  1 for the bisection method")
        print("                  2 for Newton's method")
        print("                  3 for the secant method")
        print("    a[0-4]    coefficients of the equation")
        print("    n         precision (the application of the polynomial to the solution should")
        print("              be samller than 10^-n)")
    elif len((sys.argv)) != 8:
        sys.exit(84)
    else:
        check_for_error()
        get_which_algorithm()
    sys.exit(0)


my_input()
