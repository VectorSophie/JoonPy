def fact(n):
    return n * fact(n-1) if n > 1 else 1

a = int(input())  
b = str(fact(a))  
cnt = 0  

for i in range(len(b)): 
    if b[-(i+1)] == '0':  
        cnt += 1
    else:
        break  
print(cnt)  
