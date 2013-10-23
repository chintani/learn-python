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

    player_number = name_to_number(name)	# convert name to player_number using name_to_number

    comp_number = random.randrange(5)    # compute random guess for comp_number using random.randrange()

    difference = (player_number - comp_number)% 5 # compute difference of player_number and comp_number modulo five

    if difference == 1 or difference == 2:    # use if/elif/else to determine winner
        winner = "Player wins!"
    elif difference == 3 or difference == 4:
        winner = "Computer wins!"
    elif difference == 0:
        winner = "Player and computer tie!"
    else:
        "Invalid turn"
        
    
    computer_output = number_to_name(comp_number)    # convert comp_number to name using number_to_name
    
    print "Player chooses "  + name	# print results
    print "Computer chooses " + computer_output
    print winner
    print "\n"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# end of code