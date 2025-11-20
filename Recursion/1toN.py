def print_1_to_n(N):
    if N == 0:
        return 
    print_1_to_n(N-1)
    print(N)
N=int(input())
print_1_to_n(N)