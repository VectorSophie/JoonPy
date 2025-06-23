T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    c = a + b
    for i in range(1, 51):
        if i != c:
            print(i)
            break