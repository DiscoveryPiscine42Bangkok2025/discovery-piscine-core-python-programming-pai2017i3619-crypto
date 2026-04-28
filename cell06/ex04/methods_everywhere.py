#!/usr/bin/env python3
import sys

# Method to display only the first eight characters
def shrink(s):
    print(s[:8])

# Method to append 'Z' until the string is eight characters long
def enlarge(s):
    # Calculate how many Zs are needed
    needed = 8 - len(s)
    print(s + ('Z' * needed))

def main():
    # If no arguments are provided, display 'none'
    if len(sys.argv) == 1:
        print("none")
    else:
        # Process each argument
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) < 8:
                enlarge(arg)
            else:
                # If exactly eight, just print it
                print(arg)

if __name__ == "__main__":
    main()
