from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# outputs the follwoing based on the argument passed to the program
# corysmini:python_the_hard_way cory$ python 13ex.py first 2nd 3rd
# The script is called: 13ex.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# corysmini:python_the_hard_way cory$ python 13ex.py what am i
# The script is called: 13ex.py
# Your first variable is: what
# Your second variable is: am
# Your third variable is: i

# What's the difference between argv and raw_input()?
# The difference has to do with where the user is required to give input. If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use raw_input().