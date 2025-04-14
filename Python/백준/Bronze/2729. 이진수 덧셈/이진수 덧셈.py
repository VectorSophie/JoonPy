N = int(input())
for i in range(N):
    bin1, bin2 = input().split()
    result = bin(int(bin1, 2) + int(bin2, 2))[2:]
    print(result)