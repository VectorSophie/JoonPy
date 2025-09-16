import sys
data = list(map(int, sys.stdin.read().split()))
T = data[0]
ans = []
for i in range(1, 1 + T):
    x = data[i]
    ans.append(str(2 * x - 1))
print('\n'.join(ans))