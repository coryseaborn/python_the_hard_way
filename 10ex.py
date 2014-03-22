# this puts a tab
tabby_cat = "\tI'm tabbed in."
# this cuts a new line
persian_cat = "I'm split\non a line."
# this just puts a backslash
backslash_cat = "I'm \\ a \\ cat."

# this uses both the tab and new lines
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# output shows the following
# 	I'm tabbed in.
# I'm split
# on a line.
# I'm \ a \ cat.
#
# I'll do a list:
#	* Cat food
#	* Fishies
#	* Catnip
#	* Grass

test_cat = '''
Testing single quotes.
Don't ask why.
Maybe I "should" ask.
'''

test1_cat = """
Testing double quotes.
Don't ask why.
Maybe I "should" ask.
"""

print test_cat
print test1_cat

# outputs the following
# Testing single quotes.
# Don't ask why.
# Maybe I "should" ask.
#
#
# Testing double quotes.
# Don't ask why.
# Maybe I "should" ask.

x = "testing with escaped single \' quote, don't"
y = "testing with escaped double \" quote, because we \"should\" do it"

print x
print y

# above outputs the following
# testing with escaped single ' quote, don't
# testing with escaped double " quote, because we "should" do it

print "\n"
print "%r" % x
print "%r" % y

# above outputs the following in raw format
# "testing with escaped single ' quote, don't"
# 'testing with escaped double " quote, because we "should" do it'

print "\n"
print "%s" % x
print "%s" % y

# above outputs the following in string
# testing with escaped single ' quote, don't
# testing with escaped double " quote, because we "should" do it