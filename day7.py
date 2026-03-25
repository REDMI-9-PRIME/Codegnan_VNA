'''
Time_aday = input("Enter 24 hours time: ")
Parts_=Time_aday.split(":")
print(Parts_)
hours_=int(Parts_[0])
print(hours_)
Min_=int(Parts_[1])
print(Min_)
if hours_ >=13 and Min_ < 60:
    print(f"{Time_aday} convert into {hours_-12}:{Min_}pm")
else:
    print(f"You have entered nrml or min are incorrect")

<------------------------------------------------------------->
list-->Collection of different items inside the [],which are seperated by ,.
example-->[1,"Name",[1,2,"Akash"]]
'''
'''
List_1 = [1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(List_1[4])
print(List_1[4][2])
print(List_1[4][2][0])
print(List_1[4][2][0][3])
List_2 = [1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(List_1[4][2][1])
print(List_1[4][2][0][3])
'''
'''
Methods of list
----------------
->append()-This method is used to add new items into list,it will go only for
the last index of the list.
syntax--> Variable_name.append(item)
->extend()-This method is used to add items to list in the last index,where
each item or substring is each index in the list.
->remove()-->This method will delete the item or value directly.
syntax-->Variable_name.remove(item)
->pop()-->This method will delete the item or value based on index position.
syntax-->Variable_name.pop(item)
Mutable--> I can directly modify on that particular variable
Imutable--> I can not modify directly on the variable.

List_2=[1,2,3,4,5]
print(List_2)
List_2.append([23,89])
print(List_2)

list_3 = [23,45,43]
list_3.extend("akash")
print(list_3)
list_3.extend([12,34,67,89,90])
print(list_3)

list_4=[23,45,43]
list_4.remove(43)
print(list_4)
'''
list_5=[23,'python',56,89,6]
list_5.pop(1)
print(list_5)
