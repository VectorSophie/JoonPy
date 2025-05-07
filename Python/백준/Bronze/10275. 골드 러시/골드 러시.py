t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    print(bin(a).count('1') + bin(b).count('1') - 1)