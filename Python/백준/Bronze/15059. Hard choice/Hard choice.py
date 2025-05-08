Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
not_served = 0

if Cr > Ca:
    not_served += Cr - Ca
if Br > Ba:
    not_served += Br - Ba
if Pr > Pa:
    not_served += Pr - Pa

print(not_served)