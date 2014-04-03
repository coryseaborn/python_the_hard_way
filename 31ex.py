# Remember: An if-statement creates what is called a "branch" in the code.
print """You enter a dark room with two doors. 
Do you want to go through door #1 or door #2?"""

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "Oooh the secret option. You run and get away!"
        print "You see a butterfly, what do you do?"
        print "1. Catch it."
        print "2. Kill it."
        bf = raw_input("> ")
        if bf == "1":
            print "You did it! You caught it!"
            print "Now that you own a butterfly, what do you do?"
            print "1. Eat ice cream."
            print "2. Let it go."
            print "3. Wait until something awesome happens."
            seeya = raw_input("> ")
            if seeya == "1":
                print "Sweet, you did something! Bye!"
            else:
                print "That wasn't an option and you suck."
        elif bf == "2":
            print "You're a murderer, go away."
        else:
            print "Well go home then because you don't understand the game."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare int othe endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of much. Good job!"
        
else:
    print "You stumble and fall on a knife and die. Good job!"
    
# outputs the following
# 
# Do you want to go through door #1 or door #2?
# > 1
# There's a giant bear here eating a cheese cake. What do you do?
# 1. Take the cake.
# 2. Scream at the bear.
# > 2
# The bear eats your legs off. Good job!
# corysmini:python_the_hard_way cory$ python 31ex.py 
# You enter a dark room with two doors. 
# Do you want to go through door #1 or door #2?
# > 1
# There's a giant bear here eating a cheese cake. What do you do?
# 1. Take the cake.
# 2. Scream at the bear.
# > 1
# The bear eats your face off. Good job!
# corysmini:python_the_hard_way cory$ python 31ex.py 
# You enter a dark room with two doors. 
# Do you want to go through door #1 or door #2?
# > 2
# You stare int othe endless abyss at Cthulhu's retina.
# 1. Blueberries.
# 2. Yellow jacket clothespins.
# 3. Understanding revolvers yelling melodies.
# > 3
# The insanity rots your eyes into a pool of much. Good job!
# corysmini:python_the_hard_way cory$ python 31ex.py 
# You enter a dark room with two doors. 
# Do you want to go through door #1 or door #2?
# > 2
# You stare int othe endless abyss at Cthulhu's retina.
# 1. Blueberries.
# 2. Yellow jacket clothespins.
# 3. Understanding revolvers yelling melodies.
# > 1
# Your body survives powered by a mind of jello. Good job!
# corysmini:python_the_hard_way cory$ python 31ex.py 
# You enter a dark room with two doors. 
# Do you want to go through door #1 or door #2?
# > 2
# You stare int othe endless abyss at Cthulhu's retina.
# 1. Blueberries.
# 2. Yellow jacket clothespins.
# 3. Understanding revolvers yelling melodies.
# > 2
# Your body survives powered by a mind of jello. Good job!

# How do I tell if a number is between a range of numbers?
# You have two options: Use 0 < x < 10 or 1 <= x < 10, which is classic notation, 
# or use x in range(1, 10).