#!/usr/bin/env python3

try:
    num_str = input("Give me a number: ")
    num = float(num_str)
    
    if num == int(num):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    pass
