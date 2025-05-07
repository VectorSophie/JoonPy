n = int(input())
if n == 1:
    print(1)
else:
    r = 1
    total = 1
    while total < n:
        total += 6 * r
        r += 1
    print(r)