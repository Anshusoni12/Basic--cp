n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    s = 0
    for j in range(i, n):
        s += arr[j]
        print(s)