n = 0
while True:
    try:
        input()
        n += 1
    except EOFError:
        break
print(n)
