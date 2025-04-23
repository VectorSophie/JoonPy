p, r = map(int, input().split())
v = p / r
print("weak" if v < 0.2 else "normal" if 0.2 <= v < 0.4 else "strong" if 0.4 <= v < 0.6 else "very strong")