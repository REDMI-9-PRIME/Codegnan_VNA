'''
Variables -->Variable is basically named storage location that is used to hold the
data in the memory,to make it simple it is the label which points
out to a value -->storage placeholders

Rules for defining variables
-->A-Z,a-z,0-9
-->start with uppercase,lowercase letters,even with a underscore _
-->But you cannot start with symbols (@,#,$...),even numbers also

Better preferable way is go with general purpose -->you want to store
your details name,email_id,account_number...

'''
'''
a = 1
b = 5
a = 25
#Python is dynamically typed,you need not define the datatype and also
#only the recent value to the variable with same name is pointed

print(a)
print(b)

#1a23 = 25 #Syntax Error

#@werf = 4.5 #Syntax Error

#$dsf = 12 #Invalid Syntax

#Store your personal details

name = "Codegnan"
location = "Visakhapatnam"
age = 7
emailid = "cmo@codegnan.com"
email_id = "cmo@codegnan.com"
print(name,location,age,email_id)

#How to assign multiple values to a variables
akash,praneeth,ajay = 21,20,23
print(akash)
print(praneeth)
print(ajay)

#assign same value to multiple variables

x = y = z = 21
print(x,y,z)

#Keywords are reserved words which will have specific usage/meaning
#There are 35 keywords in Python
#never use keywords as Identifiers

#if = 23
#lambda = 'saketh'
#False = 0 #cannot assign

#Python is case-sensitive
false = 25

#Identifiers are names given to variables,functions,classes,objects...

#Literals are fixed values to a Identifier
age = 25
name = 'saketh'
#name is Identifier,25 is literal

#Single line comments --> #
#Multi line comments -->  #start  end with triple quotes
'''
#Built-in Datatypes -->Numeric,boolean,Collections

#Numeric datatypes -->int,float,complex
#int -->count,values,quantities
#float -->temperature,percentage,price
#complex --> specific conversions (real and imaginary)
#implicit as Python follows dynamic type
'''count = 40
print(count)
print(type(count))

price = 175.25
print(price)
print(type(price))

j3 = 25
value = 2+j3
print(value)
print(type(value))

value = 2+3j
print(value)
print(type(value))

#Typecasting -->converting one type to another

#int -->float,complex

age = 25
print(type(age))

b = float(age)
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))

#float,complex
price = 275.25
print(type(price))
d = int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e))

f = 2+5j
print(type(f))
#g = int(f) #complex to int is not possible
#print(g)
h = float(f)#complex to float is not possible
print(h)

#boolean datatype -->validation -->True / False
a = True
print(a)
print(type(a))

#Typeconversion of bool
b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))

#Input --> input()/ output -->print()
a = 5
print(a)

a = input("Enter a value") #any input but result as str
print(a)
print(type(a))

a = int(input("Enter a value:")) #only integer input
print(a)
print(type(a))

b = float(input("Enter another value"))
print(b)
print(type(b))
'''
#Now let's work on a simple case study using above -->Fee calculator

#details of the student
name = input("Enter the student name:")
print("----------")
admission_fees = int(input("Enter the Admission Fees:"))
tuition_fees = float(input("Enter the Tuition Fees:"))
hostel_fees = float(input("Enter the Hostel Fees:"))
#Calculate the Total Fees
total_fees = admission_fees + tuition_fees + hostel_fees
print("<----------------------->")
print("Student Name :",name)
print("Admission Fees is :",admission_fees)
print("Tuition Fees is :",tuition_fees)
print("Hostel Fees is :",hostel_fees)
print("Total Fees is = ",total_fees)
print("----------------")






































































































      










































































