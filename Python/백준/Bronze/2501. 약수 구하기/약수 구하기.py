N, K = map(int, input().split())
div = []

for i in range(1, N + 1):
    if N % i == 0:
        div.append(i)
print(div[K-1] if len(div)>=K else 0)