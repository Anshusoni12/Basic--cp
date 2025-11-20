n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i, n):
        print(arr[i : (j+1)])