#!/usr/local/bin/python3
#
# greeting.py
#
"""Take a first name and last name
from input statements and generate
a friendly greeting"""

firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
fullname = firstname + " " + lastname
print("Hello, " + fullname + ". Shall we play a game?")
