'''
Created on Oct 16, 2013

@author: Tania
'''
# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    if number == 0: # convert number to a name using if/elif/else
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4: 
        name = "scissors"	
    else:
        print "Name not in this game!"
    
    return name 	# return the result!

    
def name_to_number(name):
    # fill in your code below
    
    if name == "rock": # convert name to number using if/elif/else
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Invalid number" 
    
    return number    # return the result!


def rpsls(name): 
    # fill in your code below

    name = name_to_number
    name_to_number == player_number    # convert name to player_number using name_to_number

    comp_number = random.range(5)    # compute random guess for comp_number using random.randrange()

    difference = (player_number - comp_number)% 5 # compute difference of player_number and comp_number modulo five

    if difference == 1 or 2:    # use if/elif/else to determine winner
        winner = "Player wins!"
    elif difference == 3 or 4:
        winner = "Computer wins!"
    elif difference == 0:
        winner = "Player and Computer tie"
    else:
        "Invalid turn"
        
    
    comp_number == number_to_name    # convert comp_number to name using number_to_name
    
    print "Player chooses" player_number	# print results
    print "Computer chooses" comp_number
    print winner

    
# test your code
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric
###################################################
# Test calls to name_to_number()
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)

###################################################
# Test calls to name_to_number()
#print name_to_number("rock")
#print name_to_number("Spock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors")