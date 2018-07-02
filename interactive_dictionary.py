import json
from difflib import SequenceMatcher
from difflib import get_close_matches
# library for comparing text


def load_data(filename):
    # input: name of the data file in str
    # output: data file in Python dictionary structure
    # note: utilizes json lib to import the json file

    data = json.load(open(filename))
    return data


def translate(data, word):
    # input: Python dictionary data to be searched; word that wants to know the definition of in str
    # output: definition of the word in list
    # note: considers small typos or capitalization errors, output optimized for better display

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 2:
        # probably shouldn't hardcode the numbers in conditional
            for counter in range(0,3):
                decision = input("\nDo you mean 1.%s 2.%s 3.%s ?\n (type the corresponding number in the field to choose, or N if none):" % (get_close_matches(word, data.keys())[0], get_close_matches(word, data.keys())[1], get_close_matches(word, data.keys())[2]))
                if decision == '1':
                    return data[get_close_matches(word, data.keys())[0]]
                elif decision == '2':
                    return data[get_close_matches(word, data.keys())[1]]
                elif decision == '3':
                    return data[get_close_matches(word, data.keys())[2]]
                elif decision == 'N':
                    return "\nSorry that you couldn't find your word, lets try a different word shall we."
                else:
                    display_num = 2-counter
                    print("\nInvalid choice, please try again, you have %i chances left" % display_num)
            return "Oopsies, someone can't follow instructions, lets try this again ..."
        elif len(get_close_matches(word, data.keys())) > 1:
            for counter in range(0,3):
                decision = input("\nDo you mean 1.%s 2.%s?\n (type the corresponding number in the field to choose, or N if none):" % (get_close_matches(word, data.keys())[0], get_close_matches(word, data.keys())[1]))
                if decision == '1':
                    return data[get_close_matches(word, data.keys())[0]]
                elif decision == '2':
                    return data[get_close_matches(word, data.keys())[1]]
                elif decision == 'N':
                    return "\nSorry that you couldn't find your word, lets try a different word shall we."
                else:
                    display_num = 2-counter
                    print("\nInvalid choice, please try again, you have %i chances left" % display_num)
            return "Oopsies, someone can't follow instructions, lets try this again ..."
        elif len(get_close_matches(word, data.keys())) > 0:
            for counter in range(0,3):
                decision = input("\nDo you mean %s?\n (type Y for yes, or N if none):" % get_close_matches(word, data.keys())[0])
                if decision == 'Y':
                    return data[get_close_matches(word, data.keys())[0]]
                elif decision == 'N':
                    return "\nSorry that you couldn't find your word, lets a different word shall we."
                else:
                    display_num = 2-counter
                    print("\nInvalid choice, please try again, you have %i chances left" % display_num)
            return "Oopsies, someone can't follow instructions, lets try this again ..."
        else:
            return "\nSuch word is not in ze dictionary, please try again"


data = load_data("data.json")
print("This is a work in progress. The function of this project is to get familiar with\nbasic Python library and syntax and practice using version \ncontrol Git with Github. Further developement aims to have a working database and GUI and web deployed")
while True:
    word = input("\nWhat word would you like to know more of? (type 0 to exit):")
    if word == '0':
        break
    translated = translate(data, word)
    if type(translated) == list:
        i = 0
        for definition in translated:
            i += 1
            print("\n%i. %s" % (i, definition))
    else:
        print(translated)

