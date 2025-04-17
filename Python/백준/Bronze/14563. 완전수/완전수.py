import sys
T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    divs = []
    for j in range(1, i):
        if i % j == 0:
            divs.append(j)
    if sum(divs) == i:
        print("Perfect")
    elif sum(divs) > i:
        print("Abundant")
    else:
        print("Deficient")
