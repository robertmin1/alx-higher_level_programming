#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length-1))
        for i, j in enumerate(range(1, length), 1):
            print("{}: {}".format(i, sys.argv[j]))
