X=int(input())
arr = [64]
while True:
    if sum(arr) > X:
        arr.sort()
        smallest = arr[0]
        arr.remove(smallest)
        arr.append(smallest // 2)
        
        if sum(arr) < X:
            arr.append(smallest // 2)
    else:
        break

print(len(arr))