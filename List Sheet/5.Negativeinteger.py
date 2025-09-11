#Another method
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]<0:
        print(arr[i])
        