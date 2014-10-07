# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math


# initialize global variables used in your code here
num_range = 100
guesses_left = 7


# helper function to start and restart the game
def new_game():
    global secret_number
    global guesses_left
    print "New game. Range is from 0 to %s" % num_range
    secret_number = random.randrange(0, num_range)
    guesses_left = guess_calc(num_range)
    print "Number of remaining guesses is %s\n" % guesses_left


# calculate max number of guesses using math.log and math.ceil
def guess_calc(high):
    x = math.log(high+1)/math.log(2)
    n = math.ceil(x)
    return int(n)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    guess = int(guess)
    global guesses_left

    if guesses_left > 0:
        print "Guess was %s" % guess
        if guess > secret_number:
            print "Lower!\n"
            guesses_left -= 1
            print "Number of remaining guesses is %s" % guesses_left
        elif guess < secret_number:
            print "Higher!\n"
            guesses_left -= 1
            print "Number of remaining guesses is %s" % guesses_left
        elif guess == secret_number:
            print "Correct! Starting a new game.\n"
            new_game()
    else:
        print "Sorry, you have no more guesses. Starting a new game!"
        new_game()

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
label = f.add_label('Button Label')
label.set_text('Click on a button to start a new game')

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game
new_game()
