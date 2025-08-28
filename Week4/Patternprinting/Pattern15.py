#For Upper Part of Triangle

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

#For Lower Part of Triangle

for i in range(1,n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()

