#!/usr/local/bin/python3
"""Accepts a string from user input and will capitalize, title-ize, upper/lower-case the string based on user choice."""

import sys

def c_text(text):
    """Capitalize the first character of the first word"""
    print(text.capitalize())

def t_text(text):
    """First Characters Of All Words Capilized"""
    print(text.title())

def u_text(text):
    """CAPITALIZE ALL TEXT"""
    print(text.upper())

def l_text(text):
    """convert all characters to lower case in text"""
    print(text.lower())

def exit(text):
    """Quit the program"""
    print("Goodbye.")
    sys.exit()


if __name__ == "__main__":
    case = {
        "capitalize": c_text,
        "title": t_text,
        "upper": u_text,
        "lower": l_text,
        "exit": exit
    }

    options = case.keys()
    prompt = "Enter a function name ({0}): ".format(", ".join(options))

    while True:
        inp = input(prompt)
        option = case.get(inp, None)
        if option:
            if inp != "exit":
                option(input("Enter a string: "))
            else:
                option("")
        else:
            print("Please enter a valid option.")
            
