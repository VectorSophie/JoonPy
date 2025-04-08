def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    print(gcd(A,B))