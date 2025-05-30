def explosion(s, bomb):
    arr = []
    bomb_len = len(bomb)

    for ch in s:
        arr.append(ch)
        if ''.join(arr[-bomb_len:]) == bomb:
            del arr[-bomb_len:]

    result = ''.join(arr)
    return result if result else "FRULA"

s = input().strip()
bomb = input().strip()

print(explosion(s, bomb))