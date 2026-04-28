#!/usr/bin/env python3

secret = "Python is awesome"

try:
    user_input = input().strip()
    
    if user_input == secret:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
except:
    pass
