grid = [list(map(int, input().split())) for _ in range(9)]
max_val = -1
max_row = 0
max_col = 0

for i in range(9):  
    for j in range(9): 
        if grid[i][j] > max_val:
            max_val = grid[i][j]
            max_row = i
            max_col = j

print(max_val)
print(max_row + 1, max_col + 1)