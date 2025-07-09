max_count = -1
max_name = ""

for _ in range(7):
    name, count = input().split()
    count = int(count)
    if count > max_count:
        max_count = count
        max_name = name

print(max_name)