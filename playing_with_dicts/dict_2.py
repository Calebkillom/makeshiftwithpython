#!/usr/bin/python3
# continued tutorials on dictionaries and how to work with them
# this example borrows from DERRICK BANAS
# Youtube Tutorial on Recursive Functions and Dictionaries

calebDict = {"fname": "Caleb", "lname": "Kilonzi", "address": "Nairobi City"}

print("My name is ", calebDict["fname"])

# changing the value of a dictionary
calebDict["address"] = "Kisumu City"
print(calebDict)

# Adding the new key-value pair
calebDict["country"] = "Kenya"
print(calebDict)

# Checking if a key exists
print("Is there a city: ", "city" in calebDict)

# we can also get a list of values as well as our Keys
print(calebDict.values())
print(calebDict.keys())

# using the for loop to get both the keys and the values
for key, value in calebDict.items():
    print(key, value)
