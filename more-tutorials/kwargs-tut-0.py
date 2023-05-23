#!/usr/bin/python3
# simple tutorial on how **kwargs is used

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")
