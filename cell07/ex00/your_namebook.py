#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    # Iterate through the dictionary items (key = first, value = last)
    for first, last in persons.items():
        # Capitalize both and join with a space
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

if __name__ == "__main__":
    # Test dictionary from the subject
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier",
        "NUCLEAR":"ICBM",
        "DEFCON":"ONE"
    }
    
    print(array_of_names(persons))
