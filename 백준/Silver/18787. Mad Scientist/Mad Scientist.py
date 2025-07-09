n=int(input())
A=input()
B=input()
cnt=0
i=0
while i<n:
    if A[i]!= B[i]:
        cnt+=1
        while i<n and A[i]!=B[i]:
            i+=1
    else:
        i+=1
print(cnt)