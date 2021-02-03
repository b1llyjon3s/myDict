import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./data.json"))



#retrieve the word from the dictionary and error handle.
def getWord(word):
    res = ''
    if word in data: 
        res = "\n".join(data[word]) + "\n"
        return res
    else:
        w = get_close_matches(word, data.keys())
        if w:
            selection = ''
            while(selection != 'y' or selection != 'y' or selection != w[0]):
                selection = input("Did you mean '" + w[0] +"'? Enter 'Y' if yes and 'N' if no: ").lower()
                if(selection == 'y' or selection == w[0]):
                    res = "\n".join(data[w[0]]) + "\n"
                    return res
                elif(selection == 'n'):
                    return "Word doesnt not exist.\n"
            
        else:
            return "Word doesnt not exist.\n"


while(True):
    word = input("Enter a word: ")
    print(getWord(word.lower()))
