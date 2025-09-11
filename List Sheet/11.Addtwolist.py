arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
A=[]
for i in range(len(arr)):
    A.append(arr[i]+arr1[i])
print(A)