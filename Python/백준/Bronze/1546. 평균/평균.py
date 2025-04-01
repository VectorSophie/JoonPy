n = int(input())
g = list(map(int,input().split()))
m = max(g)
g_rigg = [(i/m) * 100 for i in g]
print(sum(g_rigg)/len(g_rigg))