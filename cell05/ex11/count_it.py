#!/usr/bin/env python3
import sys

def main():
    # Subtract 1 because sys.argv[0] is the script name
    count = len(sys.argv) - 1
    
    # If no parameters were passed, display "none"
    if count == 0:
        print("none")
    else:
        print(f"parameters: {count}")
        # Use a for loop to iterate through parameters starting from index 1
        for param in sys.argv[1:]:
            print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()
