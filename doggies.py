#!/usr/local/bin/python3

"""Creates a catalog of dogs and their respective breed attribute, using python Classes and instances"""

class Dog:

        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def __str__(self):
            return "%s:%s" % (self.name, self.breed)
            
if __name__ == "__main__":

    dogs = []
    sepline = "*"*40
    print("\n\n" + sepline + "\nCreate of catalog of dogs, with their first name and breed.\nHit <Enter> for the dog's name at any time to quit.\n" + sepline + "\n")
    
    while True:
        
        name = input("Dog's Name: ")
        if not name:
            break
        breed = input("Dog's Breed: ")
        dogs.append(Dog(name, breed))

        print("\nDOGS")
        for num, dog in enumerate(dogs):
            print(str(num) + ". " + str(dog))
        print(sepline+"\n\n")

