def is_valid(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_cnt = sum(1 for ch in password if ch in vowels)
    consonant_cnt = len(password) - vowel_cnt
    return vowel_cnt >= 1 and consonant_cnt >= 2

def backtrack(arr, L, start, path, results):
    if len(path) == L:
        if is_valid(path):
            results.append(''.join(path))
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        backtrack(arr, L, i + 1, path, results)
        path.pop()

L, C = map(int, input().split())
chars = input().split()
chars.sort()

results = []
backtrack(chars, L, 0, [], results)

for password in results:
    print(password)