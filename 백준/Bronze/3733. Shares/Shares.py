while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():  
        break
    enter = list(map(int, line.split()))
    print(enter[1] // (enter[0] + 1))

