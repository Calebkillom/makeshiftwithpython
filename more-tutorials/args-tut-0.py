#!/usr/bin/python3
# examples to help understand the *args concept

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15
