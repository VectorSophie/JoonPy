T = int(input())
for t in range(1, T+1):
    N = int(input())
    h = list(map(float, input().split()))
    for i in range(1, N-1):
        h[i] = min(h[i], (h[i-1] + h[i+1]) / 2)
    print(f"Case #{t}: {h[-2]:.6f}")