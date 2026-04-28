#!/usr/bin/env python3

def average(class_dict):
    # Get all the scores from the dictionary values
    scores = class_dict.values()
    
    # Calculate average: total sum divided by number of students
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == "__main__":
    # Test data from the subject
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    
    print(f"Average for class 3B: {average(class_3B)}")
    print(f"Average for class 3C: {average(class_3C)}")
