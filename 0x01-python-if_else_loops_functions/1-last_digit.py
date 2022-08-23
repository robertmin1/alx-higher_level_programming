#!/usr/bin/python3
import random
number = random.randint(-10000,10000)
num = str(number)
if int(num[len(num)-1]) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,num[len(num)-1]))
elif int(num[len(num)-1])==0:
    print("Last digit of {} is {} and is 0".format(number, num[len(num)-1]))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, num[len(num)-1]))
