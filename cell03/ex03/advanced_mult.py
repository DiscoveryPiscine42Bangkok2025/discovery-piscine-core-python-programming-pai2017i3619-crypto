#!/usr/bin/env python3
import sys

def main():
    # If there are any arguments (sys.argv length > 1), print none
    if len(sys.argv) > 1:
        print("none")
        return

    table_num = 0
    while table_num <= 10:
        # Start each line with the table name
        print(f"Table de {table_num}:", end="")
        
        multiplier = 0
        while multiplier <= 10:
            # Print the result followed by a space
            print(f" {table_num * multiplier}", end="")
            multiplier += 1
            
        # Move to the next line after finishing a table
        print()
        table_num += 1

if __name__ == "__main__":
    main()
