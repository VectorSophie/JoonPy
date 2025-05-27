from collections import deque
N = int(input())
queue = deque(range(1, N + 1))
discarded = []
while len(queue) > 1:
    discarded.append(queue.popleft())  
    queue.append(queue.popleft()) 
print(*discarded,queue[0])