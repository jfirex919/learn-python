# Guess a number
import random

print("ROCK, PAPER, SCISSORS")
win = 0
lose = 0
tie = 0
"""
same = tie
r win scisor
r lost paper
scisor win paper

"""

while True:
    print(f"{str(win)} Wins, {str(lose)} Losses, {str(tie)} Ties")
    player_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    computer_move = random.choice(["r","p", "s"])
    print(f"computer is {computer_move}.")
    if player_move == "q":
        print("Thank you for playing!")
        break
    if player_move == computer_move:
        print("It's a tie!")
        tie =tie+1
    if player_move == "r":
        if computer_move == "p":
            lose=lose+1
            print("You lose!")
        if computer_move == "s":
            win=win+1
            print("You win!")
    if player_move == "p":
        if computer_move == "s":
            lose=lose+1
            print("You lose!")
        if computer_move == "r":
            win=win+1
            print("You win!")
    if player_move == "s":
        if computer_move == "r":
            lose=lose+1
            print("You lose!")
        if computer_move == "p":
            win=win+1
            print("You win!")







