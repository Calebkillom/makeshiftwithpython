#!/usr/bin/python3
# program illustrating how to use finally and else while
# exception handling

num1, num2 = input("Enter two values to divide: ").split()

try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {} ".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")

# if exception does not occur
else:
    print("You didn't raise an exception")

# If there is certain code that you'll always want to execute whether
# an exception is triggered or not.
finally:
    print("I execute no matter what.")
