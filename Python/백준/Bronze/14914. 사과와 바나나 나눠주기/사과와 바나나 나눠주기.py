import sys
a,b = map(int,sys.stdin.readline().split())
for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        print(i, a//i, b//i)