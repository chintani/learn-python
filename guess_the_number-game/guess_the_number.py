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
num_range = 100
secret_number = 0

# helper function to start and restart the game
def new_game():
    global num_range, secret_number
    secret_number = random.randint(0,100)
    print "New game. Pick a number between 0 - 100"
    print "Number of remaining guesses is", #Maximum_guess
    print "\n"
    # if num_range <= 100:
        
    # elif num_range <= 1000:
    #     Maximum_guess = 10
    #     print "New game. Pick a number between 1 - 1000"
    #     print "Number of remaining guesses is"
    # else:
    #      print "Number not within range, please choose a new number."
    
# define event handlers for control panel

def range100():
# button that changes range to range [0,100) and restarts
    global secret_number
    secret_number = random.randint(0, 100)
    if input_guess < secret_number:
        print "Higher"
    elif input_guess > secret_number:
        print "Lower"
    elif input_guess == secret_number:
        print "Correct!"
    else:
        print "Please choose a number between 0 - 100"
        new_game()
        
def range1000():
# button that changes range to range [0,1000) and restarts
    global secret_number
    secret_number = random.randint(0, 1000)
    if input_guess < secret_number:
        print "Higher"
    elif input_guess > secret_number:
        print "Lower"
    elif input_guess == secret_number:
        print "Correct!"
    else:
        print "Please choose a number between 0 - 1000"
        new_game()
    
def input_guess(guess):
# main game logic goes here    
    global num_range
    num_range = int(guess)
    print "Your guess was", num_range
    print "Number of remaining guesses is"
    if num_range < secret_number:
        print "Higher!"
    elif num_range > secret_number:
        print "Lower!"
    elif num_range == secret_number:
        print "Correct!"
    else:
        new_game()
    print "\n"
    
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)


# register event handlers for control elements

frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Guess a number", input_guess, 200)

# call new_game and start frame
new_game()
frame.start


# always remember to check your completed program against the grading rubric
#URL to keep track of my work in codeskulptor:http://www.codeskulptor.org/#user28_m46cME57C0_9.py