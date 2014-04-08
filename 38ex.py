ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# this does a pop on stuff
print stuff.pop()
# this does a join(' ', stuff), so 'join stuff with space between them'
print ' '.join(stuff) # what? cool!
# this does a join('#' and stuff stuff [3 and stop at 5th element] )
# so 'join stuff 3 through 5 with # between them
# the 3:5 is getting a 'slice' from the stuff list that is from
# element 3 to element 5, which doesn't include element 5
# similar to how range(3, 5) would work
print '#'.join(stuff[3:5]) # super stellar!

# outputs the following
# 
# Wait there's not 10 things in that list, let's fix that.
# Adding:  Boy
# There's 7 items now.
# Adding:  Girl
# There's 8 items now.
# Adding:  Banana
# There's 9 items now.
# Adding:  Corn
# There's 10 items now.
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do some things with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone#Light