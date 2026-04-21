'''inheritance:
--------------
3.multi-level inheritance:
--------------------------
-->This occurs when a class inherits from a child class, creating a grandparent to parent to
child.
example1:
---------
class grandfather():               #multi-level inheritance
    def old(self):
        print("This is grandfather")
class father(grandfather):
    def age(self):
        print("This is father")
class child(father):
    def young(self):
        print("This is child")
obj = child()
obj.old()
obj.age()
obj.young()
example2:
---------
class mobile():
    def old(self):
        print("This is mobilephone")
class update(mobile):
    def new(self):
        print("This mobilephone is updated")
class data(update):
    def open(self):
        print("This mobilephone data is notchanged")
obj = data()
obj.old()
obj.new()
obj.open()

4.Hierchical inheritance:
-------------------------
-->This occurs when multiple child classes inherit from a single parent class, this process
is called hierchical inheritance.
example1:
--------
class parent():                   #Hierchical inheritance
    def old(self):
        print("This is parent")
class child1(parent):
    def play(self):
        print("This is child1")
class child2(parent):
    def new(self):
        print("This is child2")
class child3(child1,child2):
    def young(self):
        print("This is child3")
obj = child3()
obj.old()
obj.play()
obj.new()
obj.young()

5.Hybrid inheritance:
---------------------
-->This is a combination of 2 or more types of inheritance such as single,multiple,
multilevel,hierchical all this is called hybrid inheritance.
example1:
--------
'''
class mobile():                              #multilevel
    def old(self):
        print("This is mobilephone")
class update(mobile):
    def gang(self):
        print("This mobilephone is updated")
class data(update):
    def open(self):
        print("This mobilephone data is notchanged")
        
class parent():                             #Hierchical inheritance                  
    def old(self):
        print("This is parent")
class child1(parent):            
    def play(self):
        print("This is child1")
class child2(parent):
    def new(self):
        print("This is child2")
class child3(child1,child2,update):
    def young(self):
        print("I have inherited from update class and child1,child2")
obj = child3()
obj.gang()
obj.play()
obj.new()
obj.young()















