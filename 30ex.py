people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
    
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
    
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, lets stay home then."
    
if cars > people and buses < cars:
    print "Let's get on the stupid bus."
else:
    print "Let's just stay home, this is hard."
    
if cars < people and buses < cars:
    print "Not enough cars."
else:
    print "This is WAY too hard, just stay home."
    
if buses > cars:
    print "More buses than cars."
elif buses < cars:
    print "More cars than buses."
elif buses != cars:
    print "Different amount of buses than cars."
elif buses == cars:
    print "Same amount of buses and cars."
else:
    print "None of it works!"

# an else: closes the block, get an error on the elif    
# if buses > cars:
#     print "More buses than cars."
# else:
#     print "None of it works!"
# elif buses < cars:
#     print "More cars than buses."
# elif buses != cars:
#     print "Different amount of buses than cars."
# elif buses == cars:
#     print "Same amount of buses and cars."
    
# outputs the following
# 
# We should take the cars.
# Maybe we could take the buses.
# Alright, let's just take the buses.