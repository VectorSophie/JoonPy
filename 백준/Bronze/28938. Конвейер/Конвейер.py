n = int(input())
sequence = list(map(int, input().split()))
total = sum(sequence)

print("Right" if total>0 else ("Left" if total<0 else "Stay"))
