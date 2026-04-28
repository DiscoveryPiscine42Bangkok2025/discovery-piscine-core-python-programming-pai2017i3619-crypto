#!/usr/bin/env python3
import math

try:
    num_str = input("Give me a number: ")
    num = float(num_str)
    rounded_num = math.ceil(num)
    print(rounded_num)
except:
    pass
