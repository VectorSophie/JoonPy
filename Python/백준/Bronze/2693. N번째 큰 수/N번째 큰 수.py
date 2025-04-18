import sys
T = int(input())
for i in range(T):
    arr=list(map(int,sys.stdin.readline().split()))
    arr.sort(reverse=True)
    print(arr[2])