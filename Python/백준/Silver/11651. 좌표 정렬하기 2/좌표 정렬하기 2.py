N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arr = sorted(arr, key=lambda x: (x[1],x[0]) ) 

for row in arr:
    print(" ".join(map(str, row))) 