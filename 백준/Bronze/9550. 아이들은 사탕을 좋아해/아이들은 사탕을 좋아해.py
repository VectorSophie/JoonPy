T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    result = sum(c // K for c in candies)
    print(result)