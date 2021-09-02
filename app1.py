import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[word]
    else:
        return "The word does not exist. Please double check it."    

word = input("Enter word: ")
print(translate(word))    