while True:
    enter = input()
    if enter == '0':
        break
    cnt = 0
    for i in enter:
        if i =='0':
            cnt+=4
        elif i == '1':
            cnt+=2
        else:
            cnt+=3
    print(len(enter)+cnt+1)