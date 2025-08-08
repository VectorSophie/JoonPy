N = int(input())
best_sum = -1

for _ in range(N):
    A, B, C = map(int, input().split())
    total = A + B + C
    
    if total >= 512:
        if best_sum == -1 or total < best_sum:
            best_sum = total

print(best_sum)