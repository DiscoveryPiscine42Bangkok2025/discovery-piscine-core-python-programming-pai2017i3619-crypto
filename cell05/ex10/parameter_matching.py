#!/usr/bin/env python3
import sys

def main():
    # Rule: If number of parameters is different from 1, display none
    # (len is 2 because sys.argv[0] is the script name)
    if len(sys.argv) != 2:
        print("none")
    else:
        # Save the parameter passed in the terminal
        secret_word = sys.argv[1]
        
        # Prompt the user to enter a word
        user_guess = input("What was the parameter? ")
        
        # Compare them
        if user_guess == secret_word:
            print("Good job!")
        else:
            print("Nope, sorry...")

if __name__ == "__main__":
    main()
