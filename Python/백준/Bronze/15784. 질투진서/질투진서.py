N, a, b = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

a -=1
b -=1
jin = X[a][b]

for i in range(N):
    if X[i][b] > jin:
        print("ANGRY")
        exit()
        
for j in range(N):
    if X[a][j] > jin:
        print("ANGRY")
        exit()

print("HAPPY")