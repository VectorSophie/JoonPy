X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    numer = X
    denom = line - X + 1
else:
    numer = line - X + 1
    denom = X

print(f"{numer}/{denom}")