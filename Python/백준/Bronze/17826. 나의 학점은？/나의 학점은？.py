A = list(map(int, input().split()))
H = int(input())
A.append(H)
A.sort(reverse=True)
L = A.index(H)
if L >=0 and L <= 4:
	print("A+")
elif L >=5 and L <= 14:
	print("A0")
elif L >=15 and L <= 29:
	print("B+")
elif L >=30 and L <= 34:
	print("B0")
elif L >=35 and L <= 44:
	print("C+")
elif L >=45 and L <= 47:
	print("C0")
elif L >= 48 and L <= 49:
	print("F")