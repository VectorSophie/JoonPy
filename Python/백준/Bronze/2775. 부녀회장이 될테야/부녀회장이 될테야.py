import math
def calc(k, n):
    return math.comb(n + k, k + 1)
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(calc(k,n))