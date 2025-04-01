arr = list(map(int, input().split()))
new_arr = list(map(lambda x: x*x, arr))
print(sum(new_arr) % 10)