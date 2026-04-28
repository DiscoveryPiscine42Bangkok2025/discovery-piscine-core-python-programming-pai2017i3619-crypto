#!/usr/bin/env python3

def famous_births(persons):
    # Sort the dictionary values based on the 'date_of_birth' key
    # persons.values() gives us the inner dictionaries
    sorted_persons = sorted(persons.values(), key=lambda x: x['date_of_birth'])
    
    # Iterate through the sorted list and print
    for person in sorted_persons:
        name = person['name']
        year = person['date_of_birth']
        print(f"{name} is a great scientist born in {year}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    
    famous_births(women_scientists)
