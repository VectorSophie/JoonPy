while True:
    n = input().strip()
    if n == '0':
        break
    remainder = 0
    for digit in n:
        remainder = (remainder * 10 + int(digit)) % 42
    if remainder == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
