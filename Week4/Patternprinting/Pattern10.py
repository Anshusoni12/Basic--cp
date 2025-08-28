n=int(input("Enter the number:")) 
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*(n-i)-2):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()