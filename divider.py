#!/usr/local/bin/python3
""" Example of exception handling -- divide 10 by some integer provided by the user, and trap errors """

numerator = 10

def divide(divisor):
    try:
        divisor=int(divisor)
        try:
            return numerator/divisor
        except ZeroDivisionError:
            print("Division by zero (0) is illegal!")
    except ValueError:
            print("Only integers are accepted.")
    except:
        print("Something went wrong!")
        raise


print("Dividing 10 by an integer")

while True:
    try:
        divisor = input("Please provide an integer: ")
    except (EOFError, KeyboardInterrupt):
        print("\nHit <Enter> to exit.")
        continue
    if not divisor:
        print("Goodbye.")
        break
    try:
        quotient=(divide(divisor))
        if quotient:
            print(quotient)
    except Exception as msg:
        print("Problem: {0}".format(msg))
        print("Please email this error message to support@python.newbie")

        
