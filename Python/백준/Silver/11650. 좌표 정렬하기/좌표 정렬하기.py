N = int(input())
arr = []
for i in range(N):
    a, b = map(int,input().split())
    arr.append((a,b))
sort_arr = sorted(arr)
for A,B in sort_arr:
    print(A, B)
    