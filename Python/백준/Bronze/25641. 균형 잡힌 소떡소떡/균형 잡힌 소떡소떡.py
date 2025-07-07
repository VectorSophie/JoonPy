N = int(input())
st = input()

for i in range(N):
    sub = st[i:]  
    if sub.count('s') == sub.count('t') and sub.count('s') > 0:
        print(sub)
        break
