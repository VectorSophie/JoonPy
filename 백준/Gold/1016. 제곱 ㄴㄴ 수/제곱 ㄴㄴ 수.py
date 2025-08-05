import math

min_val, max_val = map(int, input().split())
length = max_val - min_val + 1
freedom = [True] * length

for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i
    start = ((min_val + square - 1) // square) * square
    for j in range(start, max_val + 1, square):
        freedom[j - min_val] = False

print(sum(freedom))