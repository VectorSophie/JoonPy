N, M = map(int, input().split())
board = [input() for _ in range(N)]

def cnt_re(x, y, start):
    re = 0
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            expect = start if (i + j) % 2 == 0 else ('B' if start == 'W' else 'W')
            if current != expect:
                re += 1
    return re

min_re = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        re_w = cnt_re(i, j, 'W')
        re_b = cnt_re(i, j, 'B')
        min_re = min(min_re, re_w, re_b)
print(min_re)