N=int(input())
arr=list(map(int,input().split()))
days=sum(arr)+(8*(N-1))
print(days//24,days%24)