#!/usr/bin/env python3
import sys

# Define the method as requested
def downcase_it(string):
    return string.lower()

def main():
    # Check if there are no parameters (sys.argv[0] is the script name)
    if len(sys.argv) == 1:
        print("none")
    else:
        # Loop through parameters starting from index 1
        for param in sys.argv[1:]:
            # Apply the method and display its return value
            print(downcase_it(param))

if __name__ == "__main__":
    main()
