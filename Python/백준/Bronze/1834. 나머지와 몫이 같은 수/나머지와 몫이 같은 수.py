def divmod(N):
    total = 0
    for r in range(1, N):
        x = r * (N + 1)
        total += x
    return total

N = int(input())
print(divmod(N))
