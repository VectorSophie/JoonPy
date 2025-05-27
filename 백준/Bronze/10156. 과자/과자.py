K,N,M = map(int,input().split())
status = K*N>=M
print(K*N-M if status else 0)