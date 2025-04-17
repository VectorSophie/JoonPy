import sys
n = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split()))
list2 = list(map(int,sys.stdin.readline().split()))
list3 = list(map(int,sys.stdin.readline().split()))
if 7 in list1 and 7 in list2 and 7 in list3:
    print("777")
else:
    print("0")
