# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some new states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, state)
    
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbrevated %s and has city %s" % (
        state, abbrev, cities[abbrev])
    
print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
    
# get a cit ywith a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# dictionaries or dicts are also called hashes with key/value pairs
# outputs the following
# 
# ----------
# NY state has:  New York
# OR state has:  Portland
# ----------
# Michigan's abbreviation is:  MI
# Florida's abbreviation is:  FL
# ----------
# Michigan has:  Detriot
# Florida has:  Jacksonville
# ----------
# California is abbreviated CA
# Michigan is abbreviated MI
# New York is abbreviated NY
# Florida is abbreviated FL
# Oregon is abbreviated OR
# ----------
# FL has the city Oregon
# CA has the city Oregon
# MI has the city Oregon
# OR has the city Oregon
# NY has the city Oregon
# ----------
# California state is abbrevated CA and has city San Fransisco
# Michigan state is abbrevated MI and has city Detriot
# New York state is abbrevated NY and has city New York
# Florida state is abbrevated FL and has city Jacksonville
# Oregon state is abbrevated OR and has city Portland
# ----------
# Sorry, no Texas.
# The city for the state 'TX' is: Does Not Exist