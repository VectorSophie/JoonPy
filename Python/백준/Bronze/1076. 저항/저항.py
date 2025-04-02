res_val = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
res_mult = {key: 10 ** value for key, value in res_val.items()}
val1 = input()
val2 = input()
mult = input()
print((res_val[val1]*10+res_val[val2]) * res_mult[mult])