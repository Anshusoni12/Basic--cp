# Another method with empty array
arr=list(map(int,input().split()))
inc_value=int(input("Enter a number:"))
for i in range(len(arr)):
    arr[i]=arr[i]+inc_value
print(arr)
