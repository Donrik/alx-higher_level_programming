#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if(num1 is 8) and (num2 is 9):
            print("{}".format(str(num1) + str(num2)))
        elif(num1 > num2):
            print("{}".format(str(num1) + str(num2)) + ", ", end="")
