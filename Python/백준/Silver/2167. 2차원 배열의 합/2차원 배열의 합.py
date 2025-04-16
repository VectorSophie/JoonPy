import sys
N,M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    total = 0
    i,j,x,y = map(int,sys.stdin.readline().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    for m in range(i, x + 1):  
        total += sum(arr[m][j:y + 1])  
    
    print(total)

    