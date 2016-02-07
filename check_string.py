#!/usr/local/bin/python3

ustring = input("Please enter an upper-case string ending with a period: ")

if not ustring.isupper():
    print("Input is not all upper case.")
if not ustring.endswith("."):
    print("Input does not end with a period.")
elif ustring.isupper():
    print("Input meets both requirements")



    


