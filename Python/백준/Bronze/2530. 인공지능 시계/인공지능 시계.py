A,B,C = map(int, input().split())
D = int(input())

C += D % 60
B += D // 60

if C >= 60:
    C -= 60
    B += 1

if B >= 60:
    A += B // 60
    B %= 60

if A >= 24:
    A %= 24

print(A,B,C)
