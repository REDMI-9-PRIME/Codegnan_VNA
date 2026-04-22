'''Polymorphism:
----------------
-->This allows a object of different classes to be treated as instance of the same base
class, with methods behaving differently based on the actual object type.
example:
-------
print(len("Python"))
print(len([1,2,3]))

Method Overloading:
-------------------
-->This defines multiple methods with the same name but different parameters, such as
(numbers, type, or order) in the same class.
example-1:
---------
class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
    
cal = calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))
example-2:
---------
class calculator:
    def multiply(self, a, b=0, c=0):
        return a*b*c
    
cal = calculator()
print(cal.multiply(2))
print(cal.multiply(5,6))
print(cal.multiply(6,8,9))

Method Overriding:
------------------
-->This occurs in the child class, redefining a parent class method with the same signature
for runtime.
example-1:
---------
class animal:
    def speak(self):
        return ("speaking")
class dog:
    def bark(self):
        return ("barking")
class cat:
    def meow(self):
        return ("meow")
class snake:
    def ssss(self):
        return ("ssss")
DOG = dog()
CAT = cat()
SNAKE = snake()
print(DOG.bark())
print(CAT.meow())
print(SNAKE.ssss())
example-2:
----------
class Parent:
    def scold(self):
        return ("scolding")
class Father:
    def chatayedava(self):
        return ("chatayedava")
class Mother:
    def vedavanari(self):
        return ("vedavanari")
FATHER = Father()
MOTHER = Mother()
print(FATHER.chatayedava())
print(MOTHER.vedavanari())

Operator Overloading:
---------------------
-->This is customizes operator like +,- for user-defined classes by implementing special
methods.
example:  __add__, __sub__
--------
class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return someone(self.a +other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(4,5)
so = someone(6,10)
print(any + so)

Data Abstraction:
-----------------
-->This hides complex implementation details, exposing only essential features via abstract
class or interface.

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
Circle = circle(5)
print(Circle.area())
'''
