#Given a list of integer and a target num find and print the index of a target no
arr=list(map(int,input().split()))
tar_no=int(input("Enter a no:"))
for i in range(len(arr)):
   if arr[i] ==tar_no:
      print(i)