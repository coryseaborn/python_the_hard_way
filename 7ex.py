# prints out everything as expected
print "Mary had a little lamb."
# prints out snow, which is just a string. a variable wouldn't have the single quotes around it
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary went."
# this just prints ten periods
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try rmoving it and see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# the reason you add the comma instead of putting one long line is because longer than 80 characters in python is considered bad style

# output shows the following
# Mary had a little lamb.
# Its fleece was white as snow
# And everywhere that Mary wet.
# ..........
# Cheese Burger

# when removing the comma after end6 it shows the following, they don't end up on the same line
# ..........
# Cheese
# Burger