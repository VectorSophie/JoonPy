N = int(input())
n, m = 0,0
cmd = input()
arr = [['.' for _ in range(N)] for _ in range(N)]

def update(y, x, char):
    if arr[y][x] == '.':
        arr[y][x] = char
    elif arr[y][x] != char:
        arr[y][x] = '+'

for c in cmd:
    ny, nx = n, m
    if c == 'U' and n - 1 >= 0:
        update(n, m, '|')    
        n -= 1
        update(n, m, '|')    
    elif c == 'D' and n + 1 < N:
        update(n, m, '|')
        n += 1
        update(n, m, '|')
    elif c == 'L' and m - 1 >= 0:
        update(n, m, '-')
        m -= 1
        update(n, m, '-')
    elif c == 'R' and m + 1 < N:
        update(n, m, '-')
        m += 1
        update(n, m, '-')

for row in arr:
    print(''.join(row))