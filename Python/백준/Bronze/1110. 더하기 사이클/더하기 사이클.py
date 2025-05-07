def cycle_length(N):
    original = N
    count = 0
    while True:
        count += 1
        N = (N % 10) * 10 + ((N // 10 + N % 10) % 10)
        if N == original:
            break
    return count
N = int(input())
print(cycle_length(N))