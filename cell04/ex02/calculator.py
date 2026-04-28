#!/usr/bin/env python3

try:
    n1 = int(input("Give me the first number: "))
    n2 = int(input("Give me the second number: "))
    
    print("Thank you!")
    
    print(f"{n1} + {n2} = {n1 + n2}")
    print(f"{n1} - {n2} = {n1 - n2}")
    print(f"{n1} / {n2} = {int(n1 / n2)}")
    print(f"{n1} * {n2} = {n1 * n2}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except:
    pass
