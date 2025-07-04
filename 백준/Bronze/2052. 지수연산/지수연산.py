from decimal import Decimal, getcontext

N = int(input())
getcontext().prec = 300
result = Decimal(1) / (Decimal(2) ** N)
s = format(result.normalize(), 'f')
print(s.rstrip('0').rstrip('.') if '.' in s else s)