'''Generators
-------------
-->This is a special type of function that return an ITERATOR which one at a time.

def my_generator():
    yield 1
    yield 2
    yield 3

to = my_generator()
print(next(to))
print(next(to))
print(next(to))
------------------------
def square_gen(n):
    for i in range(n):
        yield i*i

for val in square_gen(6):
    print(val)
    
yield
-----
-->it will take a pause and again resume,this is not a nrml keyword can not be used in
nrml functions.
-->this is used to produce a value and pause execution.

def power_gen(n):
    for i in range(n):
        yield i**i

for val in power_gen(5):
    print(val)
------------------------
def modulus_gen(n):
    for i in range(1,n):
        yield i%i

for val in modulus_gen(5):
    print(val)

Next()
------
-->this is used to get next value from a generator
-->when the value is finished, it will stop the iterator.
'''
def power_gen(n):
    for i in range(n):
        yield 

for val in power_gen():
    print(val)
