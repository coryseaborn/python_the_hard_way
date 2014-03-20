# create cars variable, at 100
cars = 100
# create space in a car variable, at 4.0
space_in_a_car = 4.0
# create drivers in a car variable, at 30
drivers = 30
# passengers at 90
passengers = 90
# cars not driven, which comes out to 70
cars_not_driven = cars - drivers
# cars driven is equivalent to drivers, so 30
cars_driven = drivers
# carpool capacity, which comes out to 120.0
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car, comes out to 3
average_passengers_per_car = passengers / cars_driven

# time to print everything to the terminal when run
# this comes to say 'There are 100 cars available.'
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

# ends up being the following output:
# There are 100 cars available.
# There are only 30 drivers available.
# There will be 70 empty cars today.
# We can transport 120.0 people today.
# We have 90 to carpool today.
# we need to put about 3 in each car.