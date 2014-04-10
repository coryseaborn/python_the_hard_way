## Animal is-a object (yes, sort of confusing) lok at the extra credit
class Animal(object):
    print "This is the Animal class!"
    pass
    
## Dog is-a Animal
class Dog(Animal):
    print "This is the Dog class!"
    
    def __init__(self, name): # class Dog has-a __init__ that takes parameters
        ## name is-a object - from self get the name attribute and set it to name
        ## Dog has-a name of some kind
        self.name = name
        print name
        
## Cat is-a Animal
class Cat(Animal):
    print "This is the Cat class!"
    
    def __init__(self, name): # class Cat has-a __init__ that takes parameters
        ## name is-a object - from self get the name attribute and set it to name
        ## Cat has-a name of some kind
        self.name = name
        
## Person is-a object
class Person(object):
    
    def __init__(self, name): # class Person has-a __init__ that takes parameters
        ## name is-a object - from self get the name attribute and set it to name
        ## Person has-a name of some kind
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        print name
        
## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## what is this strange magic?
        ## this is how you can run the __init__ method of a parent class
        ## in this case, the __init__ of Person
        super(Employee, self).__init__(name)
        ## from self get the salary attribute and set it to salary
        ## Employee has-a salary of some kind
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass
    
## Salmon is-a fish:
class Salmon(Fish):
    pass
        
## Halibut is-a fish:
class Halibut(Fish):
    pass
    
    
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## from mary get the attribute pet and set it to satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## from Frank get the attribute pet and assign it rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()





# This is where "class is-a object" comes in. They decided that they would use
# the word "object," lowercased, to be the "class" that you inherit from to make
# a class. Confusing, right? A class inherits from the class named object to make 
# a class but it's not an object really it's a class, but do not forget to inherit 
# from object.