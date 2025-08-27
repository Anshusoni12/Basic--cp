n=int(input("Enter the number:"))
x=1
for i in range(n):
    for j in range(1,i+1):
        print(x,end=" ")
        x+=1
    print()