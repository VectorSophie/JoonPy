from collections import Counter
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
cards = list(map(int, data[1:N+1]))
M = int(data[N+1])
query= list(map(int, data[N+2:]))

counter = Counter(cards)

result = [str(counter[q]) for q in query]
print(' '.join(result))