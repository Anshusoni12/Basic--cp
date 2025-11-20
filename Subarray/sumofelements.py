n = int(input())
arr = list(map(int,input().split()))
l, r = map(int,input().split())
l -= 1
r -= 1
total = sum(arr[l:r+1])
print(total)