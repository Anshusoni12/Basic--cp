n=int(input("Enter the number "))
for i in range(n):
    for j in range(7-i):
        if j==0 or j==6-i:
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()
