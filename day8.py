'''print(9+8)
print("Python"+"Language")
print([1,2]+ [3,4])

concatenation
--------------
This is nothing but,, a (+) behavior...
case-1
------
integers---this will act as addition for the int

case-2
------
Note: if we access 2 different datatypes we will not get the output.
for other datatypes(we have to use same type)this(+) act as concatenation.

print("Teja" +[1,2])#Type error
print(5+[1,2])
print([1,2]+"Teja")

tuple()-->tuple is a collection of different datatypes and this is
represented by (), seperated by (,)
eg:Thing = (1,"Teja",[12,4],(6,7))
print(Thing)

Thing = (12,89,"python",(23,"Akash",[67,"Python is a Language",(7,8)],[8,("Python",[34,9])]))
print(Thing)
print(Thing[3][2][1][9])

Num = 9
Num_2= 90
print(f"before swapping Num = {Num} and Num_2 = {Num_2}")
Num,Num_2= Num_2,Num
print(f"After swapping Num = {Num} and Num_2 = {Num_2}")
'''
leap_year = int(input("Enter year:"))
if(leap_year % 4 == 0 and leap_year % 100 != 0)or leap_year % 400 ==0:
  print(f"Yes, {leap_year} is a leap year")
else:
    print(f"No,{leap_year}is not a leap year")
