# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()


n=13333338
d=3
count=0
while n>0:
    a=n%10
    if a==d:
        count=count+1
    n//=10
print(count)

# n=6
# for i in range(6,1,-1):
#     for j in range(n-i):
#         print(" ",end= " ")
#     for k in range(i-1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print("*",end=" ")
#     print()