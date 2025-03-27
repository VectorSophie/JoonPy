enter = int(input())
if (enter % 4 == 0 and not enter % 100 == 0) or enter % 400 == 0:
    print(1)
else:
    print(0)