#!/usr/bin/env python3
import sys

def main():
    # Check for exactly 2 parameters (len is 3)
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        # Convert parameters to integers
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        # Construct the array using range
        # Note: range(start, end) stops BEFORE the end, 
        # so we use end + 1 to make it inclusive.
        res = list(range(start, end + 1))
        
        # Display the array
        print(res)
    except ValueError:
        # In case the parameters aren't valid numbers
        print("none")

if __name__ == "__main__":
    main()
