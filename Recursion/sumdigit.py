def sumdigit(N):
    if N == 0:
        return 0
    return (N % 10) + sumdigit(N // 10)

N = int(input())
print(sumdigit(N))