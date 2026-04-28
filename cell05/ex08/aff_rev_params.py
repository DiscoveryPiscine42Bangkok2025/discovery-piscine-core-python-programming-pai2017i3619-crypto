#!/usr/bin/env python3
import sys

def main():
    # sys.argv includes the script name, so len < 3 means fewer than 2 params
    if len(sys.argv) < 3:
        print("none")
    else:
        # Get all parameters (starting from index 1)
        params = sys.argv[1:]
        # Print them in reverse order using [::-1]
        for p in params[::-1]:
            print(p)

if __name__ == "__main__":
    main()
