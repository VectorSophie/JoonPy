from collections import Counter

room = input()
counter = Counter(room)

count_69 = counter.get('6', 0) + counter.get('9', 0)
counter['6'] = (count_69 + 1) // 2
counter['9'] = 0

print(max(counter.values()))