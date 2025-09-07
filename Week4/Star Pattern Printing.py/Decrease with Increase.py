#For Upper Half Triangle
n=int(input("Enter number of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#For Lower Half Triangle
for i in range(2,n+1):
    for j in range(1,i+1):
        print("*",end= " ")
    print()