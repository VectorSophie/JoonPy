N = int(input())

fib = [0] * (N+2)
fib[1] = 1
for i in range(2, N+2):
    fib[i] = fib[i-1] + fib[i-2]
print(2 * (2*fib[N] + fib[N-1]))