your_name = 'Zed A. Shaw'
your_age = 35 # not a lie
your_height = 74 # inches
your_weight = 180 # lbs
your_eyes = 'Blue'
your_teeth = 'White'
your_hair = 'Brown'

print "Let's talk about %s." % your_name
print "He's %d inches tall." % your_height
print "He's %d pounds heav." % your_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (your_eyes, your_hair)
print "His teeth are usually %s depending on the coffee." % your_teeth

# this line is gtricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (your_age, your_height, your_weight, your_age + your_height + your_weight)

# output from everything above
#Let's talk about Zed A. Shaw.
#He's 74 inches tall.
#He's 180 pounds heav.
#Actually that's not too heavy.
#He's got Blue eyes and Brown hair.
#His teeth are usually White depending on the coffee.
#If i add 35, 74, and 180 I get 289.

# testing above math, which came out to 289.
print 35 + 74 + 180

print "#####################STUDY DRILLS############################"

# testing different format characters
print "what does percent s give you, here - %s" % your_name
print "how about percent r, here - %r" % your_name
# output of these shows the difference
# what does percent s give you, here - Zed A. Shaw
# how about percent r, here - 'Zed A. Shaw'

# this comes out as an invalid syntax, because its trying format a string to a digit
# print "percent d should give a digit, here - %d" your_name

print "seeing your weight in signed hex, uppercase, here - %X" % your_weight
# output shows this
# seeing your weight in signed hex, uppercase, here - B4

# converting inches and pounds to centimeters and kilos
# 1 inch = 2.54 centimeters
# 1 pound = 0.453592 kilos
inch = 5
lb = 12
inch_to_cent = inch * 2.54
lb_to_kilo = lb * 0.453592

print "Converting %d inches to centimeters - %r" % (inch, inch_to_cent)
print "Converting %d lbs to kilos - %r" % (lb, lb_to_kilo)
# outputs the following
# Converting 5 inches to centimeters - 12.7
# Converting 12 lbs to kilos - 5.443104