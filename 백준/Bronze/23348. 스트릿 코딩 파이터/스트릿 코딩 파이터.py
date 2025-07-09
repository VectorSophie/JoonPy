A, B, C = map(int, input().split())
N = int(input())

max_score = 0

for _ in range(N):
    club_score = 0
    for _ in range(3):  
        a, b, c = map(int, input().split())
        member_score = A * a + B * b + C * c
        club_score += member_score
    max_score = max(max_score, club_score)

print(max_score)