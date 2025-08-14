days_in_month = {
    1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
    4: 30, 6: 30, 9: 30, 11: 30,
    2: 29
}

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    time  = (0 <= x <= 23) and (0 <= y <= 59)
    date= (1 <= x <= 12) and (1 <= y <= days_in_month.get(x, 0))
    print("Yes" if time else "No", "Yes" if date else "No")