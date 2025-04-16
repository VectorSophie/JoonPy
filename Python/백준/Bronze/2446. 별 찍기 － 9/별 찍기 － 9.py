N = int(input())

for n in range(N):
    print(" " * n + "*" * (2 * (N - n) - 1))

for n in range(1, N):
    print(" " * (N - n - 1) + "*" * (2 * n + 1))
