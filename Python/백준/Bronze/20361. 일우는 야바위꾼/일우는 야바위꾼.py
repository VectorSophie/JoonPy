N, X, K = map(int, input().split())
pos = X
for _ in range(K):
    A, B = map(int, input().split())
    pos = B if pos == A else A if pos == B else pos
print(pos)