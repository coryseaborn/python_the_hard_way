# creating fallback 'oops' for else statements
def oops():
    print "He hates that, cries, and wants to go home. Hit Enter to try again!"
    raw_input()
    start()

def quit(why):
    print why, "\nThanks for playing!"
    exit(0)

# start of the game!
def start():
    print """\n*********************************************
Welcome to the William and Wallace adventures! 
Where Will explores the neighborhood
and TT tries her absolute hardest to keep up.
Type in 'exit' at any time to quit.
*********************************************\n"""
    print "Will's already in an awesome mood."
    print "Where would you like to go?"
    print "1. The zoo!"
    print "2. The aquarium!"
    print "3. Menchies!"
    print "4. Ella Bailey!"
    next = raw_input("> ")
    
# choosing a location and head there    
    if next == "1" or "zoo" in next:
        zoo()
    elif next == "2" or "aquarium" in next:
        aquarium()
    elif next == "3" or "menchies" in next:
        menchies()
    elif next == "4" or "ella bailey" in next:
        ella_bailey()
    elif next == "exit":
        quit("Fine, I didn't want you to play anyways. We barely even got started!")
    else:
        oops()
                
# what happens at these locations are defined here    
def zoo():
    print "You got to the zoo!"
    print "You ask Will what animal he wants to see"
    print "But he just mean mugs you. Take a guess!"
    print "Maybe monkeys? Elephants? Zebras? Tigers?"
    will_happy = False
    
    while True:
        next = raw_input("> ")
        
        if "monkey" in next:
            print "He likes the Monkeys! Time to go check em out."
            print "You check out the Monkeys for a minute but now he wants a treat."
            print "Guess we're going to Menchies!"
            menchies()
        elif "tiger" in next and not will_happy:
            print "He says 'shure' and you check out the elephants. Now what?"
            will_happy = True
        elif "tiger" in next and will_happy:
            quit("Again? Great, now he's super mad. Time to go home!")
        elif "elephant" in next:
            print "He loves the elephants! But now he's cranky and wants ice cream."
            print "To Menchies we go!"
            menchies()
        elif "quit" in next:
            quit("Okay, take the day off then, see if I care.")
        else:
            print "You see the %s. I feel Wallace coming.. \nNow what should we see?" % next
    
def aquarium():
    print "You got to the aquarium!"
    
def menchies():
    print "You got to Menchies!"
    
def ella_bailey():
    print "You got to Ella Bailey!"

# treasures along the way
def treasures():
    print "You got a treasuer!"

# traps
def traps():    
    print "You ran into a trap!"

# calls the start of the game
start()