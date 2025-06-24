jinho = input().strip()

n = int(input())

cnt = 0
for _ in range(n):
    friend = input().strip()
    if friend == jinho:
        cnt += 1

print(cnt)