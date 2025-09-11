#Given an array find the maximum value in it
arr=list(map(int,input().split()))       
max=arr[0]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]> max and arr[i]> min:
        max=arr[i]
    else:
        min=arr[i]
print(max , min)



# #Another method

# Ans = -float("inf")
# for i in arr:
#     if (Ans<i):
#         Ans=1
# print(Ans)