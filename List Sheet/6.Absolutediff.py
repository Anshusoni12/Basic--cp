arr=list(map(int,input().split()))
even_count=0
odd_count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even_count+=1
    else:
        odd_count+=1

absolute =(even_count-odd_count)
print(absolute)


