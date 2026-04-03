'''num = int(input("Enter the limit: "))
for j in range(num):
    for i in range(j):
        print("*",end = "")
    print()
here j = number
     i = how many times repeat

num = int(input("Enter the limit: "))
for j in range(num):
    for i in range(j):
        print("1",end = "")
    print() 

num = int(input("Enter the limit: "))
for j in range(num):
    for i in range(num):
        print("*",end= "")
    print()

num = int(input("Enter the limit: "))
for j in range(num):
   for i in range(num-j):
       print("*",end= "")
   print()

num = int(input("Enter the limit: "))
for j in range(num):
    print(" " *(num-j),end = "")
    for i in range(j+1):
        print("*", end="")
    print()
'''

'''Bank details'''
SBI_Akash_ = {"Name" : "Akash",
              "ATM PIN" : "7799",
              "Balance" : 5000}
print("Welcome to SBI ATM")
print("pls insert your ATM card")
SBI_pin = input("plz enter your 4 digits ATM pin: ")
if len(SBI_pin) == 4:
    if SBI_pin in SBI_Akash_['ATM PIN']:
        user_choice = int(input("Enter \n1. for Withdraw: "))
        if user_choice == 1:
            money_w = int(input("Enter money you want to withdraw: "))
            if money_w <= SBI_Akash_['Balance']:
                SBI_Akash_['Balance'] -= money_w
                print(f"money withdrawn,your balance is {SBI_Akash_['Balance']}")
            else:
                print("you have entered wrong pin")
                
else:
  print("invalid pin, enter 4 digit pin")
