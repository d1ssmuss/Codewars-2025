import math
def largest_power(N):
    a = int(math.log(N, 3))
    if 3 ** a == N:
        return a - 1
    else:
        return a

print(largest_power(28))