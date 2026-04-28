#!/usr/bin/env python3

try:
    print("Enter the first number:")
    n1 = int(input().strip())
    print("Enter the second number:")
    n2 = int(input().strip())
    
    result = n1 * n2
    
    print(f"{n1} x {n2} = {result}")
    
    if result < 0:
        print("The result is negative.")
    elif result > 0:
        print("The result is positive.")
    else:
        print("The result is positive and negative.")
except:
    pass
