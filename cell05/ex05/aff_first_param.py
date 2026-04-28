#!/usr/bin/env python3
import sys

def main():
    # If the length is 1, it means only the script name exists (no parameters)
    if len(sys.argv) == 1:
        print("none")
    else:
        # Print the parameter at index 1
        print(sys.argv[1])

if __name__ == "__main__":
    main()
