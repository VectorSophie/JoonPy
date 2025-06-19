N = int(input())

start_y = 2024
start_m = 8
total_m = start_m + (N - 1) * 7
yearpp = (total_m - 1) // 12

print((start_y + yearpp), ((total_m - 1) % 12 + 1))
