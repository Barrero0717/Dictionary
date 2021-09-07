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
    elif len(get_close_matches(w, data.keys())) > 0: 
        return "Did you mean " + get_close_matches(w, data.keys())[0] +" instead?"
    else:
        return "The word does not exist. Please double check it."    

word = input("Enter word: ")
print(translate(word))