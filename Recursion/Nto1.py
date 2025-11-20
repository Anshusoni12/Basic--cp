def print_n_to_1(N):
    if N == 0:
        return
    print(N)
    print_n_to_1(N-1)
N = int(input())
print_n_to_1(N)