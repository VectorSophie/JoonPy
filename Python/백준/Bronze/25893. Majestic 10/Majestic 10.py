n = int(input())
for _ in range(n):
    stats_line = input()
    stats = list(map(int, stats_line.split()))
    count = sum(1 for stat in stats if stat >= 10)

    print(stats_line)
    if count == 0:
        print("zilch")
    elif count == 1:
        print("double")
    elif count == 2:
        print("double-double")
    elif count == 3:
        print("triple-double")
    print()  