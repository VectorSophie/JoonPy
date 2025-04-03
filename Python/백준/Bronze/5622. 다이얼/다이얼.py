dial = input()
time = 0
for x in dial :
    if 65 <= ord(x) < 68 :
        time += 3
    if 68 <= ord(x) < 71 :
        time += 4
    if 71 <= ord(x) < 74 :
        time += 5
    if 74 <= ord(x) < 77 :
        time += 6
    if 77 <= ord(x) < 80 :
        time += 7
    if 80 <= ord(x) < 84 :
        time += 8
    if 84 <= ord(x) < 87 :
        time += 9
    if 87 <= ord(x) < 91 :
        time += 10
print(time)