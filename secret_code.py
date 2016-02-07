#!/usr/local/bin/python3

e_text = ""

c_text = input("Enter a line of text to encipher: ")
for char in reversed(c_text):
    e_text += (chr(ord(char)+1))

print(e_text)



