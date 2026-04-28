#!/usr/bin/env python3

# Define the method with a default parameter "noble stranger"
def greetings(name="noble stranger"):
    # Check if the name is actually a string
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        # If it's not a string (like the 42 in the example), show error
        print("Error! It was not a name.")

# Test calls as shown in the subject PDF
if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()   # Should use the default "noble stranger"
    greetings(42) # Should trigger the error message
