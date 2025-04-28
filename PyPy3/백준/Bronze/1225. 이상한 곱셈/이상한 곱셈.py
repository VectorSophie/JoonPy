import sys
A, B = sys.stdin.readline().split()
result = 0
for a in A:
    for b in B:
        result += int(a) * int(b)
print(result)
