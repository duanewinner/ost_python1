#!/usr/local/bin/python3
#
# word_list.py
#
"""Read input from user and then print the input
as two lists: words with at least one upper-case character
followed by word with no upper-case characters"""

import string

uppers=[]
lowers=[]
#unique_words=[]
#wordlist=[]

user_sez=input("Input your text: ")

# Break text into list of words, seperated by spaces (split), after removing any leading or trailing whitespace (strip)
words=user_sez.strip().split()

# Simplified attempt 2. Does not include count logic.
for word in words:
    if word.islower():
        lowers.append(word)
    else:
        uppers.append(word)

for word in uppers+lowers:
    print(word)


    
##### First attempt:

# Cycle through each character in each word, adding the word to  a upper-case or lower-case list, 
# then append the two lists in order, uppers first.
#for word in words:
#    has_upper=False
#    for char in word:
#        if char in string.ascii_uppercase:
#            has_upper=True
#            break
#    if has_upper:
#        uppers.append(word)
#    else:
#        lowers.append(word)

# Cycle through the sorted list and print each word, only once each, but list occurrences
# if it appears more than once.
#for word in uppers+lowers:
#    if word not in unique_words:
#        unique_words.append(word)
#        if (uppers+lowers).count(word) > 1:
#            print(word, "(appears ",(uppers+lowers).count(word)," times.)")
#        else:
#            print(word)

# 
#for st in words:
#    print("{0} {1} {2}".format(st,'lower', st.islower() ))
#    print("{0} {1} {2}".format(st,'upper', st.isupper() ))



