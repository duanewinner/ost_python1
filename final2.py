#!/usr/local/bin/python3
""" Reads a text file as an argument when program is executed,
calculates the length of each word (without punctuation), and
prints table of word counts for each length encountered in text.
"""

import math
import os
import string
import sys


def read_textfile_as_param():
    """ Function to open a file as an argument when launching program.
    Capture common errors and exit with error code of 1,
    printing friendly messages.
    """
    
    try:
        filename = sys.argv[1]
        try:
            openfile = open(filename, 'r')
            if os.stat(filename)[6] == 0:
                print("\nFile \"{0}\" is has no content".format(filename))
                print("Nothing to be done, exiting...\n")
                sys.exit(1)                
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
        print("\nUsage: ./final2.py [path-to/]<filename>\n")
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

def comma_int(number):
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

def histogram_function(count, y_scale=5):
    """ Calculate Y-axis based on maximum count, divided into quads,
    with 5 tics per quad.
    """
    y_div = 4
    y_tic = 5

    """ Determine y-axis numbering and divisions, based on y_scale """
    maxcount=max(count.values())
    y = math.ceil(maxcount / y_div)
    while y % y_scale > 0:
        y+=1
    y_tic = int(y / y_tic)

    """ Create the histogram bins """
    bins = {}
    for i in range(64):
        bins[i]=[]

    """ Calculate adequate left margin
        to accomdate largest size number
    """
    left_margin=(len(comma_int(y * y_div)))

    # build x-axis lines
    x_scale = 4 # (Default for word lengths 16 or less)
    if max(count) > 16: 
        x_scale = 2
    if max(count) > 32:
        x_scale = 1

    x_int = ""
    for i in range(16):
        x_int += str("{0:4}".format(int(((i + 1) * 4 ) / x_scale)))
    x_axis = "{0:>{2}} -+{1}".format("0", "---+" * 16, left_margin) + "\n" +\
        "{0:>{1}}  |{2}".format(" ", left_margin, x_int)
    """ Create histogram as string object
    """
    histogram=""
    # start at top of y-axis, building from left to right
    for row in reversed(range(y_tic, y * y_div + 1, y_tic)):
        tic = " "
        tic_label = ""
        if row % y == 0:
            tic = "-"
            tic_label = comma_int(row)
        fill=""
        for wlen in range(1,65):
            fill += " " * (x_scale - 1 )
            if wlen in count and (count[wlen]) >= (row - y_tic + 1):
                fill += "*"
            else:
                fill += " "
        histogram += "{0:>{1}} {2}|{3}{4}".format(tic_label, left_margin, tic, fill[:64], "\n")

    histogram += x_axis

    """ Exclude words over 64 chars
        (NOTE: According to Wikipedia, the longest word in
        a major dictionary is 45 characters).
    """
    over64=0
    for wlen in count:
        if wlen > 64:
            over64 += count[wlen]
    # Footnote to count words over 64 which are excluded from historgram.
    if over64 > 0:
        pl = ""
        if over64 > 1:
            pl = "s"
        histogram += "\n\n(" + str(over64) + " word" + pl + " exceeded 64 characters.)\n"
              
    return histogram


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
        print(fmt.format(i, comma_int(count[i])), "\n", sepline, sep="")

    print("\n", histogram_function(count), sep="")

