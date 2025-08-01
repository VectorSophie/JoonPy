a, b, n, w = map(int, input().split())
solutions = []

for x in range(1, n):
    if a * x + b * (n - x) == w:
        solutions.append((x, n-x))

if len(solutions) == 1:
    print(solutions[0][0], solutions[0][1])
else:
    print(-1)
