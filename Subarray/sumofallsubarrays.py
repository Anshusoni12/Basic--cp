#index (i)= 0  1 2  3 4 5
#array    = 3 -2 4 -1 2 6
#S (i+1)  = 1  2 3  4 5 6
#E (N-i)  = 6  5 4  3 2 1
# Total   = 6 10 12 12 10 6

arr=list(map(int,input().split()))
ans=0
for i in range(len(arr)):
    total=(i+1)*(len(arr)-i)
    Contri=total*arr[i]
    ans+=Contri
print(ans)