from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("What do you wanna do? ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# this is what the original writes were
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# here's the same but in one line for study drill 3
target.write(("%s\n%s\n%s\n") % (line1, line2, line3))

print "And finally, we close it."
target.close()

# outputs the following
# CSEABSEAOSXL2:python_the_hard_way cory.seaborn$ python 16ex.py 16ex_sample.txt
# We're going to erase '16ex_sample.txt'.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# What do you wanna do? 
# Opening the file...
# Truncating the file. Goodbye!
# Now I'm going to ask you for three lines.
# line 1: truncated the first line, now taking this guy
# line 2: followed by this line
# line 3: and then this one finally!
# I'm going to write these to the file.
# And finally, we close it.

# this creates the 16ex_sample.txt file, which ends up with the following
# truncated the first line, now taking this guy
# followed by this line
# and then this one finally!