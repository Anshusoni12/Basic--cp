def countdigit(N):
    if N ==0:
        return 0
    return 1 + countdigit(N//10)

N=int(input())
print(countdigit(N))