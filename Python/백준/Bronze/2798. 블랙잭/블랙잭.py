N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

maxsum = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            cursum = arr[i] + arr[j] + arr[k]
            if cursum <= M:
                maxsum = max(maxsum, cursum)
print(maxsum)