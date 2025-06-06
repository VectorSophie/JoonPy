def counter(trophies):
    max_height = 0
    visible = 0
    for height in trophies:
        if height > max_height:
            visible += 1
            max_height = height
    return visible

N = int(input())
trophies = [int(input()) for _ in range(N)]

print(counter(trophies))
print(counter(reversed(trophies)))