T = int(input())

def adder(a,b):
    return a+b

for i in range(T):
    A, B = map(int, input().split())
    print(adder(A,B))
    