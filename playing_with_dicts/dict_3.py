#!/usr/bin/python3
# continued practise on the previous tutorial

# getting values associated with Key if not, we throw in a default
calebDict = {"fname": "Caleb", "lname": "Kilonzi", "address": "Nairobi City"}
print(calebDict.get("car", "doesn't have a car"))

# Deleting a Key-Value pair
del calebDict["fname"]
print(calebDict)

# Looping through our dictionary Keys
for i in calebDict:
    print(i)

# deleting all the data
calebDict.clear()
print(calebDict)
