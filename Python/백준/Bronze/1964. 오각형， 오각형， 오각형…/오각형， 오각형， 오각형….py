sum = 0
n = int(input())
for i in range(1, n+1):
    sum += i*5
for i in range(1,n):
    sum -= (i+1)*2-1
print(sum%45678)