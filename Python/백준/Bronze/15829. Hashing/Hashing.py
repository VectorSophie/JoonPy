L = int(input())
word = input()
sum = 0

for i in range(L):
    current = ord(word[i]) - 96
    sum += current * (31 ** i)

print(sum%1234567891)