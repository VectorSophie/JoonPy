import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())
primes = [i for i in range(M, N + 1) if is_prime(i)]

print(-1 if not primes else f"{sum(primes)}\n{min(primes)}")