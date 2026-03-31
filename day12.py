'''prime_num = 89
count = 0
# means check if it is divisible by only 1 and itself.
for j in range(1,prime_num+1,):
    print(j)
    if prime_num % j == 0:
        count += 1
        print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")

for i in range(2,10):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(f"{i} is a prime")
    else:
        print(f"{i} is not a prime")

a=[1057,197,9,86,17673]
for i in a:
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
           count += 1
    if count == 2:
        print(f"{i} is a prime")
    else:
        print(f"{i} is not a prime")

y = [2,356,8,6,3,2,8]
x = []
for i in y:
    if i not in x:
        x.append(i)
print(x)

a = [2,356,8,6,3,2,8]
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        for j in empty
'''
so = int(input("enter any number:"))
length_ = len(str(so))
Amstr_ =0
for j in str(so):
    Amstr_ += int(j) ** length_
    print(Amstr_)
if Amstr_ == so:
    print(f"{so} is Amstrong num")
else:
    print(f"{so} is not Amstrong num")






















