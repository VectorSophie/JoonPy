from datetime import datetime, timedelta

def parse_time(t):
    return datetime.strptime(t, "%H:%M:%S")

current = parse_time(input())
start = parse_time(input())

if start <= current:
    start += timedelta(days=1)

print(str(start - current).zfill(8))