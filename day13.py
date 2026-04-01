'''num = [10,15,20,30,35,65,85,80]
even_num = 0
odd_num = 0
for n in num:
    if(n%2)==0:
      even_num += num
    else:
      odd_num += num
print(f"sum of even numbers:{even_num}")
print(f"sum of odd numbers:{odd_num}")

table_num = int(input("Enter a number:"))
for j in range(1,11):
    print(f"{table_num}x {j} = {table_num*j}")

an = "Python Is A Programming Language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
        count_L += 1
print(f"There are total {count_U} Cap L")
print(f"There are total {count_L} small L")

an = "Python is a Programming Language"
capitals = []
lower = []
for ch in an:
    if ch.isupper():
        capitals.append(ch)
    elif ch.islower():
        lower.append(ch)
print(f"{capitals}")
print(f"{lower}")

SBI_Akash_AC_details = {"Name" : "Akash",
                         "ATM PIN" : "7799"}
print("Welcome to SBI ATM")
print("pls insert your ATM card")
SBI_user_pin = input("plz enter your 4 digits ATM pin: ")
if len(SBI_user_pin) == 4:
    if SBI_user_pin in SBI_Akash_AC_details['ATM PIN']:
        print("The pin  correct")
    else:
        print("You have entered invalid pin")
else:
    print("plz enter 4 digit pin")
'''
per_num = int(input("Enter a number: "))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a  perfect num")








