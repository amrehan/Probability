#problem statement: 
#Given a phone number, return all valid words that can be created using that phone number.

#For instance, given the phone number 364
#we can construct the words ['dog', 'fog'].



lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeString(phone):
    input_list = [int(c) for c in phone]
    input_string = ""
    output = []
    for i in input_list:
        l = lettersMaps[i]
        for a in l:
            input_string += a
    return input_string

def makeWords(phone):
    input_string = makeString(phone)
    output = []
    for i in validWords:
        word = ""
        for k in i:
            if k in input_string:
                word += k
            output.append(word)
    final = []
    for c in output:
        if c in validWords:
            final.append(c)
            
    return final

print(makeWords('364'))
# ['dog', 'fog']
