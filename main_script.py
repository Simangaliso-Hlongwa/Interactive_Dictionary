import json
from difflib import get_close_matches

def word(w):
    data = json.load(open("data.json", 'r'))
    w = w.lower() #converts input to lowercase since the data is in lower case
    if w in data:
        return data[w]

    elif w.title() in data: #if the user entered texas the program will still find the word
        return data[w.title()]

    elif w.upper() in data: #in case user enters an uppercase word
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0: #wanna check if the length of the list is greater than 0
        choice = input("did you mean %s instead? Enter yes or no: " % get_close_matches(w, data.keys())[0]) #%s string formatter that can store a value
        if choice == "yes":                                                                                       #[0] getting the first element of the list
            return data[(get_close_matches(w, data.keys())[0])]
        elif choice == "no":
            return "please double check the spelling"
        else:
            return "we did not understand your entry."

    else:
        return "this word does not exist. please double check it"

name = input("enter word you want to find: ")
output = (word(name))


if type(output) == list: #preventing the other string from being printed line for line
    for i in output:    #to print the definition as a string NOT as a list
        print(i)
else:
    print(output)
