import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = float('-inf')
for i in range(N-K+1):
    new = sum(arr[i:i+K])
    result = max(result,new)
print(result)