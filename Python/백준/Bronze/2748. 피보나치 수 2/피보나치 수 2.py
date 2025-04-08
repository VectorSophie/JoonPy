N=int(input())
fibo=[0,1,1]
for x in range(3,N+1):
    fibo.append(fibo[x-2]+fibo[x-1])
print(fibo[N])