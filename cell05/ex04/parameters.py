#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] is the script name, so we subtract 1 from the total length
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()
