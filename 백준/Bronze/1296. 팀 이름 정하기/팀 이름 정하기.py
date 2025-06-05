def calculate_probability(name1, name2):
    combined = name1 + name2
    L = combined.count('L')
    O = combined.count('O')
    V = combined.count('V')
    E = combined.count('E')
    score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    return score

yeondu = input().strip()
n = int(input())
teams = [input().strip() for _ in range(n)]
best = ''
max_score = -1

for team in teams:
    score = calculate_probability(yeondu, team)
    if score > max_score or (score == max_score and team < best):
        max_score = score
        best = team

print(best)