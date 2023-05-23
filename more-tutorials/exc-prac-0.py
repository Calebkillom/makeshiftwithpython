#!/usr/bin/python3
# practising exception handling

while True:

    try:
        number = int(input("Please Enter a Number: "))
        print(number)
        break
    except ValueError:
        print("You didn't enter a number!")
        break
    except:
        print("An unkwon error occured!")
        break
print("Thank you for your coorporation.")
