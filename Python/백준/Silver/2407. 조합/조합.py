import math
import sys

n, m = map(int, sys.stdin.readline().split())
result = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
print(result)