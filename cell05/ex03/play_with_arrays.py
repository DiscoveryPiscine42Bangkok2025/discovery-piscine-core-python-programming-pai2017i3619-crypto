#!/usr/bin/env python3

def main():
    # The original array
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # 1. Filter (> 5) and Math (+ 2)
    # 2. Wrap it in set() to remove duplicates
    new_array = set([x + 2 for x in original if x > 5])
    
    # Display exactly as shown in the example
    print(original)
    print(new_array)

if __name__ == "__main__":
    main()
