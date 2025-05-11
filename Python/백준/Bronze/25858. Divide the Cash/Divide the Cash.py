n, d = map(int, input().split())
problems = [int(input()) for _ in range(n)]
total = sum(problems)
reward = d // total

for solved in problems:
    print(solved * reward)
