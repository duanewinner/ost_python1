#!/usr/local/bin/python3

def print_list(lst, rev=False):
    """ prints the content of a list. """
    if rev:
        lst = reversed(lst)
    for i in lst:
        print(i)

print_list(['Printing', 'a', 'list'])
print()
print_list(['Printing', 'a', 'reversed', 'list'], 1)
print()
print_list(lst=['A', 'list', 'with', 'specified', 'arguments'], rev=0)
