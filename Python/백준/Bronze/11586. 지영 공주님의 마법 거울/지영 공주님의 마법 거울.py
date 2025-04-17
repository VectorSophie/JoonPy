N = int(input())
arr = [list(input().strip()) for _ in range(N)]
K = int(input())
if K == 1:
    for row in arr:
        print(''.join(row))
elif K == 2:
    for row in arr:
        print(''.join(row[::-1]))
elif K == 3:
    for row in reversed(arr):
        print(''.join(row))