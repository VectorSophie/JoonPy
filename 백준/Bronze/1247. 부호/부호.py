for _ in range(3):
    N=int(input())
    narr=[]
    for _ in range(N):
        narr.append(int(input()))
    print(0 if sum(narr)==0 else("+" if sum(narr)>0 else "-"))