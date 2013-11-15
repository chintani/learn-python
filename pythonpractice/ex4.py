cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# The lines above In programming are variables which are nothing more 
# than a name for something so you can use the name rather than the something as you code.
print "There are", cars, "cars available." # commas will not print and the cars will be replaced with 100
print "There are only", drivers, "drivers available"
print "There we be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 
