arr = []
for i in range(10):
    a = int(input())
    arr.append(a)
arr_fix = [i % 42 for i in arr]
set_arr = set(arr_fix)
print(len(set_arr))