'''
Created on Oct 16, 2013

@author: Tania
'''
# Rock-paper-scissors-lizard-Spock template


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
    number = num 
    if num == 0:
        print 'rock'
    elif num == 1:
        print 'Spock'
    elif num == 2:
        print 'paper'
    elif num == 3:
        print 'lizard'
    else num == 4:
        print 'scissors'
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


