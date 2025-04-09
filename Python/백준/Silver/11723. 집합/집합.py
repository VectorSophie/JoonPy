import sys

S = set()

def check(x):
    return 1 if x in S else 0

def toggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def set_all():
    global S
    S = set(range(1, 21))

def empty():
    global S
    S = set()

M = int(sys.stdin.readline())

for _ in range(M):
    parts = sys.stdin.readline().split()
    cmd = parts[0]
    if cmd == 'add':
        S.add(int(parts[1]))
    elif cmd == 'remove':
        S.discard(int(parts[1]))
    elif cmd == 'check':
        print(check(int(parts[1])))
    elif cmd == 'toggle':
        toggle(int(parts[1]))
    elif cmd == 'all':
        set_all()
    elif cmd == 'empty':
        empty()