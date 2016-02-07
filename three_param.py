#!/usr/local/bin/python3

def my_func(a, b="b was not entered", c="c was not entered"):
    print(a, b, c, sep='\n')

while True:
    i = input("Enter 3 parameters separated by commas (or Enter to quit): ").split(",")
    if not i[0]:
        break
    y=[]
    for x in i:
        y.append(x.strip())
    my_func(*y[0:3])

print(my_func)



# First solution, produces correct results, but less elegant, and technically incorrect I think, based on the objective requirements:
"""
def my_func(a, b, c):
    print(a)
    if b:
        print(b)
    else:
        print("b was not entered")
    if c:
        print(c)
    else:
        print("c was not entered")



while True:
    print("Enter three parameters")
    i1 = input("Parameter 1: ")
    if not i1:
        break
    i2 = input("Parameter 2: ")
    i3 = input("Parameter 3: ")
    my_func(i1, i2, i3)

print(my_func)
"""


