N = int(input())
levels = list(map(int, input().split()))

result = []
for M in levels:
    if M == 300:
        result.append(1)
    elif 275 <= M < 300:
        result.append(2)
    elif 250 <= M < 275:
        result.append(3)
    else:
        result.append(4)
print(*result)