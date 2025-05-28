arr = [input() for _ in range(6)]
cnt = arr.count('W')
if cnt <= 0:
    print(-1)
elif cnt == 5 or cnt == 6:
    print(1)
elif cnt == 4 or cnt == 3:
    print(2)
else:
    print(3)