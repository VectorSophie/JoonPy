dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

for i in range(9):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == total - 100:
            excluded = [dwarfs[i], dwarfs[j]]
            result = [d for d in dwarfs if d not in excluded or excluded.remove(d)]
            result.sort()
            for height in result:
                print(height)
            exit()