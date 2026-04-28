#!/usr/bin/env python3
import sys

def main():
    # If no parameters (only script name exists), display none
    if len(sys.argv) == 1:
        print("none")
        return

    # Slice to ignore the script name itself
    params = sys.argv[1:]
    
    for p in params:
        # Only process if it doesn't already end in 'ism'
        if not p.endswith("ism"):
            # Display the parameter with 'ism' appended
            print(f"{p}ism")

if __name__ == "__main__":
    main()
