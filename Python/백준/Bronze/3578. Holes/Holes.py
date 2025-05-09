def holes(h):
    if h == 0:
        return '1'  
    elif h == 1:
        return '0'
    result = ''
    if h % 2 == 0:
        result = '8' * (h // 2)
    else:
        result = '4' + '8' * (h // 2)
    return result
h=int(input())
print(holes(h))