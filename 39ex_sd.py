test_dict = {
    "First key": "One",
    "Second key": "Two",
    "Third key": "Three"
}

# print test_dict['First key']

for first, second in test_dict.items():
    print "The key is %s and value is %s" % (first, second)

print '-' * 10    
test_dict['Last key'] = 'Four'

for first, second in test_dict.items():
    print "The key is %s and value is %s" % (first, second)
    
print '-' * 10    
test_dict['Too far key'] = 'Five'

for first, second in test_dict.items():
    print "The key is %s and value is %s" % (first, second)

print '-' * 10    
print test_dict["Second key"]

print '-' * 10    
del test_dict["Third key"]

for first, second in test_dict.items():
    print "The key is %s and value is %s" % (first, second)
    
print '-' * 10
print test_dict