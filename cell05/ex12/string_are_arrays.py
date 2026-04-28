#!/usr/bin/env python3
import sys

def main():
    # Must have exactly 1 parameter (len is 2)
    if len(sys.argv) != 2:
        print("none")
        return

    input_string = sys.argv[1]
    
    # Check if 'z' exists at all
    if 'z' not in input_string:
        print("none")
    else:
        # Loop through each character (treating string as an array)
        for char in input_string:
            if char == 'z':
                # print(char, end='') is also an option, 
                # but the PDF shows them on one line.
                # Actually, standard behavior usually implies 
                # one print if they are together. 
                # Let's check the PDF example... 
                # It shows 'zzz' for three z's.
                print('z', end='')
        print() # Final newline

if __name__ == "__main__":
    main()
