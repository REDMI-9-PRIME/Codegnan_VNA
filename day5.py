'''String ---> String is a sequence of char, which represented by
""or'' and we can acccess the string characters using indexing
and also slicing.this is also immutable, where i coould not able to
modify on that paticular variable.'''
 
any = 'Python Programing'
'''
#print(any[7])#indexing
#print(any[7,8,9])#type error: string indices must be integers,not tuples
print(any[-6])#negative indexing is possible.
print(any[30])#gives error as index in out of range

#Slicing
#print(any[7:13])
#print(any[:5])#by default the starting index will be zero

#Strings are immutable
print(any.replace("Python","Java"))

print(any.replace("Python","Java"))

-->strings are immutable where we cannot modify on that particular variable.
so = any.replace("Python","Java")
print(any)
print(so)
len()--> len() method is used to get char present in the string or find the
length of the string.
'''
'''
#Task
a_day = "I'm Akash from vizag.I'm am python trainne from codegnan"
print(f"My name is {a_day[4:8]}")
print(f"I am {a_day[-9:-4]}")
print(f"I am {a_day[1:10]}")
'''

'''
#Task
name ="Teja"

print(f" Reversed string {name[::-1]}")
print(len(name))
print(len(digit))#ogject type 'int' as no method len()

*Note:-we can able to convert a string into integer, if the contain
only integer values...
'''
'''
some = "123p"
num = int(some)
print(type(num))
'''
'''
Methods of string
-------------------
->split()-->remove space,and the is in the list[]it will give the
seperated thing in each index.
syntax-->var_name.split("substring")
->lower()-->this is used to convert all letter to lower case.
syntax-->var_name.lower()
->upper()-->this is used to convert all letter to upper case.
syntax-->var_name.upper()
->replace()-->this is used to replace the old string with the new string.
syntax-->var_name.replace("old string","new string")
'''
some = "python is a programming Language"
print(some.split(" "))
print(some.split("programming"))
print(some.lower())
print(some.upper())
print(some.replace("programming","normal"))

if "python" in some:
   print("yes")
else:
   print("no")






