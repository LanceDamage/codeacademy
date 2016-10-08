#this is going to be a dice game
#the script will randomly roll the dice
#then sum the dice roll, let the user pick
#a number, then compare the the two.
#to win, the user's guess needs to be bigger
#than the sum of the dice. Why a user wouldn't
#pick 12 every time, I don't know. 

#let's start by importing a module that will
#generate the random dice roll.
from random import randint

#next, well need sleep to simulate roll
from time import sleep

#now that we have some tools, lets move on
#let's prompt a user for a guess in a function
def get_user_guess():
    user_guess = int(raw_input("Guess a number: "))
    return user_guess

#Next, we will build the roll dice part
def roll_dice(number_of_sides): 
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_value = number_of_sides * 2
    print "Max value is " + str(max_value)
    sleep(1)
    user_guess = get_user_guess()
    #now let's limit the users guess to within defined parameters
    if user_guess > max_value:
        print "Invalid guess, too large"
        return
    else:
        print "rolling..."
        sleep(2)
        print "The first roll is %d" % (first_roll)
        sleep(1)
        print "and rolling second dice..."
        sleep(2)
        total_roll = first_roll + second_roll
        print "Result..."
        sleep(1)
        print str(total_roll) + "!"
        sleep(1)
        if user_guess > total_roll:
            print "You won!"
            return
        else:
            print "...better luck next time..."
            return
 
roll_dice(6)       
         
