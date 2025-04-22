import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    drink = {S: int(L) for S, L in (input().split() for _ in range(N))}
    sorted_drink = sorted(drink.items(), key=lambda x: x[1], reverse=True)
    print(sorted_drink[0][0])