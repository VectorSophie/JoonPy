N, M = map(int, input().split())
setN = set()
setM = set()

for _ in range(N):
    setN.add(input())

for _ in range(M):
    setM.add(input())

result = sorted(setN & setM)  

print(len(result))
for name in result:
    print(name)

