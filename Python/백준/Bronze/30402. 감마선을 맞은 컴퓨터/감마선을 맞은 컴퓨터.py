arr = [input().split() for _ in range(15)]

if any('b' in row for row in arr):
    print('nabi')
elif any('w' in row for row in arr):
    print('chunbae')
else:
    print('yeongcheol')
