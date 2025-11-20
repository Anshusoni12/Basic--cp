def fib(N):
    if N <=1:
        return N
    return fib(N-1)+fib(N-2)

N=int(input())
print(fib(N))