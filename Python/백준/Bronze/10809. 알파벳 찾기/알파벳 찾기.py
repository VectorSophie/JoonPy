arr = [chr(i) for i in range(97,123)]
N = input().strip()

for i in range(26):
    if arr[i] in N:
        print(N.index(arr[i]))
    else:
        print(-1)