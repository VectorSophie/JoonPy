R,C = map(int,input().split())
arr = [input() for _ in range(R)]

tempR = 0
tempC = 0

for i in range(R):
    if 'X' not in arr[i]:
        tempC += 1

for j in range(C):
    if all(arr[i][j] != 'X' for i in range(R)):
        tempR += 1
        
print(max(tempR, tempC))