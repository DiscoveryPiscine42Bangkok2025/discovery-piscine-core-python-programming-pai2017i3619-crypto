#!/usr/bin/env python3
import sys

def main():
    # Check for exactly 2 parameters (len of 3)
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]
    
    # Use the count method to find occurrences
    count = search_string.count(keyword)
    
    # If count is 0, requirements say display none
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()
