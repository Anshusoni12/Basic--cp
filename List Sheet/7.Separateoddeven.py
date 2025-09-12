arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]%2==0:
        print(arr[i],end=" ")
print()

for i in range(len(arr)):
    if arr[i]%2!=0:
        print(arr[i],end=" ")
print()
    


