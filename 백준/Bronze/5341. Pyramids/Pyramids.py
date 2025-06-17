while True:
    enter=int(input())
    sum = 0
    if enter == 0:
        break;
    else:
        for i in range(1,enter+1):
            sum += i
        print(sum)