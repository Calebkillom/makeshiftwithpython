#!/usr/bin/python3
# more exception handling

try:
    alist = [1,2,3]
    print(alist[3])
except IndexError:
    print("sorry that index doesn't exist")
except:
    print("An unknown error occured")
