import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[x.title()]
    elif x.upper() in data:  # in case user enters words like USA or NATO
        return data[x.upper()]
    elif len(get_close_matches(x, data.keys())) > 0:
        answer = input("Did you mean %s instead? Type 'Y' for yes or 'N' for no: " %
                       get_close_matches(x, data.keys())[0])
        if answer == "Y":
            return data[get_close_matches(x, data.keys())[0]]
        elif answer == "N":
            print("Word entered does not exist, please try again!")
    else:
        return "Entered word does not exist. Please try again!"


word = input("Enter the word: ")
output = translate(word)

# if type(output) == list:
for meanings in output:
    print(meanings)
# else:
#     print(output)


# git remote add origin https://github.com/fardin019/English-Dictionary.git
# git push -u origin master