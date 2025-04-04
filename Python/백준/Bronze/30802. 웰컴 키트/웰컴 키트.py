import math

N = int(input())
arr = list(map(int,input().split()))
T, P = map(int,input().split())
cnt = 0
for i in range(len(arr)):
    cnt += math.ceil(arr[i] / T)
print(cnt)
print(N//P, N%P)