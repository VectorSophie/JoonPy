t = int(input())  

for _ in range(t):
    n = int(input())
    p1_wins = 0
    p2_wins = 0
    for _ in range(n):
        p1, p2 = input().split()
        if p1 == p2:
            continue 
        elif (p1 == 'R' and p2 == 'S') or \
             (p1 == 'S' and p2 == 'P') or \
             (p1 == 'P' and p2 == 'R'):
            p1_wins += 1
        else:
            p2_wins += 1
    if p1_wins > p2_wins:
        print("Player 1")
    elif p2_wins > p1_wins:
        print("Player 2")
    else:
        print("TIE")