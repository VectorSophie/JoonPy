while True:
    enter = int(input())
    if enter == 0:
        break
    else:
        if str(enter) == str(enter)[::-1]:
            print("yes")
        else:
            print("no")