A, B, N = map(int, input().split())
remnant = A % B

for i in range(N):
    remnant *= 10
    digit = remnant // B
    remnant %= B

print(digit)