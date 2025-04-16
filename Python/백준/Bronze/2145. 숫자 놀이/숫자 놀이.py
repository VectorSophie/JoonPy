while True:
    enter = int(input())
    if enter == 0:
        break
    while len(str(enter)) != 1: 
        enter = sum(int(digit) for digit in str(enter))
    print(enter)