'''Metacharacters:
-----------------
7.?->This meta character will form a searching pattern as it will take any zero or one
character for (?)
syntax:re.findall(".?",Variable_name)
       re.search(".?",Variable_name)
example1:
--------
import re
any = "This meta character"
an = re.findall("Th.?",any)
na = re.search("me.?",any)
print(an)
print(na)
-------------------------------------------------------------------------------------------
8.{}->This meta character will form a searching pattern as we can mention the size in the{}
syntax:re.search(".{size}",variable)
example1:
--------
import re
any = "This meta character will form a searching pattern as it will take any zero"
an = re.findall(".{25}as",any)
me = re.findall("me.{15}",any)
print(an)
print(me)
--------------------------------------------------------------------------------------------
9. |->This metacharacter will form a searching pattern as it consider right or left any
string is present or not for (|)
example1:
--------
import re
any = "This meta character will form "
an = re.findall("that|will",any)
print(an)
-------------------------------------------------------------------------------------------
special sequence:A special sequence is a \ followed by one of the characters in the list
----------------  below, and has a  special meaning.

10. \A->Returns a match if the specified characters are at the the beginning of the string.
eg: "\AThe"
import re
txt = "The potatoes are good"
#check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")
-------------------------------------------------------------------------------------------
11. \b->Returns a match where the specified characters are at the beginning or at the end
of the word.
eg: r"\bain"
import re
txt = "The potatoes are good"
#check if "is present at the beginning of a WORD":
x = re.findall(r"\bgood", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
--------------------------------------------------------------------------------------------
12. \d->Returns a match where the string contains digits(numbers from 0-9)
eg: "\d"
import re
txt = "The rain in 56 Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
--------------------------------------------------------------------------------------------
13. \D->Returns a match where the string does notcontains digits(numbers from 0-9)
import re
txt = "The rain in 56 Spain"
x = re.findall("\D",txt)
print(x)
if x:
    print("yes, there is one digit")
else:
    print("no match")
--------------------------------------------------------------------------------------------
14. \s->returns a match where the string contains a white space character.
eg:"\s"
import re
txt = "The rain in spain"
#Return a match at every white-space character:
x = re.findall("\s",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
-------------------------------------------------------------------------------------------
Time and Date:
--------------
%d-- Day
%m-- Month
%Y-- Year
%H-- Hours
%M-- Min
%S-- Sec
%p-- AM/PM
%A-- Day name
%B-- Month name

import datetime
any = datetime.datetime.now()
print(any)
'''
import datetime
today = datetime.date.today()

print(today.strftime("%d-%m-%y"))
print(today.strftime("%A"))
print(today.strftime("%B"))
print(today.strftime("%m"))
