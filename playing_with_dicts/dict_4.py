#!/usr/bin/python3
# more tutorials on dictionaries and their usage in python
# Illustration on How we are able to create lists that are going to be able to
# hold dictionaries.

employees = []

fname, lname = input("Enter employee Name: ").split()

employees.append({'fname': fname, 'lname': lname})

print(employees)
