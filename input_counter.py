#!/usr/local/bin/python3
"""Read words from user input, and track the order in which they were entered"""

import string

iset = set()
idict = dict()
lastlen = 0

while True:
    text = input("Enter text: ")
    if text:
        for punc in string.punctuation:
            text = text.replace(punc, "")
        for word in text.lower().split():
            iset.add(word)
            if len(iset) > len(idict):
                idict[word] = len(iset)
# The next three lines accomplish the same thing as the previous four lines but without the need for a set.
#            if word not in idict:
#                lastlen +=1
#                idict[word] = lastlen
#        for word in sorted(idict.keys()):
#            print(word,idict[word])
        for word, order in idict.items():
            print(word, order)
#        for word in idict:
#            print(word,idict[word])     
    else:
        print("Finished")
        break


