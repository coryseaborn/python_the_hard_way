# while-loops. What they do is simply do a test like an if-statement, 
# but instead of running the code block once, they jump back to the "top" 
# where the while is, and repeat. It keeps doing this until the expression is False.
i = 0
numbers = []

def fun(arg1):
    return arg1

x = fun(30)

def fun1(arg1, arg2):
    return arg1 + arg2
    
while i < x:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = fun1(i, 3)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
# original exercise was the following:
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#     
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# making a for loop:
# for i in range(0, 10):
#     print "At the top i is %d" % i
#     numbers.append(i)
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i

    
print "The numbers list contains the following: "

for num in numbers:
    print num
    
    
# outputs the following
# 
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 1
# At the top i is 1
# Numbers now:  [0, 1]
# At the bottom i is 2
# At the top i is 2
# Numbers now:  [0, 1, 2]
# At the bottom i is 3
# At the top i is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom i is 4
# At the top i is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom i is 5
# At the top i is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 6
# The numbers list contains the following: 
# 0
# 1
# 2
# 3
# 4
# 5