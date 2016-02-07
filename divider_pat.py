#!/usr/local/bin/python3

while True:

    denominator_str = input("Provide an integer: ")
    if not denominator_str:
        break

    try:
        print(10/int(denominator_str))

    except ValueError:
        print("Please enter an integer")
        
    except ZeroDivisionError:
        print("Division by zero!")

print('Bye!')
