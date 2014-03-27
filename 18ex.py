# this one is like your scripts with argv.
# note that you give an asterisk arg, which is a lot like
# argv but for functions and has to go inside ().
# this 'unpacks' args, which we can just set in the (),
# which is demonstrated in print_two_again
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothin'."
    
print_two("Cory","Seaborn")
print_two_again("Cory","Seaborn")
print_one("First!")
print_none()

# outputs the following
# arg1: 'Cory', arg2: 'Seaborn'
# arg1: 'Cory', arg2: 'Seaborn'
# arg1: 'First!'
# I got nothin'.

# Function checklist:
# 1) Did you start your function definition with 'def'?
# 2) Does your function name have only characters and _ (underscore) characters?
# 3) Did you put an open parenthesis ( right after the function name?
# 4) Did you put your arguments after the parenthisis ( separated by commas?
# 5) Did you make each argument unique (meaning no diplicate names)?
# 6) Did you put a close parenthesis and a colon ): after the arguments?
# 7) Did you indent all lines of code you want in the function four spaces? No more, no less
# 8) Did you "end" your function by going back to writing with no indent (dedenting we call it)?

# When you run ("use" or "call") a function, check these things:
# 1) Did you call/use/run this function by typing its name?
# 2) Did you put the ( character after the name to run it?
# 3) Did you put the values you want into the parenthesis separated by commas?
# 4) Did you end the function call with a ) character?