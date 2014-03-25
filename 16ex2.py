# this is for study drill number 2
from sys import argv

script, filename = argv

print "Going to read the %r file now." % filename

target = open(filename)

print "Printing the target file with the read function."
print target.read()

print "Closing that file out now."
print target.close()

# outputs with the following
# CSEABSEAOSXL2:python_the_hard_way cory.seaborn$ python 16ex2.py 16ex_sample.txt 
# Going to read the '16ex_sample.txt' file now.
# Printing the target file with the read function.
# truncated the first line, now taking this guy
# followed by this line
# and then this one finally!
# 
# Closing that file out now.
# None