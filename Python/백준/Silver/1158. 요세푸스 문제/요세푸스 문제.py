import sys
def josephus(n, k):
    q = [i for i in range(1, n + 1)]
    result = []
    index = 0
    while q:
        index = (index + k - 1) % len(q)
        result.append(q.pop(index))
    return result
N, K = map(int, sys.stdin.readline().split())
result = str(josephus(N, K))
rere = result.replace("[", "<").replace("]", ">")
print(rere)