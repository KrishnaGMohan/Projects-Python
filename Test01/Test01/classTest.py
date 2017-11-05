class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = [3,5,7]

    def f(self):
        return 'hello world'


x = MyClass()
print(x.data)
print(x.i)

# Data attributes need not be declared; like local variables, 
# they spring into existence when they are first assigned to!
# counter is one such variable. Note that it has not been 
# declared in the class.

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# calling the member method
x.f()

# Another example. Note the constructor __init__

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(3.0, -4.5)
y.r, y.i


#-----------------------------------------------------------------

# Generally speaking, instance variables are for data unique to each instance 
# and class variables are for attributes and methods shared by all instances 
# of the class:
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)       # shared by all dogs
print(e.kind)       # shared by all dogs
print(d.name)       # unique to d
print(e.name)       # unique to d



# Correct design of the class should use an instance variable 
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


# Inheritance
# class DerivedClassName(BaseClassName):
# class DerivedClassName(modname.BaseClassName):
#
# Method references are resolved as follows: the corresponding class attribute is 
# searched, descending down the chain of base classes if necessary, and the method 
# reference is valid if this yields a function object.
#
# Derived classes may override methods of their base classes
# 
# ---------------------------------------------------------------------------------
# Multiple Inheritance
# class DerivedClassName(Base1, Base2, Base3):

#

# “Private” instance variables that cannot be accessed except from inside an object 
# don’t exist in Python. However, there is a convention that is followed by most 
# Python code: a name prefixed with an underscore (e.g. _spam) should be treated 
# as a non-public part of the API

# Empty Class
class Employee:
    pass
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000







