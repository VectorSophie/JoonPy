cnt, x = map(int,input().split())
arr = list(map(int,input().split()))
new_arr = []
for i in range(len(arr)):
    if arr[i] < x:
        new_arr.append(arr[i])
    else:
        continue
print(*new_arr)