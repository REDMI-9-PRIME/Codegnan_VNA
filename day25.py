'''Encapsulation:
----------------
->The principle of bunding data(Attributes) and methods that operate on that data into a
single unit, which is a class.

class BankAC:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = BankAC(20000)
Acc.deposite(8000)
print(Acc.get_balance())

class Aadhar:
    def __init__(self, number):
        self.__number = number

    def name(self, name):
        self.__name = name

    def address(self, address):
        self.__address = address

    def DOB(self, DOB):
        self.__DOB = DOB

    def phno(self, phno):
        self.__phno = phno

    def get_details(self):
        print(self.__number)
        print(self.__name)
        print(self.__address)
        print(self.__DOB)
        print(self.__phno)
Card = Aadhar(8059845699)
Card.name("AKASH")
Card.address("duvvada")
Card.DOB("29-05-2003")
Card.phno("7799990447")
print(Card.get_details())

Inheritance:
------------
->This allows a child class(subclass) to acquire the attributes and methods of a parent
class(base class) this is inheritance.
1.single inheritance:
--------------------
 using single method of the class from base class.
example:
-------
 class parent:                               #single inheritance
    def display(self):
        print("This is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
any = child()
any.display()

2.multiple inheritance:
----------------------
   


super()
-------
-->this is used to call methods of the parent class from the child class
'''
class father:
    def hai(self):
        print("This is father")
class mother:
    def rage(self):
        print("This is mother")
class child(father, mother):
    def play(self):
        print("This is child")
obj = child()
obj.hai()
obj.rage()
obj.play()

       
