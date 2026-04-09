'''lambda function()
--------------------
--> This is also called anonymous function.
--> A lambda function can take n number of arguments but have only one expression.
syntax:  lambda(keyword) arguments : expression
Examples:
any = lambda so : so + 10
print(any(6))
some = lambda an, how: how - an
print(some(4,9))
some = lambda an, how, do: (how - an)* do
print(some(4,9,2))

sai = lambda an, how, do: (how - an)* do,do + an
print(sai(4,9,2))(wrong implementation)

bhai = lambda four, five, two : (four + five)- two
print(bhai(4,5,2))

bro = lambda nine, eight, seven : (nine - eight)+ seven
print(bro(9,8,7))

april = lambda three, six, ten : (three * six)/ ten
print(april(3,6,10))

list Comprehension:
-------------------
-->This is offers the shorter syntax when you want to create a new list from the
existing list.
syntax:  Variable_name = [expression loop and addition]

old_list = [1,2,3,4,5]
new_list = [j for j in old_list]
print(new_list)
'''
old_list = [1,2,3,4,5]
new_list = [j for j in old_list if j%2==0]
print(new_list)
