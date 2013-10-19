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
    if number == 0:
        name_to_number = "rock"
    elif number == 1:
        name_to_number = 'Spock'
    elif number == 2:
        name_to_number = 'paper'
    elif number == 3:
        name_to_number = 'lizard'
    elif number == 4:
        name_to_number = 'scissors'
    else :
        print "Name not in this game!"
        
    return name_to_number

    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        number_to_name = 0
    elif name == "Spock":
        number_to_name = 1
    elif name == "paper":
        number_to_name = 2
    elif name == "lizard":
        number_to_name = 3
    elif name == "scissors":
        number_to_name = 4
    else :
        print "invalid Number"
    
    return number_to_name
    # convert name to number using if/elif/else
    # don't forget to return the result!


#def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric

print number_to_name(0)
print number_to_name(1)
print number_to_name(2)
print number_to_name(3)
print number_to_name(4)
print name_to_number("rock")
print name_to_number("Spock")
print name_to_number("paper")
print name_to_number("lizard")
print name_to_number("scissors")


