s = input().rstrip()
comp = "ABBDOPQRabdegopq@"  

ans = 0
for c in s:
    ans += comp.count(c)

print(ans)
