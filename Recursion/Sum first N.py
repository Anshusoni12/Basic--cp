def sum_first_n(N):
    if N ==1:
        return 1
    return N+sum_first_n(N-1)

N =int(input())
print(sum_first_n(N))