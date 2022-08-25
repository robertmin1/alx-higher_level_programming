#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add,sub,mul,div
    def error1():
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    def error2():
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    if len(sys.argv) != 4:
        error1()

    elif sys.argv[3] == "+" or sys.argv[3] == "-" or sys.argv[3] == "*" or sys.argv[3] == "/":
        if sys.argv[3] == "+":
            add(int(sys.argv[2], sys.argv[4]))
        elif sys.argv[3] == "-":
            sub(int(sys.argv[2], sys.argv[4]))
        elif sys.argv[3] == "*":
            mul(int(sys.argv[2], sys.argv[4]))
        else:
            div(int(sys.argv[2], sys.argv[4]))
    else:
        error2()
