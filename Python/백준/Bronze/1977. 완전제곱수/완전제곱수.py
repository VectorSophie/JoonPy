import math

A = int(input())
B = int(input())
arr = []

for i in range(A, B + 1):
    if math.sqrt(i).is_integer():
        arr.append(i)

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
    