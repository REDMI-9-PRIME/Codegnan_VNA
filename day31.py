'''Regular Expression(Reg Ex):
------------------------------
-->This regular expression is a sequence of characters that forms a searching pattern.
-->To use this we have to "import re",which will unlock the package.
-------------------------------------------------------------------------------------------
Functions:
----------
1. findall: by using this function,it will find all the sequence in the string.
----------
syntax: re.findall("metachar",variable_name)
2. search:by using this function,it will only find first sequence in the string.
---------
syntax: re.search("metachar",variable_name)
------------------------------------------------------------------------------------------
Metacharacters:
--------------
-->Metacharacters are used to form searching pattern.
1.[]->In this metacharacter we an search for [a-z],[A-Z],[0-9]
example1:
--------
import re
any = "My friends all are good people.they help if i need and solve my problem."
so = re.findall("[a-z]",any)
print(so)
example2:
--------
import re
hai = "My friends all are good people.they help if i need and solve my problem."
so = re.search("[a]",hai)
print(so)

2.dot(.)->This meta character will form a searching pattern as it will take any single
character for(.)
example1:
--------
import re
hell = "india"
bro = re.search("in..a",hell)
print(bro)
example2:
---------
import re
hell = "india"
the = re.findall("i.d.a",hell)
print(the)
example3:
---------
import re
hell = "india"
doll = re.findall("i.d..a",hell)
print(doll)

3.^->This is used to find the string is starting with the sequence.
syntax: re.findall("metachar",variable_name)
example1:
--------
import re
how = "This is used to find the string is starting with the sequence"
who = re.findall("^This is",how)
they = re.findall("^string",how)
print(who)
print(they)
example2:
--------
how = "This is used to find the string is starting with the sequence"
then = re.search("^This",how)
print(then)

4.$->This is used to find the string is ending with the sequence or not.
syntax: re.findall("$",variable_name)
example1:
--------
import re
out = "This is used to find the string is ending with the sequence "
one = re.findall("sequence $",out)
two = re.search("This$", out)
print(one)
print(two)

5.*->This meta character will form a searching pattern as it will take any zero or more
character for (*).
syntax: re.findall(".*",variable_name)
example1:
--------
import re
ds = "This meta character will form a searching pattern as it will take any zero"
vn = re.findall("c.*e",ds)
nv = re.search("T.*",ds)
print(vn)
print(nv)

6.+->This meta character will form a searching pattern as it will take any one or more
character for (+)
syntax: re.search(".+",variable_name)
example1:
--------
import re
gf = "This meta character will form a searching pattern as it will take any one or more"
hi = re.findall("an.*y",gf)
ih = re.findall("an.+y",gf)
roll = re.search("t.",gf)
hall = re.search("t....",gf)
print(hi)
print(ih)
print(roll)
print(hall)
'''
