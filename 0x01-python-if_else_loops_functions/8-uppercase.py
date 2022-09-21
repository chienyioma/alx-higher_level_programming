#!/usr/bin/python3
def uppercase(str):
    for i in str:
# Check for lowercase using if statement
        num = ord(i)
        if((num >= 97) and (num <= 122)):
# Convert lowercase to uppercase
            ch = chr(num - 32)
        else:
            ch = chr(num)
        print("{}".format(ch), end="")
    print()
