# this imports the argv module
# from sys allows you to import only argv
# as opposed to just saying import sys
# which would have all things in sys available
from sys import argv

# this sets the argv parameters which the user passes
script, filename = argv

# this sets the txt variable, and uses the open function against
# the filename passed by the argv function, which the user gives
txt = open(filename)

# this tells the user what filename they gave
# the second line uses the read method against the txt variable
# that second line outputs the entirety of 'filename'
print "Here is your file %r:" % filename
print txt.read()
# added a close function, which outputs with 'None'
print txt.close()

# this asks the user to type the filename
# the second line takes the user's input and creates file_again
print "Type the filename again:"
file_again = raw_input("> ")

# this creates the txt_again variable, which references the
# file_again variable created by the user's raw input above
txt_again = open(file_again)

# this prints out the txt_again variable using the read method
print txt_again.read()
# added a close function, which outputs with 'None'
print txt_again.close()

# outputs the following
# CSEABSEAOSXL2:python_the_hard_way cory.seaborn$ python 15ex.py 15ex_sample.txt 
# Here is your file '15ex_sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# Type the filename again: 
# > 15ex_sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# after adding the close function
# Here is your file '15ex_sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# None
# Type the filename again:
# > 15ex_sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# None

# To run open from the interpreter:
# >>> test = open("15ex_sample.txt")
# >>> print test  
# <open file '15ex_sample.txt', mode 'r' at 0x1028345d0>
# >>> print test.read()
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# >>> lastone = open('15ex_sample.txt')
# >>> print lastone.read()
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# >>> print lastone.close()
# None
# >>> 