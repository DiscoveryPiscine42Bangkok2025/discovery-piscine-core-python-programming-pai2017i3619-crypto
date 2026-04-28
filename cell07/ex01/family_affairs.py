#!/usr/bin/env python3

def find_the_redheads(family):
    # filter() takes a function and an iterable.
    # We filter the keys (names) based on whether their value (hair color) is 'red'.
    redheads = filter(lambda name: family[name] == "red", family.keys())
    
    # filter returns an object, so we convert it to a list
    return list(redheads)

if __name__ == "__main__":
    # Test dictionary from the subject
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    
    print(find_the_redheads(dupont_family))
