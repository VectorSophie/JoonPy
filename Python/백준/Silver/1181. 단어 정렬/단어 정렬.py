N = int(input())
arr = [input() for _ in range(N)]
unique_sorted = sorted(set(arr), key=lambda x: (len(x), x))
for i in unique_sorted:
    print(i)
