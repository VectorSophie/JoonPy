import sys
arr=[]
N = int(sys.stdin.readline())
for i in range(N):
    enter = list(sys.stdin.readline().split())
    cmd = enter[0]
    if cmd == "push":
        arr.append(enter[1])
    elif cmd == "pop":
        print(arr.pop() if arr else -1)
    elif cmd == "size":
        print(len(arr))
    elif cmd == "empty":
        print(1 if len(arr) == 0 else 0)
    elif cmd == "top":
        print(arr[-1] if arr else -1)