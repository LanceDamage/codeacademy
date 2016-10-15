"""This will be a rock, paper, scissors game. I am going to
prompt the user to select one of the three, then the computer
will randomly select one of the three. The script will compare the two and pick the winner!"""
#Let's gather the right materials
from random import randint
from time import sleep
# Next, we'll create the constant variables
options = ["R","P","S"]
USER_LOST = "Terrible, F!"
USER_WON = "You won!"
#We need to create a function that decides who wins
def decide_winner(user_choice, computer_choice):
    print "You selected: %s" % user_choice
    sleep(1)
    print "Computer selected: %s" % computer_choice
    sleep(1)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "It's a draw!"
    elif user_choice_index == 0 and computer_choice_index == 2:
        print USER_WON
    elif user_choice_index == 1 and computer_choice_index == 0:
        print USER_WON
    elif user_choice_index == 2 and computer_choice_index == 1:
        print USER_WON
    elif user_choice_index > 2:
        print "Invalid entry"
        return
    else:
        print USER_LOST
  # We also need a function that starts the game\
def play_RPS():
    print "Paper, Rock, Scissors"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
    sleep(1)
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,len(options)-1)]
    decide_winner(user_choice,computer_choice)
#now let's play
play_RPS()
