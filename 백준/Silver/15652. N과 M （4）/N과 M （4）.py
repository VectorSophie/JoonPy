from itertools import combinations_with_replacement
import sys

N, M = map(int, sys.stdin.readline().split())

for seq in combinations_with_replacement(range(1, N + 1), M):
    print(*seq)
