arr = input()
digitsum = sum(map(int, arr))
cnt = 1 if len(arr) > 1 else 0

while digitsum >= 10:
    digitsum = sum(map(int, str(digitsum)))
    cnt += 1
print(cnt)
if digitsum % 3 == 0:
    print("YES")
else:
    print("NO")