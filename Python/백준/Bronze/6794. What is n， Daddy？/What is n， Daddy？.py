n = int(input())
count = 0

for a in range(0, 6):       
    for b in range(0, 6):   
        if a + b == n and a >= b:
            count += 1
print(count)