N = int(input())
S = input()

vowels = {'a', 'i', 'u', 'e', 'o'}
count = sum(1 for c in S if c in vowels)

print(count)