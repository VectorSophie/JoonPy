N = int(input())  
K = input()       
even = 0
odd = 0

for digit in K:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)