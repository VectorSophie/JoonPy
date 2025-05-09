L, P = map(int, input().split())
arr = list(map(int, input().split()))
expect = L * P
diff = [x - expect for x in arr]
print(*diff)
