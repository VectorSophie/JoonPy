def primes(N):
    i = 2
    while i * i <= N:
        while N % i == 0:
            print(i)
            N //= i
        i += 1
    if N > 1:
        print(N)

N = int(input())
primes(N)