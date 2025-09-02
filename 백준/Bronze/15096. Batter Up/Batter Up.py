n=int(input())
atts=list(map(int, input().split()))
print(sum(x for x in atts if x>=0)/sum(1 for x in atts if x>=0))