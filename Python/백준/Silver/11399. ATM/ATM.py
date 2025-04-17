N = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
cur = 0
for i in range(len(arr)):
    cur = arr[i] + cur
    result += cur
print(result)
