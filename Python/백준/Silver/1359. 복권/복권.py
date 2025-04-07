import math

def coeff(n,m):
    if m>n:
        return 0
    return math.factorial(n) // (math.factorial(m) * math.factorial(n-m))

N,M,K = map(int,input().split())

result = sum((coeff(M,i)*coeff(N-M,M-i)) / coeff(N,M) for i in range(K,M+1))
print(f"{result:.10f}")