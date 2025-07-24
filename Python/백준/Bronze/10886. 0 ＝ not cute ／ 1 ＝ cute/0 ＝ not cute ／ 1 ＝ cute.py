n = int(input())  
cute = 0          
for _ in range(n):
    vote = int(input())
    if vote == 1:
        cute += 1

print("Junhee is cute!" if cute > (n-cute) else "Junhee is not cute!")