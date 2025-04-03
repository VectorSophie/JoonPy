T=int(input())
for i in range(T):
    total = 0
    o=0
    ox=list(map(str,input()))
    for i in range(len(ox)):
        if ox[i]=='O':
            o+=1
            total+=o
        elif ox[i]=='X':
            o=0
    print(total)