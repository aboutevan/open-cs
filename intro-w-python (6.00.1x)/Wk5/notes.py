"""
WK 5: OBJECT ORIENTED PROGRAMMING

- Everything is an object and has a type
- objects are data abstraction:
    - internal representation through data attributes
    - interface for interacting with object

- can create new instances of objects
- can destroy
    - del

- internal representation should be private

CLASSES

- creating vs. instance of class

- creating:
    - define name
    - define attributes

- using class:
    - creating new instances of objects
    - doing operations on the instances
    - i.e. len()

Advantages:
    - bundle data together with procedures
    - divide-and-conquer development
    - easy to reuse code
        - many python modules define new classes
        - each class has a separate env
        - inheritance allows subclasses to redefine or extend class
"""

"""
DEFINE OWN TYPES

    - class Coordinate (object: class parent):
        - code 
        
    - subclass / superclass
    
WHAT ARE ATTRIBUTES
    - data and procedure belong to class
    - data attributes
        - other objs that make up the class
    - procedural attributes (methods)
        - functions that only work with this class
    
DEFINING:
    
    class Coordinate(object):
        // special method to create an instance
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        // python passes self as first arg in ALL methods
            
USE:
    c = Coordinate(3, 4)
    origin = Coordinate(0, 0)
    
__str__ method
    - define this yourself and if you print(className), then it will print the __str__ method
    
- isinstance()
    - use to check if object is a certain class
    isinstance(c, Coordinate)
"""

"""
EX: FRACTIONS

"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        return 'Coordinate' + '(' + str(self.x) + ',' + str(self.y) + ')'



class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        self.common = []
        for e in self.vals:
            if self.member(e) and other.member(e):
                self.common.append(e)
        return '{' + ','.join([str(e) for e in self.common]) + '}'

    def __len__(self):
        return len(self.vals)


c1 = intSet()
c2 = intSet()
c1.insert(5)
c2.insert(5)
c1.insert(20)
c2.insert(20)
print(c1.intersect(c2))

"""

"""