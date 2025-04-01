total = int(input())
amount = int(input())
total_cnt = 0  # Initialize total_cnt to 0

for i in range(amount):
    A, B = map(int, input().split())
    total_cnt += A * B

if total == total_cnt:
    print("Yes")
else:
    print("No")