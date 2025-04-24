def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
n = int(input())
print(fibonacci(n)%10007)