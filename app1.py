import json

# Load a .json file
data = json.load(open("data.json"))

# Search a word into the .json file
def translate(w):
    w = w.lower() # Lower case the entered text
    if w in data: # Ask if the word is into the data
        return data[w]
    else:
        return "The word does not exist. Please double check it."    

word = input("Enter word: ")
print(translate(word))