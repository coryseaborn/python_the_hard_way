class Song(object):
    
    # the variables can be anything - anything can be changed
    # this is just a placeholder and doesn't need to be 'self'
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # you use self. because it's clear you eman the instance attribute
    # of self.lyrics, as opposed to not knowing if it's an instance's
    # attribute or a local variable
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
                    
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
test_song = Song(["Testing a brand new song"])

test_song.sing_me_a_song()
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# outputs the following
# 
# Happy birthday to you
# I don't want to get sued
# So I'll stop right there
# They rally around the family
# With pockets full of shells

# simplified class is shown below, to understand the concept
class Complex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
 
# this gives arguments (3.0 and -4.5) to the class instantiation operator (init)
# which are passed
x = Complex(3.0, -4.5)
print x.r, x.i

# outputs the following
# 3.0 -4.5



# Another example of how to call the class like it's function:
# 
# >>> class MyStuff(object):
# ...     def __init__(self):
# ...             self.tangerine = "And now a thousand years between"
# ...     def apple(self):
# ...             print "I AM CLASSY APPLES!"
# ... 
# >>> thing = MyStuff()
# >>> thing.apple()
# I AM CLASSY APPLES!
# >>> print thing.tangerine
# And now a thousand years between
# >>> 
# 


# and another because i need to learn this stuff
# >>> class TestClass(object):
# ...      def __init__(self):
# ...              self.what = "Print a test thing!"
# ...      def noway(self):
# ...              print "Noway print this!"
# ... 
# >>> wut = TestClass()
# >>> wut
# <__main__.TestClass object at 0x1094968d0>
# >>> wut.noway()
# Noway print this!
# >>> wut.what
# 'Print a test thing!'

# another one to drive it home, from ex 44

class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

# set the dad and son instance of the Parent and Child classes
dad = Parent()
son = Child()

# from dad and son instances call the implicit function
dad.implicit()
son.implicit()

# outputs the following
# PARENT implicit()
# PARENT implicit()