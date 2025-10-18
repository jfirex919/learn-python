# Guess a number
import random

print("I am thinking of a number between 1 and 20.")
guess_counter = 1
random_number = random.randint(1, 20)
while True:

    input_number = int(input("Take a guess."))
    if input_number == random_number:
        break
    elif input_number > random_number:
        print("Sorry, your number is too high.")
    elif input_number < random_number:
        print("Sorry, your number is too low.")

    guess_counter+=1

print(f"Good job! You got it in {guess_counter} guesses!")
