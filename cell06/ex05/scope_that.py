#!/usr/bin/env python3

# Method that adds 1 to the parameter
def add_one(n):
    n = n + 1

def main():
    # Initialize a variable
    my_var = 42
    
    # Display it first
    print(f"Before method: {my_var}")
    
    # Call the method
    add_one(my_var)
    
    # Display it again
    print(f"After method: {my_var}")

if __name__ == "__main__":
    main()
