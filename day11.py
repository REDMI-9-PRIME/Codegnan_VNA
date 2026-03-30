'''any_ = "Python is a programming language"
vowel_cou = 0
space_cou = 0
con_cou = 0
for j in any_:
    if j in "AEIOUaeioe":
        vowel_cou += 1
    elif j == " ":
        space_cou += 1
    else:
        con_cou += 1
print(f"this is count of all vowel in the string :{vowel_cou}")
print(f"this is count of all space in the string :{space_cou}")
print(f"this is count of all consonants in the string :{con_cou}")
print(f"this is count of all consonants in the string :{len(any_)-(vowel_cou + space_cou)}")

j is initial variable.

a = 9
print(b)
for j in range(1,10):
    print(j)

range()--> this is used to generate the numbers.
syntax: range(start,end,step)
step means positon ,2nd step means 2nd position.

for j in range(1,20,3):
    print(j)

*string to list,tuple

any = "abc"
print(list(any))
print(tuple(any))

any = "123"
print(int(any))
print(float(any))
print(str(any))

an = [1,2,3]
vs = str(an)
print(type(vs))
print(vs)
print(tuple(an))

a=[("akash",1),("sai",2)]
print(dict(a))

reverse the string

a='akash'
print(a[::-1])#dont use this reverse method

rev_str = "akash"
empty_ = ""
for j in rev_str:
    empty_= j + empty_
    print(empty_)
palindrome->if we reverse the string we should get same value.

rev_str = "madam"
empty_ = ""
for j in rev_str:
    empty_= j + empty_
if empty_== rev_str:
    print(f"{rev_str} is palin")
else:
    print(f"{rev_str} is not a palin")
'''
for num in range(1,101):
  if num%2 == 0:
      print(f"{num} is a even num")
  else:
      print(f"{num} is a odd num")
        
    
