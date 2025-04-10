import sys

N, K = map(int, input().split())
value = []

for i in range(N):
    enter = int(sys.stdin.readline())
    value.append(enter)

value.sort(reverse=True)  

cnt = 0
for j in value:
    if j <= K:
        cnt += K // j
        K = K % j
    if K == 0:
        break

print(cnt)