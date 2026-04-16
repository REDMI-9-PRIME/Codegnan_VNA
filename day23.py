''' Introduction to OOP'S
classes
objects
Attributes
Methods

OOP'S
-----
--> object oriented programing(oop) is a style of programming where we model real_world
things as objects that contain both data and functions(behaviour).
-->reusability of code.
-->scalability(long scope)

class
-----
--> class is a blueprint or template,that defines what kind of data and behavior a certain
type of object will have.
syntax: class class_Name:
            Pass
example:  class car:

object
------
--> this is instance of class or an object is a real instance created from a class. it is
the actual thing that exists in memory while the program runs.
example: car1 = car()
         car2 = car()

Attributes
----------
--> these are the variables that store data related to a class or object

class Dog:
    def __init__(self, breed, color, gender, weight):
        self.breed = breed
        self.color = color
        self.gender = gender
        self.weight = weight
dog_1 = Dog("Labrador", "Brown", "Male","10kg")
dog_2 = Dog("puppy", "white", "Female","9kg")
dog_3 = Dog("husky", "black", "Male", "12kg")
print(dog_1.color,dog_2.breed,dog_3.weight,dog_1.gender)

class car:
    def __init__(self,brand,model,Type,year,color):
        self.brand = brand
        self.model = model
        self.Type = Type
        self.year = year
        self.color = color
car_1 = car("toyota","Camry","Sedan","2022","white")
car_2 = car("Hyundai","Creta","SUV","2023","Black")
print(car_1.brand,car_2.model,car_1.Type,car_2.year,car_1.color)
'''
class mobiles:
    def __init__(self,brand,model,price,color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
mobiles_1 = mobiles("Samsung","Galaxy S23","75000","black")
mobiles_2 = mobiles("Apple","iPhone 14","80000","Blue")
print(mobiles_1.brand,mobiles_2.model)
