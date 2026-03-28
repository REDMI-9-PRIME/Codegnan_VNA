'''
we can store data as key : value
keys--- are union and we can only give immutable data types in the keys
values--- we all data types(immutable and mutable)
{}
methods
--------
keys()--this method is used to get all keys from the dict
values()--this method is used to get all values from the dict
clear()--this method is used to delete the dict

sbi_akash = {"name":"Akash",
             "Role":"Mentor",
             "Sal":5678}
#print(sbi_akash)
#print(sbi_akash.keys())
#print(sbi_akash.values())
sbi_akash.clear()
print(sbi_akash)

set{}--set data type is a unordered collection and it never allow duplicates.
methods
--------
union--this method is used to add or get 2 different sets without duplicates.
intersection--this method is used to find out common  items from 2 sets.
difference--this method is used to find the difference once from the 2nd set.

any = {1,2,3,4}
so = {4,5,6}
#print(any)
#print(any.union(so))
#print(any.intersection(so))
#print(any.difference(so))
#any.remove(3)
#print(any)
'''
userinfo={"user_name":"Akash",
           "pin":"2003"}

user_info=input("enter your pin:")
if user_info in userinfo["pin"]:
    print("valid")
else:
    print("invalid")

