def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
def lcm(a,b):
    g = gcd(a,b)
    return a*b//g
       
N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    print(lcm(A,B))