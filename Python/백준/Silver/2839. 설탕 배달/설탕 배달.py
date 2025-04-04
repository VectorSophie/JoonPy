N = int(input())
min_bag = float('inf') 

for i in range(N // 5 + 1):
    for j in range(N // 3 + 1):
        if i * 5 + j * 3 == N:
            min_bag = min(min_bag, i + j)

print(min_bag if min_bag != float('inf') else -1)