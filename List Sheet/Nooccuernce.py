# Given an array and a target number find number of occurence of target no in given array.
arr=list(map(int,input().split()))
tar_no=5
count=0
for i in range(len(arr)):
    if arr[i]==tar_no:
        count+=1
print(count)