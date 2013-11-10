'''
Created on Oct 24, 2013

@author: Tania
'''
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialize global variables used in your code

num_range = 0
secret_number = 0
Maximum_guess = 0

# helper function to start and restart the game

def new_game(): 
    global secret_number, Maximum_guess
    secret_number = random.randint(1,100)
    if num_range <= 100:
        Maximim_guess == 7
        print "New game. Pick a number between 1 - 100"
    elif num_range <= 1000:
        Maximum_guess == 10
        print "New game. Pick a number between 1 - 1000"
    else:
        print "Number not within range, please choose a new number."
    
#    print "Maximum guesses allowed is" Maximum_guess

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
#    global num_range, Maximum_guess, secret_number 
    new_game() 
    

def range1000():
    # button that changes range to range [0,1000) and restarts
#    global num_range, Maximum_guess, 
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    guess = int(guess)
        print "Your guess was:" guess
    if guess < secret_number:
        print "Higher!"
    if guess is > secret_number:
        print "Lower!"
    if guess is == secret_number:
        print "Correct!"
    else:
        pass
        
    #print "New Game"
    #"Number of remaining guesses is"
    #"You ran out of guesses. The number was"
    # remove this when you add your code
        
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)


# register event handlers for control elements

frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Guess a number", get_input, 200)

# call new_game and start frame
frame.start
new_game()


# always remember to check your completed program against the grading rubric
#URL to keep track of my work in codeskulptor:http://www.codeskulptor.org/#user23_ReT3kya23l_5.py