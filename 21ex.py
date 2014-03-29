# this defines the 'add' function, using the 'return' statement
# to assign a value to the variable which is calling the function
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with just functions!"

# these are variables which are calling the defined functions above
# the value of each function is then assigned to the variable
age = add(20, 6)
height = subtract(78, 4)
weight = multiply (82, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, EQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

# orginal variable calling the functions defined above 
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what = add(age, subtract(height, multiply(weight, divide(iq, add(5, 5)))))

print "That becomes: ", what, "Can you do it by hand?"

# outputs the following
# Let's do some math with just functions!
# ADDING 20 + 6
# SUBTRACTING 78 - 4
# MULTIPLYING 82 * 2
# DIVIDING 100 / 2
# Age: 26, Height: 74, Weight: 164, EQ: 50
# Here is a puzzle.
# DIVIDING 50 / 2
# MULTIPLYING 164 * 25
# SUBTRACTING 74 - 4100
# ADDING 26 + -4026
# That becomes:  -4000 Can you do it by hand?

# With int(raw_input()), the problem with that is then you can't enter
# floating point, so also try using float(raw_input()) instead

# return statement causes your function to exit, hand back a value to its caller
# for example, age = add(20, 6). if the return statement is commented
# out in the function, then you get an error printing all the variables because
# the age variable has NoneType assigned. sample output is below showing this
# Traceback (most recent call last):
#   File "21ex.py", line 24, in <module>
#     print "Age: %d, Height: %d, Weight: %d, EQ: %d" % (age, height, weight, iq)
# TypeError: %d format: a number is required, not NoneType