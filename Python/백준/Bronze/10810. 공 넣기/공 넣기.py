N, M = map(int, input().split())  
arr = [0] * N  
output = []

for _ in range(M):
    a, b, c = map(int, input().split())  
    for j in range(a-1, b):  
        arr[j] = c
print(*arr)  

        
    