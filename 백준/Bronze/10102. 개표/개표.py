V=int(input())
vote=input()
print("A"if vote.count("A")>(V//2) else("B" if vote.count("B")>(V//2) else "Tie"))