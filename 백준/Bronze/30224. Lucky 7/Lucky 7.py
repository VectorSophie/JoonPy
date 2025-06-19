num = int(input().strip())
contains_7 = '7' in str(num)
div_7 = (num % 7 == 0)

if not contains_7 and not div_7:
    print(0)
elif not contains_7 and div_7:
    print(1)
elif contains_7 and not div_7:
    print(2)
else:  
    print(3)
