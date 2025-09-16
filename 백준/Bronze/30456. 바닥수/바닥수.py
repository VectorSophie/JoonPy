import sys
N, L = map(int, sys.stdin.read().split())

if N == 0:
    print("1" + "0"*(L-1))
else:
    print(str(N) + "1"*(L-1))
