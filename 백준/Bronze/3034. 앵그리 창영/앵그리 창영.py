import sys

data = sys.stdin.read().strip().split()
it = iter(data)
N, W, H = map(int, [next(it), next(it), next(it)])
limit = W*W + H*H

out = []
for _ in range(N):
    L = int(next(it))
    out.append("DA" if L*L <= limit else "NE")
print("\n".join(out))