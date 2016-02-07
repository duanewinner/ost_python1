#!/usr/local/bin/python3

""" Inputter.py: This program will accept user input until the Enter key pressed, then will save the content so far, and exit the program.
It will print the text when resumed."""

my_file = "text.txt"

try:
    f = open(my_file, 'r')
    text = f.read()
    if text:
        print("The story so far...\n")
        print(text)
except IOError:
    f = open(my_file, 'w')
    f.close()

while True:
    f = open(my_file, 'a+')
    text = input("Enter text (\"\\n\" for a newline, \"Enter\" to quit): ")
    if text:
        if text == '\\n':
            f.write('\n')
        else:
            f.write(text)
        f.seek(0)
        print(f.read())
    else:
        f.close()
        break

