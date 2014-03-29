# importing the argv module
from sys import argv

# variables grabbed by the arguments supplied
script, input_file = argv

# defines a function, print_all, which takes a
# variable and calls the read function on the variable
def print_all(f):
    print f.read()
    
# defines a function, rewind, which takes a variable
# and uses the seek function which moves the pointer
# to the byte of the file specified, in this case
# it goes back to the beginning (byte 0)
def rewind(f):
    f.seek(0)
    
# defines a function, print_a_line, which takes two
# variables. the first just gets called, the second
# specifies what line of the variable to read
# the , at the end removes the \n returned by the
# readline function
def print_a_line(line_count,f):
    print line_count, f.readline(),
    
# sets the current_file variable, and uses the open
# function on the input_file which is gathered from
# argv above by the user running the script
current_file = open(input_file)

print "First let's print the whole file:\n"
# this uses the print_all function which reads the
# variable. the variable current_file opens the
# input_file which is supplied in argv
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# this uses the rewind function which uses the seek
# function against the variable supplied, which is
# current_file. again, current_file just opens the
# input_file supplied in argv
rewind(current_file)

print "Let's print three lines:"
# this sets the current_line variable to a decimal, 1
current_line = 1
# this calls the print_a_line function, which takes
# two variables. the first current_line, is just printed
# which the second has the readline function called.
# this ends up being the first line
print_a_line(current_line, current_file)

# this does the same as above but adds a 1 to the 
# current_line variable, making it line 2
# this overwrites the current_line variable
#current_line = current_line + 1
# rewriting in shorthand notation
current_line += 1
print_a_line(current_line, current_file)

# adds another 1 to the current_line, making it line 3
#current_line = current_line +1
# rewriting in shorthand notation
current_line += 1
print_a_line(current_line, current_file)

# outputs the following before the comma in the print_a_line:
# First let's print the whole file:
# 
# this is my example file
# it's not full or anything
# at all
# just a bunch of jibbirish
# that we'll be reading
# and rewinding
# and grabbing lines 'n stuff
# 
# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 this is my example file
# 
# 2 it's not full or anything
# 
# 3 at all
#
# outputs the following after the comma in the print_a_line:
# First let's print the whole file:
# 
# this is my example file
# it's not full or anything
# at all
# just a bunch of jibbirish
# that we'll be reading
# and rewinding
# and grabbing lines 'n stuff
# 
# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 this is my example file
# 2 it's not full or anything
# 3 at all
#
#
# += adds another value with the variable's value and 
# assigns the new value to the variable.
#
# -=, *=, /= does similar for sub, mult, and div
# in otherwords, x = x + y is the same as x += y.