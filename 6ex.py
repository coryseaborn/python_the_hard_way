# these just set your variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who know %s." % (binary, do_not)

# just prints the x and y variables, which are strings
print x
print y

# prints r, which stands for raw data, which is used for debugging
# also prints y as a string, hence the s
# take a look at the single tick '' which is used inside a string that has double quotes, mostly for just style points
print "I said: %r." % x
print "I also said: '%s'." % y

# first sets the hilarious variable as a bolean, as false
# Then it prints hilarious as it's raw value, which returns as false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# this then prints the joke_evaluation variable, which includes the raw format character, then tells it to use the hilarious variable
print joke_evaluation % hilarious

# this just sets the two variables as strings
w = "This is the left side of..."
e = "a string with a right side."

# and this adds them in together, which results in one string line
print w + e

# here's the output of it all - NOTE the "I said" and "I also said" use the single ' tick when putting a string inside of another string
# There are 10 types of people.
# Those who know binary and those who know don't.
# I said: 'There are 10 types of people.'.
# I also said: 'Those who know binary and those who know don't.'.
# Isn't that joke so funny?! False
# This is the left side of...a string with a right side.