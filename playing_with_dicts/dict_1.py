#!/usr/bin/python3
# modifying or adding values inside a dictionary

my_dict = {'name' : 'caleb', 'occupation' : 'unemployed', 'status' : 'hopeful'}

print(my_dict['name'])
print(my_dict['occupation'])
print(my_dict['status'])

# modifying the value associated with the age key
my_dict['status'] = 'intern'
print(my_dict['status'])

# Adding a new key-value pair
my_dict['gender'] = 'male'
print(my_dict['gender'])
