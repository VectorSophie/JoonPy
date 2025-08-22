n = input().strip()

steps = 0
while len(n) > 1: 
    product = 1
    for digit in n:
        product *= int(digit)
    n = str(product)
    steps += 1
print(steps)
