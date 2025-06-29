S0, N, M = map(int, input().split())
commands = [int(input()) for _ in range(N + M)]
S = S0  
U = 0  

for cmd in commands:
    if cmd == 1:
        if U == S:
            S *= 2
        U += 1
    else:
        U -= 1

print(S)