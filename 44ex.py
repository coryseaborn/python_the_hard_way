# Override IMPLICITLY
#
# class Parent(object):
#     
#     def implicit(self):
#         print "PARENT implicit()"
#         
# class Child(Parent):
#     pass
#     
# # create the dad and son instances of the Parent and Child classes
# dad = Parent()
# son = Child()
# 
# # from the dad and son instances call the implicit functions
# dad.implicit()
# son.implicit()
# 
# Override EXPLICITLY
#
# class Parent(object):
#     
#     def override(self):
#         print "PARENT override()"
#         
# class Child(Parent):
#     
#     def override(self):
#         print "CHILD override()"
#         
# create a dad and son instance of Parent and Child class
# dad = Parent()
# son = Child()
# from the dad and son instances, call the override functions
# dad.override()
# son.override()
# outputs the following
# PARENT override()
# CHILD override()
#
# Override using SUPER
#
# class Parent(object):
#     
#     def altered(self):
#         print "PARENT altered()"
#         
# 
# outputs the following - NOTICE that four get spit out
# from the altered() function because of how super works
#
# PARENT implicit()
# PARENT implicit()
# PARENT override()
# CHILD override()
# PARENT altered()
# CHILD, BEFORE PARENT altered()
# PARENT altered()
# CHILD, AFTER PARENT altered()
#
# COMPOSITION
# This is a has-a relationship (instead of the parent-child, which child is-a parent)
# as in Child has-a Other that it uses to get its work done
#
class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        # set self to an instance of class Other
        self.what = Other()

    def implicit(self):
        # call the implicit() function from the self instance
        self.what.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.what.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()