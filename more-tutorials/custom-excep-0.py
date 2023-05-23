#!/usr/bin/python3
# Creating and experimenting with custom exceptions.

class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name: ")

    if any (char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("Your Dog's name can't contain a number")
