#!/usr/local/bin/python3
"""test understanding of classes and object"""

#Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
#Bind an empty list to a dogs variable.
#Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
#For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
#Each time around the loop, print the current dogs list (the name and breed of each dog).

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        """fun with printing"""
        return "     __\n(___()'';\n/,    /`  {0}: {1}\n\\\\\"--\\\\\n".format(self.name, self.breed)

if __name__ == "__main__":
    dogs=[]
    while True:
        name = input("Enter dog's name (return to exit):")
        if name:
            breed = input("Enter dog's breed:")
            dogs.append(Dog(name,breed))
            print("\nYour kennel:")
            for dog in dogs:
                print(dog)
        else:
            print("Goodbye!")
            break
