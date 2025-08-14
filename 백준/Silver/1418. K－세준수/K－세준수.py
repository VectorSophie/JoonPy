N, K = int(input()), int(input())

sejun = [True] * (N + 1)
sejun[0] = False  

for p in range(K + 1, N + 1):
    if all(p % d for d in range(2, int(p ** 0.5) + 1)):  
        sejun[p:N+1:p] = [False] * ((N - p) // p + 1)  
print(sum(sejun))