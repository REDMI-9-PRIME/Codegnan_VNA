'''Handling Errors:
------------------
1.try block:
-----------
-->The try block will test a block of code for errors.
example:
-------
try:
    print(b)
-------------------------------------------------------------------------
2.Except block:
--------------
-->This block will take care of any errors
example1:
-------
try:
    print(b)
except:
    print("This block can error")
example2:
--------
try:
    print(b)
except NameError:
    print("b is not defined")
----------------------------------------------------------------------------
3.else block:
------------
-->else keyword to define a block of code to be executed if no error were raied.
example1:
--------
try:
    a = 9
    b = 0
    print(a / b)
except:
    print("Error here")
else:
    print("No error in the code")
example2:
---------
try:
    a = 25
    b = 19
    print(b - a)
except:
    print("Error here")
else:
    print("No error in the code")
------------------------------------------------------------------------------
4.finally block:
---------------
-->This block will execute either try block having any error or no error
example1:
--------
try:
    a = 25
    b = 19
    print(b + a)
except:
    print("Error here")
else:
    print("No error in the code")
finally:
    print("The try-except block is finished")
example2:
--------
try:
    a = 9
    b = 0
    print(a / b)
except:
    print("Error here")
else:
    print("No error in the code")
finally:
    print("The try-except block is finished")
---------------------------------------------------------------------------
'''
try:
    num = int(input("Enter a number: "))
    num_2 = int(input("Enter a number: "))
    result = num / num_2
    print(so)
except NameError:
    print("so is not defined")
except ValueError:
    print("pls enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result = {result}")
finally:
    print("Program is completed")
