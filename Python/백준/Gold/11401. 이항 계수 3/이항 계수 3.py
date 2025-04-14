MOD = 10**9 + 7

def factorial(n):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    return fact

def inverse(x):
    return pow(x, MOD - 2, MOD)

def coeff(n, k):
    if k < 0 or k > n:
        return 0
    fact = factorial(n)
    num = fact[n]
    denom = (fact[k] * fact[n - k]) % MOD
    return (num * inverse(denom)) % MOD

n, k = map(int, input().split())
print(coeff(n, k))