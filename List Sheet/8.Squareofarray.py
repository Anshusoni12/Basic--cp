arr=list(map(int,input().split()))
B=[]
for i in range(len(arr)):
    arr[i]=arr[i]**2 
    B.append(arr[i])
print(B)