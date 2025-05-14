def valid(n, m):
    count = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            numerator = a * a + b * b + m
            denominator = a * b
            if numerator % denominator == 0:
                count += 1
    return count
T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    print(valid(n,m))