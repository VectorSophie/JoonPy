N = int(input())
result = 0
for M in range(1, N):
    digit_sum = sum(map(int, str(M)))  
    if M + digit_sum == N:
        result = M
        break  
print(result)