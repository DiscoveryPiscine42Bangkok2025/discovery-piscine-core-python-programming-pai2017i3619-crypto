#!/usr/bin/env python3

def main():
    # The same original array
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # Build the new array: add 2 only to values > 5
    new_array = [x + 2 for x in original_array if x > 5]
    
    # Print exactly as shown in the example
    print(original_array)
    print(new_array)

if __name__ == "__main__":
    main()
