N = int(input())

for i in range(1, 2 * N):
    stars = i if i <= N else 2 * N - i
    print('*' * stars)
