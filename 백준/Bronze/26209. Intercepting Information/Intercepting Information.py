N=list(map(int,input().split()))
print("S"if N.count(0)+N.count(1) == 8 else "F")