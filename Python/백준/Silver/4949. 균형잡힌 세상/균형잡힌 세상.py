def checker(enter) :
    stack = []

    for i in enter:
        if i in '([':
            stack.append(i)
        elif i in '])':
            if not stack:
                return "no"
            top = stack.pop()
            if (i == ')' and top != '(') or (i == ']' and top != '['):
                return "no"
            
    if not stack:
        return "yes"
    else:
        return "no"
    
while True:
    enter = input()
    if enter == ".":
        break
    else:
        print(checker(enter))