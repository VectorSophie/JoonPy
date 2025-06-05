T = int(input())
for i in range(T):
    steps = input()
    count = 0
    for c in steps:
        if c == 'D':
            break
        count += 1
    print(count)
