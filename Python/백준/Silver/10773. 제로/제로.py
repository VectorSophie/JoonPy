import collections

K = int(input())
arr = collections.deque()
for _ in range(K):
    enter = int(input())
    if enter == 0:
        arr.pop()
    else:
        arr.append(enter)
print(sum(arr))
        