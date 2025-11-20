B=int(input("Enter the number: "))
c=0
print("Enter array elements: ")
A=list(map(int,input().split()))
N=len(A)
for i in range(N):
    s=0
    for j in range(i,N):
        s+=A[j]
        if s<B:
            c+=1
print("Number of subarrays is ",c)