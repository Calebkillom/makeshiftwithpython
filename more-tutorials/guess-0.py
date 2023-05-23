#!/usr/bin/python3
# from Derek Banas youtube tutorial, creating a guessing game, in which a user
# chooses a number between 1 and 10.
# It should guess a number between 1 and 10
# if not correct it is going to ask again
# if guessed correctly, you find the number.


# store the correctnumber in a variable
correct_number = 9
# have a condition that prompts the user for input and store in a variable
while True:
    guessed_numb = int(input("Guess a number between 1 and 10: "))
    # don't include a break statement so it keeps prompting

    # compare it with the correct number and return the correctnumber
    if(correct_number == guessed_numb):
        print(correct_number)
        print("Congratulations, you won the game")
        break;
