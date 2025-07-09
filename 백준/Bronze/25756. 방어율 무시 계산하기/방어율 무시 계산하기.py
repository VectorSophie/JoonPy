n = int(input())
potions = list(map(int, input().split()))

v = 0.0

for a in potions:
    v = 1 - (1 - v) * (1 - a / 100)
    print(round(v * 100, 6))  
