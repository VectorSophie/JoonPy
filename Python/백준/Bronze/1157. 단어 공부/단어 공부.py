word = input().strip().upper()
alphabet = [0] * 26

for char in word:
    if 'A' <= char <= 'Z':  
        index = ord(char) - ord('A')
        alphabet[index] += 1

max_count = max(alphabet)
max_indices = [i for i, count in enumerate(alphabet) if count == max_count]

if len(max_indices) > 1:
    print("?")
else:
    print(chr(max_indices[0] + ord('A')))