print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor cmprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------"
print poem
print "-------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# original, redoing to show that the variables in the function are temp
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates

# this shows that the returned variables are temporary
def secret_formula(started):
    what = started * 500
    does = what / 1000
    this = does / 100
    return what, does, this

# sets the start_point variable so we have an argument for when
# we call the function above    
start_point = 10000
# this sets the variables that are returned from the secret_formula function
# remember that inside the function, the variable is temporary
# when you return it, then it can be assigned to a variable for later
beans, jars, crates = secret_formula(start_point)
madeup, variables, whatever = secret_formula(start_point)

print "madeup is %s, variables is %s, whatever is %s" % (madeup, variables, whatever)
# outputs the following
# madeup is 5000000, variables is 5000, whatever is 50

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# outputs with the following:
# Let's practice everything.
# You'd need to know 'bout escapes with \ that do 
#  newlines and 	 tabs.
# -------------------
# 
# 	The lovely world
# with logic so firmly planted
# cannot discern 
#  the needs of love
# nor cmprehend passion from intuition
# and requires an explanation
# 
# 		where there is none.
# 
# -------------------
# This should be five: 5
# With a starting point of: 10000
# We'd have 5000000 beans, 5000 jars, and 50 crates.
# We can also do that this way:
# We'd have 500000 beans, 500 jars, and 5 crates.