#!/usr/bin/env python3
import sys

def main():
    # Length 2 means the script name + 1 actual parameter
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

if __name__ == "__main__":
    main()
