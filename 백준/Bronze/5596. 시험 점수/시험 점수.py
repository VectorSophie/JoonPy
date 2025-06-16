s=sum(map(int,input().split()))
t=sum(map(int,input().split()))
print(max(s,t) if t>s else s)