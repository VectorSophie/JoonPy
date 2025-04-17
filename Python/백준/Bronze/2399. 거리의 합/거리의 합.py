import sys
n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
x.sort()

prefix = 0
total = 0

for i in range(n):
    total += x[i] * i - prefix
    prefix += x[i]

print(total * 2)