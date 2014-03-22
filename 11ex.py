print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# this is split into two lines to keep it less than 80 characters per line, which python programmers prefer so that it doesn't do what this comment does
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# output shows the following
# How old are you? 26
# How tall are you? 5'11"
# How much do you weigh? 165
# So, you're '26' old, '5\'11"' tall and '165' heavy.

print "test the raw input with a prompt",
raw_test = raw_input('--> ')

print raw_test

# output shows the following, user input is requested after the arrow
# test the raw input with a prompt --> arrows!
# arrows!

raw_test2 = raw_input('Does this accomplish the same thing? ')
print raw_test2

# output shows the following
# Does this accomplish the same thing? I think so?
# I think so?