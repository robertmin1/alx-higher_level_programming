#!/usr/bin/python3
for i in range(0, 100):
    if i <10:
        print("{}{}, ".format(0, i), end="")
    elif i <=98:
        print("{}, ".format(i), end="")
    else:
        print("{}, ".format(i), end="")
