N=int(input())
for _ in range(N):
	a,h=map(float,input().split())
	print(f'The height of the triangle is {(2*a)/h:.2f} units')