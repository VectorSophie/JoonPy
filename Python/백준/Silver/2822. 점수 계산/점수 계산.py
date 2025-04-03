li = []
arr = []

for i in range(8):
    li.append((int(input()), i + 1))  

li.sort(reverse=True, key=lambda x: x[0])

arr = [x[1] for x in li[:5]]
arr.sort()  

print(sum(x[0] for x in li[:5]))
print(*arr)
