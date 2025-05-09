T = int(input())
for i in range(T):
	left,right = input().split('=')
	if eval(left.strip()) == int(right.strip()):
		truth = "YES"
	else:
		truth = "NO"
	
	print(f"Case {i+1}: {truth}")