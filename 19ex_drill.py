def my_function(usr_work, known_dates, job):
    print "Someone you work with is %s." % usr_work
    print "You've known them %d days." % known_dates
    print "You hope they get %s!?\n" % job
    
print "Someone you like to work with:"
my_function("Cliff",785,"promoted")

# outputs the following:
# Someone you like to work with:
# Someone you work with is Cliff.
# You've known them 785 days.
# You hope they get promoted!?

print "Someone you don't like to work with:"
my_function("Jerk",20,"fired")

# outputs the following:
# Someone you don't like to work with:
# Someone you work with is Jerk.
# You've known them 20 days.
# You hope they get fired!?

my_function("Stupid "+"Idiot",250,"dead")

# outputs the following:
# Someone you work with is Stupid Idiot.
# You've known them 250 days.
# You hope they get dead!?

guy = "Waldo"
days = 0
work = "canned"

my_function(guy, days, work)

# outputs the following:
# Someone you work with is Waldo.
# You've known them 0 days.
# You hope they get canned!?

# need to convert the user's input to an integer using int()
# needed because the function created formats using %d decimal
name = raw_input("Name of a person: ")
num = int(raw_input("Number of days you've known them: "))
status = raw_input("What do you wish they receive?: ")

my_function(name, num, status)

# outputs the following
# Name of a person: John
# Number of days you've known them: 54325432
# What do you wish they receive?: candy
# Someone you work with is John.
# You've known them 54325432 days.
# You hope they get candy!?