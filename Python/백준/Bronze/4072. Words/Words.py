while True:
    line = input()
    if line == "#":
        break
    restored_line = ' '.join(word[::-1] for word in line.split())
    print(restored_line)