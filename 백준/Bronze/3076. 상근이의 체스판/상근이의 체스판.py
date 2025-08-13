import sys

R, C = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())

for r in range(R):
    row = []
    for c in range(C):
        ch = 'X' if (r + c) % 2 == 0 else '.'
        row.append(ch * B)   
    line = ''.join(row)
    for _ in range(A):
        print(line)