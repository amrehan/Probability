import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))

word = input().lower()

def dictionary(w):
    """
    This function returns the description(s), if any.
    """

    if w in data:
        return data[w]
    else:

        """
        get_close_matches retuns the word in case of striking
        similarity between the user input and a word in dictionary
        generally a typo.
        """

        val = get_close_matches(word, data.keys())[0]
        if val in data:
            user_input = input("Do you mean {} ? [Y/N] ".format(val))
            if user_input.lower() == 'y':
                return data[val]
            else:
                print("Didn't know about it.")


for i in dictionary(word):
    print("-", i)



