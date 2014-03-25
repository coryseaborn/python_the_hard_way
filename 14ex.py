from sys import argv

script, user_name, age = argv
# prompt = '> '
prompt = 'YOU SUCK: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Too bad you're only %r years old, that's
too young to understand python.
""" % (likes, lives, computer, age)

# outputs with the following
# Hi cory, I'm the 14ex.py script.
# I'd like to ask you a few questions.
# Do you like me cory?
# > no
# Where do you live cory?
# > seattle
# What kind of computer do you have?
# > mac
# 
# Alright, so you said 'no' about liking me.
# You live in 'seattle'. Not sure where that is.
# And you have a 'mac' computer. Nice.