from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done. %r copied to %r." % (from_file, to_file)

out_file.close()
in_file.close()

# outputs the following
# corysmini:python_the_hard_way cory$ python 17ex.py 17ex_sample.txt 17ex_dst.txt
# Copying from 17ex_sample.txt to 17ex_dst.txt
# The input file is 21 bytes long
# Does the output file exist? False
# Read, hit RETURN to continue, CTRL-C to abort.
# 
# Alright, all done. '17ex_sample.txt' copied to '17ex_dst.txt'.

# output after simlpifying, so it doesn't prompt
# corysmini:python_the_hard_way cory$ python 17ex.py 17ex_sample.txt 17ex_dst.txt
# Alright, all done. '17ex_sample.txt' copied to '17ex_dst.txt'.
# corysmini:python_the_hard_way cory$ cat 17ex_dst.txt 
# this is a text file.