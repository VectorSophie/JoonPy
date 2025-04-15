N = int(input())
sum_1 = [i for i in range(1,N+1)]
sum_2 = [i**3 for i in sum_1]

print(sum(sum_1))
print(sum(sum_2))
print(sum(sum_1)**2)
