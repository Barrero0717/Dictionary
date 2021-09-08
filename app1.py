import json
from difflib import get_close_matches

"""
difflib: Helpers for computing deltas
This module provides classes and functions for comparing sequences. 

get_close_matches(word, possibilities, n=3, cutoff=0.6)
Return a list of the best “good enough” matches.

URL: https://docs.python.org/3/library/difflib.html
"""

# Load a .json file
data = json.load(open("data.json"))

# Search a word into the .json file
def translate(w):
    w = w.lower() # Lower case the entered text
    if w in data: # Ask if the word is into the data
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: # If the word is not there, it is evaluated if a similar word exists.
        question = input("Did you mean " + get_close_matches(w, data.keys())[0] +" instead? Enter Y if Yes, or N if not: " ) # User confirm the word
        if question == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif question == "N":
            return "The word does not exist. Please double check it." 
        else:
            return "We did not understand your entry."  
    else:
        return "The word does not exist. Please double check it."
 
word = input("Enter word: ")
print(translate(word))