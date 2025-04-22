import sys
P = int(sys.stdin.readline())
for _ in range(P):
    N,D,A,B,F = map(float,input().split())
    print(int(N), round((D/(A+B))*F,6))