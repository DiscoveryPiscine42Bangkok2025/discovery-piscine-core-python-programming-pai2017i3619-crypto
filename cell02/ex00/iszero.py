#!/usr/bin/env python3
import sys

try:
    line = input()
    number = int(line.strip())
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except EOFError:
    pass
except:
    pass
