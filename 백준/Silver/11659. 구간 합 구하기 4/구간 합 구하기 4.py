import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (N + 1)
for idx in range(1, N + 1):
    prefix[idx] = prefix[idx - 1] + arr[idx - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
