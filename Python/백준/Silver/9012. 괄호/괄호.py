def checkParen(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"
N = int(input())
for i in range (N):
    enter = input()
    print(checkParen(enter))