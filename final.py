#!/usr/local/bin/python3
""" Reads a text file as an argument when program is executed,
calculates the length of each word (without punctuation), and
prints table of word counts for each length encountered in text.
"""

import sys
import string

def read_textfile_as_param():
    """ Function to open a file as an argument when launching program.
    Capture common errors and exit with error code of 1,
    printing friendly messages.
    """
    
    try:
        filename = sys.argv[1]
        try:
            openfile = open(filename, 'r')
            try:
                return openfile.read()
            except UnicodeDecodeError:
                print("\nFile \"{0}\" is not a text file.".format(filename))
                print("Cannot read, exiting...\n")
                sys.exit(1)
        except FileNotFoundError:
            print("\nFile \"{0}\" could not be found.".format(filename))
            print("Please provide a valid [path-to/]<filename>\n")
            sys.exit(1)
        except PermissionError:
            print("\nPermission denied trying to read file \"{0}\".".\
                  format(filename))
            print("(Try running with sudo).\nExiting...\n")
            exit(1)
    except IndexError:
        print("\nUsage: ./final.py [path-to/]<filename>\n")
        sys.exit(1)

    
def nopunc_len(word):
    """ Function to return length of word after all punctuation is removed.
    Do not return a value if no characters remain after removing punctuation.
    (Example: single ampersand, "&")
    """
    for punc in string.punctuation:
        word = word.replace(punc, "")
    if len(word) > 0:
        return len(word)

def int_comma_format(number):
    """ Function to accept an integer, and format the number
    with commas for better readability.
    """
    snumber = str(number)
    if len(snumber) < 4:
        return snumber
    nnumber = ""
    while len(snumber) > 0:
        nnumber = snumber[-3:]+nnumber
        snumber = snumber[:-3]
        if snumber:
            nnumber=","+nnumber
    return nnumber



if __name__ == "__main__":
    count={}
    for word in read_textfile_as_param().split():
        wl = nopunc_len(word)
        if wl:
            if wl in count.keys():
                count[wl] += 1
            else:
                count[wl] = 1
    sepline="-"*26
    fmt = "| {0:<7}| {1:<13} |"
    print(sepline, "\n", fmt.format("Length", "Count"), "\n", sepline, sep="")
    for i in sorted(count.keys()):
        print(fmt.format(i, int_comma_format(count[i])), "\n", sepline, sep="")

