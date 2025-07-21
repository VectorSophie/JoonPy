N, C = map(int, input().split())
A, B = N, N  

for _ in range(C):
    X, Y = map(int, input().split())
    if X >= A or Y >= B:
        continue  
    horizontal = X * B
    vertical = A * Y

    if horizontal >= vertical:
        A = X 
    else:
        B = Y 

print(A * B)