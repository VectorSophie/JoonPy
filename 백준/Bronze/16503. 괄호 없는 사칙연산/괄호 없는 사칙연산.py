def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        sign = -1 if (a < 0) ^ (b < 0) else 1
        a_abs, b_abs = abs(a), abs(b)
        return sign * (a_abs // b_abs)

expr = input().split()
K1, O1, K2, O2, K3 = expr[0], expr[1], expr[2], expr[3], expr[4]
K1, K2, K3 = int(K1), int(K2), int(K3)

res1 = calc(calc(K1, O1, K2), O2, K3)  
res2 = calc(K1, O1, calc(K2, O2, K3))  

print(min(res1, res2))
print(max(res1, res2))