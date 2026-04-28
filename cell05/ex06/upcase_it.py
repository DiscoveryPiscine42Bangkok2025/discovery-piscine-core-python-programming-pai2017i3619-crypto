#!/usr/bin/env python3
import sys

def main():
    # We need exactly 1 parameter, so total length must be 2
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

if __name__ == "__main__":
    main()
