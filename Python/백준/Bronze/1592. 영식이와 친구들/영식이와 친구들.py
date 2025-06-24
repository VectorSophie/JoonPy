def balls(N, M, L):
    cnt = [0] * N 
    current = 0       
    throws = 0        

    while True:
        cnt[current] += 1
        if cnt[current] == M:
            break

        if cnt[current] % 2 == 1:
            current = (current + L) % N
        else:
            current = (current - L + N) % N
        throws += 1
    return throws

N, M, L = map(int, input().split())
print(balls(N, M, L))