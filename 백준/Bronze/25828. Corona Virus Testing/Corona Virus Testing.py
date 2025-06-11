g, p, t = map(int, input().split())

n = g * p
m = g + (t * p)
print(1 if n < m else 2 if n > m else 0)