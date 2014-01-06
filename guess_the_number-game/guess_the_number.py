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
maximum_guess = 7
wasPlayingRange100 = True

# helper function to start and restart the game
def new_game():
    if wasPlayingRange100:
        range100()
    else:
        range1000()
         
        
    
# define event handlers for control panel

def range100():
# button that changes range to range [0,100) and restarts
    global secret_number, wasPlayingRange100 
    secret_number = random.randint(0, 100)
    num_range = 100
    print secret_number
    print "New game. Pick a number between 0 -", num_range
    print "Number of guesses is", maximum_guess
    print "\n"
    wasPlayingRange100 = True
    #new_game()
    
def range1000():
# button that changes range to range [0,1000) and restarts
    global secret_number, num_range, maximum_guess, wasPlayingRange100
    secret_number = random.randint(0, 1000)
    num_range = 1000
    maximum_guess = 10
    print secret_number
    print "New game. Pick a number between 0 -", num_range
    print "Number of guesses is", maximum_guess
    print "\n"
    wasPlayingRange100 = False
    #new_game()

    
def input_guess(guess):
# main game logic goes here    
    global num_range, maximum_guess
    num_range = int(guess)
    maximum_guess = maximum_guess -1
    
    if num_range < secret_number:
        print "Your guess was", num_range
        print "Number of remaining guesses is", maximum_guess
        print "Higher!"
        print "\n"
        
    elif num_range > secret_number:
        print "Your guess was", num_range
        print "Number of remaining guesses is", maximum_guess
        print "Lower!"
        print "\n"
    elif num_range == secret_number:
        print "Your guess was", num_range
        print "Correct!"
        print "\n"
    if maximum_guess < 1:
        print "You have exceeded your guesses. The number was", secret_number
        print "\n"
        new_game()
        
   
    
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
#URL to keep track of my work in codeskulptor:http://www.codeskulptor.org/#user28_sXA11QPFN8_3.py