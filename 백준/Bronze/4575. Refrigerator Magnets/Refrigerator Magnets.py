while True:
    line = input().strip()
    if line == "END":
        break
    letters = line.replace(" ", "")
    if len(set(letters)) == len(letters):
        print(line)
