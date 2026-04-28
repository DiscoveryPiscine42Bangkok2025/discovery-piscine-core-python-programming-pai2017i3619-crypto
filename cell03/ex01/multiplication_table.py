#!/usr/bin/env python3

try:
    print("Enter a number")
    num = int(input().strip())
    
    i = 0
    while i < 10:
        result = i * num
        print(f"{i} x {num} = {result}")
        i += 1
except:
    pass
