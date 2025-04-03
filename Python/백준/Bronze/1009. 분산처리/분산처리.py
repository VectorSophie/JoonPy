import sys

t = int(sys.stdin.readline()) 

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())  
    result = pow(a, b, 10) 
    print(result if result != 0 else 10)