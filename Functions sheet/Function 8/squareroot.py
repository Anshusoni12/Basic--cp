import math
def perfect_square(A):
    root = int(math.sqrt(A))
    if root * root == A:
        return root
    else:
        return -1

print(perfect_square(25))
