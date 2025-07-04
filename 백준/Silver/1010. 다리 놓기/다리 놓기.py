from math import comb

T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    print(comb(N,M))
