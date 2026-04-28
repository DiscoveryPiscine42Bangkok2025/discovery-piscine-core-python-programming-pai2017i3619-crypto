#!/usr/bin/env python3

try:
    user_input = input("What you gotta say? : ")
    while True:
        if user_input == "STOP":
            break
        user_input = input("I got that! Anything else? : ")
except EOFError:
    pass
except:
    pass
