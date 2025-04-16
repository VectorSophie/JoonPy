import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
seen = set()
cnt = 0
for num in arr:
    if x - num in seen:
        cnt += 1
    seen.add(num)
print(cnt)
