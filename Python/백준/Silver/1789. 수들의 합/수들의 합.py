S = int(input())

low, high = 1, S
result = 0

while low <= high:
    mid = (low + high) // 2
    total = mid * (mid + 1) // 2

    if total <= S:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
