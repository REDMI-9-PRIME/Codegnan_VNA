'''Constructor(__init__)
------------------------
-->A constructor is a special method used to initialize object data
__init__()

class student:
    def __init__ (self, name, ID, Batch, Age ):
        self.name = name
        self.ID = ID
        self.Batch = Batch
        self.Age = Age
        
    def display(self):
        print(self.name, self.ID, self.Batch, self.Age)
std_1 = student("akash", 1, "PFS", 23)
std_1.display()

Access Specifiers:
------------------
1.public
syntax -- name
we can use it anywhere in the program.
2.protected
syntax -- _name
This is only for internal use
3.private
syntax -- __name
This one is restricted.
'''
class clue:
    def __init__(self):
        self.public = "Public"
        self.protected = "Protected"
        self.private = "Private"

any = clue()
print(any.public)
print(any.protected)
print(any.private)
